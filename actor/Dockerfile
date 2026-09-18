# Menggunakan image dasar Python resmi dari Apify
FROM apify/actor-python:3.11

# Salin berkas requirements.txt untuk instalasi pustaka pendukung
COPY requirements.txt ./

# Instal pustaka pendukung tanpa menyimpan cache agar image tetap ringan
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh isi folder proyek ke dalam kontainer kerja
COPY . ./

# Perintah utama untuk mengeksekusi modul utama Python di dalam folder src
CMD ["python3", "-m", "src.main"]
