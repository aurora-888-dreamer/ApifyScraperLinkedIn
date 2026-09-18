\# LinkedIn \& Loker.id Multi-Portal Scraper (Apify Actor)



Actor Apify berbasis Python ini dirancang untuk melakukan scraping data lowongan kerja (loker) di Indonesia dari dua portal besar secara asinkronus: \*\*LinkedIn Jobs (Halaman Publik)\*\* dan \*\*Loker.id\*\*. Actor ini berjalan tanpa memerlukan akses login personal (\*credentials\*) sehingga sangat aman dari risiko pemblokiran akun.



\## 🚀 Fitur Utama

\- \*\*Multi-Target Portal:\*\* Memilih target antara LinkedIn (Skala Makro/Korporat) atau Loker.id (Skala Nasional/UMKM) langsung melalui dropdown UI.

\- \*\*Tanpa Login:\*\* Memanfaatkan antarmuka publik dan teknik rotasi proxy bawaan dari Apify guna meminimalisir pemblokiran IP (\*Anti-Bot Protection\*).

\- \*\*Asynchronous HTTP Client:\*\* Menggunakan pustaka `httpx` untuk proses pengambilan data yang super cepat dan efisien.

\- \*\*Ekspor Data Terstruktur:\*\* Output data secara otomatis memiliki format kolom yang seragam, memudahkan Anda mengunduhnya langsung ke format `JSON`, `CSV`, atau `XLSX (Excel)`.



\## 📁 Struktur Direktori Proyek

Pastikan struktur file di komputer Anda tersusun sebagai berikut sebelum diunggah ke Apify Console:

```text

.

├── src/

│   └── main.py              # Logika utama scraping \& integrasi SDK Apify

├── actor.json               # Manifes konfigurasi Actor di platform Apify

├── input\_schema.json        # Desain formulir UI input untuk pengguna

├── requirements.txt         # Daftar pustaka Python (httpx, beautifulsoup4, apify)

├── Dockerfile               # Instruksi pembentukan runtime container cloud

└── README.md                # Dokumentasi petunjuk penggunaan (File ini)

```



\## ⚙️ Konfigurasi Input (UI Dashboard)

Saat menjalankan Actor ini melalui Apify Console, Anda dapat mengisi parameter berikut pada tab \*\*Input\*\*:



| Field / Key | Tipe Data | Deskripsi | Contoh Nilai |

| :--- | :--- | :--- | :--- |

| `target\_portal` | `string` | Pilihan portal target loker (\*select dropdown\*) | `linkedin` atau `loker\_id` |

| `query` | `string` | Kata kunci posisi pekerjaan yang dicari | `Python Developer` |

| `location` | `string` | Wilayah penempatan kerja (\*Khusus LinkedIn\*) | `Indonesia` atau `Jakarta` |

| `max\_pages` | `integer`| Batas halaman pencarian yang ingin diambil | `2` |



\## 📊 Contoh Output Data (Dataset)

Setelah Actor selesai berjalan (\*Status: Succeeded\*), hasil ekstraksi lowongan kerja akan disimpan ke dalam \*\*Apify Dataset\*\* dengan format skema seperti berikut:



```json

\[

&#x20; {

&#x20;   "sumber": "LinkedIn",

&#x20;   "posisi": "Python Backend Developer",

&#x20;   "perusahaan": "PT Teknologi Maju Bersama",

&#x20;   "lokasi": "Jakarta Raya, Indonesia",

&#x20;   "link\_lamar": "https://linkedin.com"

&#x20; },

&#x20; {

&#x20;   "sumber": "Loker.id",

&#x20;   "posisi": "Junior Python Developer",

&#x20;   "perusahaan": "Startup Kreatif Nusantara",

&#x20;   "lokasi": "Indonesia",

&#x20;   "link\_lamar": "https://loker.id"

&#x20; }

]

```



\## 🛠️ Pengembangan Lokal (Local Development)

Jika Anda ingin menguji dan menjalankan proyek ini langsung di komputer lokal menggunakan \*\*Apify CLI\*\*:



1\. Pastikan Node.js dan Apify CLI telah terinstal di komputer Anda.

2\. Jalankan perintah inisialisasi lokal:

&#x20;  ```bash

&#x20;  apify login

&#x20;  ```

3\. Jalankan Actor secara lokal untuk simulasi testing:

&#x20;  ```bash

&#x20;  apify run

&#x20;  ```



\## ⚖️ Catatan Etika Penggunaan (Disclaimer)

Scraper ini dibuat murni untuk keperluan edukasi, riset pasar kerja, dan analisis data pribadi. Pengguna bertanggung jawab penuh atas frekuensi scraping yang dilakukan. Selalu patuhi berkas `robots.txt` pada masing-masing domain target dan gunakan fitur \*\*Apify Proxy\*\* bawaan untuk menjaga stabilitas akses server tujuan.



