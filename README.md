# 📚 Screaping Data Buku

Proyek ini bertujuan untuk melakukan web scraping data buku dari situs [Gramedia Terutama Kategori Fiksi](https://www.gramedia.com/categories/buku/fiksi-sastra). Data yang diperoleh mencakup informasi seperti judul, dan harga, yang kemudian disimpan dalam format CSV untuk analisis lebih lanjut.

## 🛠️ Teknologi yang Digunakan

- **Python 3**: Bahasa pemrograman utama.
- **pandas**: Untuk memproses data, khususnya data terstruktur dalam bentuk tabel.
- **Selenium**: Untuk mem-parsing dan mengekstrak data dari HTML.

## 📄 Fitur

- Mengambil data dari semua kategori buku yang tersedia di situs.
- Menyimpan data setiap kategori dalam file CSV terpisah.
- Menangani berbagai elemen HTML untuk memastikan data yang lengkap dan akurat.

## 🚀 Cara Menggunakan

1. **Klon repositori ini**:

   ```bash
   git clone https://github.com/alwafa2/Screaping-Data-Buku.git
   cd Screaping-Data-Buku
   ```

2. **(Opsional) Buat dan aktifkan virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```

3. **Install dependensi**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan skrip utama**:

   ```bash
   python main.py
   ```

   Hasil scraping akan disimpan dalam folder `data/` dengan format `.csv`.

## 📁 Struktur Proyek

```
Screaping-Data-Buku/
├── data/               # Folder untuk menyimpan file CSV hasil scraping
├── main.py             # Skrip utama untuk melakukan scraping
└── README.md           # Dokumentasi proyek
```

## ✅ Etika Web Scraping

Saat melakukan web scraping, penting untuk memperhatikan etika dan kebijakan situs web yang dituju:

- 📜 **Periksa robots.txt**: Pastikan scraping diperbolehkan oleh situs target.
- ⏳ **Tambahkan jeda waktu (delay)**: Hindari mengirim terlalu banyak permintaan dalam waktu singkat untuk mencegah membebani server.
- 🤝 **Hormati hak cipta**: Jangan gunakan data yang diperoleh untuk keperluan komersial jika tidak diizinkan.
- 🔒 **Jangan scraping data pribadi**: Fokuslah pada informasi yang tersedia untuk umum.
- 📬 **Hubungi pemilik situs jika perlu**: Untuk penggunaan data dalam skala besar atau tujuan tertentu.

Situs [Books to Scrape](http://books.toscrape.com/) secara eksplisit disediakan untuk keperluan latihan web scraping dan analisis data.

## ⚠️ Catatan
- Pastikan koneksi internet stabil saat menjalankan skrip.
- Situs target dapat mengalami perubahan struktur HTML; jika terjadi error, periksa dan sesuaikan selector di skrip.

## 🤝 Kontribusi

Kontribusi sangat terbuka! Silakan fork proyek ini dan ajukan *pull request*, atau buka *issue* jika ada masukan atau masalah.

## 📄 Lisensi
License © 2025 Muhammad Nailul Wafa
