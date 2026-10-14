# Ruang Belanja

Toko demo dengan dua pilihan menjalankan aplikasi: website statis untuk GitHub Pages dan aplikasi Flask untuk server Python.

## Demo publik

[Buka Ruang Belanja](https://hauzanwafi-jackals.github.io/Toko-Wapi-Alpro/)

GitHub Pages menyajikan versi `index.html`. Flask tidak dijalankan oleh GitHub Pages.

## Fitur

- Pencarian produk, filter kategori, dan pengurutan harga/nama.
- Favorit produk yang disimpan di browser.
- Keranjang dengan pengaturan jumlah dan total belanja.
- Checkout demo dengan ringkasan serta riwayat pesanan.

Keranjang, favorit, dan riwayat tersimpan di browser masing-masing. Checkout tidak memproses pembayaran atau pengiriman.

## Struktur proyek

```text
.
|-- index.html          # Versi statis untuk GitHub Pages
|-- toko wapi alpro.py  # Aplikasi Flask
|-- requirements.txt    # Dependency aplikasi Python
|-- .gitignore
`-- README.md
```

## Menjalankan versi statis

```bash
python -m http.server 8000
```

Buka http://localhost:8000/.

## Menjalankan versi Flask

Gunakan Python 3.10 atau lebih baru, lalu jalankan:

```bash
python -m venv .venv
```

Aktifkan environment:

```powershell
.venv\Scripts\Activate.ps1
```

Di macOS/Linux:

```bash
source .venv/bin/activate
```


Pasang dependency dan jalankan aplikasi:

```bash
python -m pip install -r requirements.txt
python "toko wapi alpro.py"
```

Buka http://localhost:5001/.

## Deployment

- **GitHub Pages:** gunakan branch `main` dan folder root. File `index.html` harus tetap berada di root repository.
- **Flask:** deploy ke layanan yang mendukung Python. Dependency terdaftar di `requirements.txt`; `gunicorn` tersedia untuk deployment Linux.

GitHub Pages tidak dapat menjalankan aplikasi Flask karena tidak menyediakan server Python.