# AI Codex Manager

**AI Codex Manager** adalah aplikasi Python untuk menyimpan, mencari, dan mengelola catatan, snippet kode, serta referensi seputar AI dan pemrograman. Cocok untuk developer dan pemula yang ingin membangun dokumentasi pribadi atau belajar mengorganisir pengetahuan teknis.

---

## 📖 Apa Itu Codex?

Codex adalah kumpulan entry yang berisi:
- **Judul**: Nama atau topik utama
- **Kategori**: Jenis atau kelompok (misal: Python, Machine Learning)
- **Tag**: Label pencarian (misal: array, decorator)
- **Ringkasan**: Penjelasan singkat
- **Kode**: Snippet atau contoh kode
- **Sumber**: Link atau referensi

---

## 🚀 Fitur Utama

- **Tambah Entry**: Simpan ide, solusi, atau snippet baru
- **Cari Entry**: Temukan catatan berdasarkan judul atau tag
- **Lihat Semua**: Tampilkan seluruh codex yang tersimpan
- **Hapus Entry**: Bersihkan catatan yang tidak diperlukan
- **Ekspor Data**: Konversi codex ke format lain (fitur lanjutan)
- **CLI Interaktif**: Mudah digunakan langsung dari terminal

---

## 🗂️ Struktur Proyek

```
ai_codex_manager/
├── main.py                # Entry point aplikasi
├── codex/
│   ├── entry.py           # Struktur data codex
│   ├── manager.py         # Logika CRUD codex
│   ├── category.py        # Manajemen kategori
│   ├── tag.py             # Manajemen tag
│   └── exporter.py        # Ekspor data codex
├── interface/
│   └── cli.py             # Command-line interface
├── utils/
│   └── helpers.py         # Fungsi pendukung
├── data/
│   └── entries.json       # hide Database codex (JSON)
├── requirements.txt
├── README.md
├── LICENCE
└── .gitignore
```

---

## 🏁 Cara Memulai

1. **Clone repository ini**
2. (Opsional) Buat virtual environment dan install dependensi:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # di Windows
    pip install -r requirements.txt
    ```
3. **Jalankan aplikasi:**
    ```sh
    python main.py
    ```
4. Ikuti instruksi di terminal untuk menambah, mencari, atau mengelola codex.

---

## 💡 Tips Penggunaan

- Gunakan tag dan kategori agar pencarian lebih mudah.
- Simpan snippet kode yang sering digunakan.
- Tambahkan sumber agar mudah menemukan referensi asli.

---

## 🛠️ Dependensi

- Python 3.7+
- Modul standar Python (json, os, argparse, dll)

---

## 📜 Lisensi

Proyek ini menggunakan MIT License. Silakan cek [LICENCE](LICENCE) untuk detailnya.