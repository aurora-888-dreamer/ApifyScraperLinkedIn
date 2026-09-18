import asyncio
from apify import Actor
from bs4 import BeautifulSoup
import httpx
import random

async def main():
    async with Actor:
        # 1. Mengambil input dari user di platform Apify
        actor_input = await Actor.get_input() or {}
        keyword = actor_input.get("keyword", "Python Developer")
        location = actor_input.get("location", "Indonesia")
        max_pages = actor_input.get("max_pages", 3)

        print(f"Memulai scraping lowongan kerja untuk posisi: '{keyword}' di '{location}'...")

        # 2. Mengaktifkan Apify Proxy (PENTING untuk menghindari blokir IP)
        proxy_configuration = await Actor.create_proxy_configuration()
        # Jika menggunakan akun free, pastikan tipe proxy disesuaikan atau gunakan proxy otomatis
        proxy_url = await proxy_configuration.new_url() if proxy_configuration else None
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9,id;q=0.8"
        }

        # Menggunakan HTTPX client async dengan proxy
        transport = httpx.AsyncHTTPTransport(proxy=proxy_url) if proxy_url else None
        
        async with httpx.AsyncClient(headers=headers, transport=transport, timeout=30.0) as client:
            for page in range(max_pages):
                # Hitung start index untuk pagination halaman publik LinkedIn
                start_index = page * 25
                url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keyword}&location={location}&start={start_index}"
                
                print(f"Mengakses halaman ke-{page + 1}: {url}")
                
                try:
                    response = await client.get(url)
                    
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        # Halaman publik menggunakan struktur <li> untuk daftar loker
                        job_cards = soup.find_all('li')
                        
                        if not job_cards:
                            print("Tidak ada lowongan lagi yang ditemukan atau halaman diblokir.")
                            break
                            
                        for card in job_cards:
                            # Mengambil data dari elemen HTML publik LinkedIn Jobs
                            title_tag = card.find('h3', class_='base-search-card__title')
                            company_tag = card.find('a', class_='hidden-nested-link')
                            location_tag = card.find('span', class_='job-search-card__location')
                            link_tag = card.find('a', class_='base-card__full-link')
                            
                            if title_tag:
                                job_data = {
                                    "title": title_tag.text.strip(),
                                    "company": company_tag.text.strip() if company_tag else "N/A",
                                    "location": location_tag.text.strip() if location_tag else "N/A",
                                    "url": link_tag['href'].split('?')[0] if link_tag and 'href' in link_tag.attrs else "N/A"
                                }
                                
                                # 3. Menyimpan hasil data ke Apify Dataset (otomatis jadi JSON/CSV)
                                await Actor.push_data(job_data)
                                print(f"Berhasil menyimpan: {job_data['title']} - {job_data['company']}")
                    
                    elif response.status_code == 429:
                        print("Terkena Rate Limit (429). Coba aktifkan/ganti Proxy Apify Anda.")
                        break
                    else:
                        print(f"Gagal mengambil data. Status code: {response.status_code}")
                        
                except Exception as e:
                    print(f"Terjadi error saat request: {e}")
                
                # Jeda acak antar halaman agar lebih human-like
                await asyncio.sleep(random.uniform(3.0, 7.0))

if __name__ == "__main__":
    asyncio.run(main())