# AI Codex Manager

AI Codex Manager adalah aplikasi sederhana untuk mengelola catatan, snippet kode, dan referensi terkait AI atau pemrograman. Cocok untuk menyimpan ide, solusi, dan pengetahuan yang ingin kamu dokumentasikan.

## ✨ Fitur

- Tambah entry baru (judul, kategori, tag, ringkasan, kode, sumber)
- Lihat semua entry
- Cari entry berdasarkan tag atau judul
- Hapus entry
- Data disimpan dalam format JSON

## 📦 Struktur Proyek

```
.
├── main.py
├── codex/
│   ├── entry.py
│   ├── manager.py
│   ├── category.py
│   ├── tag.py
│   └── exporter.py
├── interface/
│   └── cli.py
├── utils/
│   └── helpers.py
├── data/
│   └── entries.json
├── requirements.txt
├── README.md
├── LICENCE
└── .gitignore
```

## 🚀 Cara Menjalankan

1. **Clone repo ini**
2. (Opsional) Buat virtual environment dan install dependensi:
    ```sh
    python -m venv venv
    source venv/bin/activate  # atau venv\Scripts\activate di Windows
    pip install -r requirements.txt
    ```
3. **Jalankan aplikasi:**
    ```sh
    python main.py
    ```

## 🛠️ Dependensi

- Python 3.7+
- (Tidak ada dependensi eksternal, semua menggunakan modul standar Python)

## 📜 Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat file [LICENCE](LICENCE) untuk detailnya.