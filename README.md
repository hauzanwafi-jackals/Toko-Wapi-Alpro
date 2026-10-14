# Ruang Belanja

Website toko sederhana yang dibuat dengan HTML, CSS, dan JavaScript agar bisa dipublikasikan di GitHub Pages.

## Akses publik

Buka toko di: https://hauzanwafi-jackals.github.io/Toko-Wapi-Alpro/

Versi publik menggunakan `index.html`. File Flask tersedia sebagai versi server Python, tetapi tidak dijalankan oleh GitHub Pages.

## Fitur

- Cari produk, filter kategori, dan urutkan katalog berdasarkan harga atau nama.
- Simpan produk favorit dan tampilkan favorit saja; pilihan tersimpan di browser.
- Kelola jumlah barang di keranjang; keranjang juga tersimpan di browser.
- Simulasi checkout untuk melihat ringkasan pesanan demo.
- Lihat konfirmasi dan riwayat pesanan demo yang tersimpan di browser.

Checkout masih berupa simulasi. Riwayat tersimpan hanya di browser yang digunakan; pembayaran dan pengiriman belum terhubung.

## Cara menjalankan lokal

### Versi statis

1. Buka folder project.
2. Jalankan server lokal:

```bash
python -m http.server 8000
```

3. Buka browser ke:

```text
http://localhost:8000/
```

### Versi Flask

Pasang Flask, lalu jalankan aplikasi Python:

```bash
python -m pip install Flask
python "toko wapi alpro.py"
```

Buka `http://localhost:5001/` di browser. Keranjang, favorit, dan riwayat pesanan demo disimpan di browser yang digunakan.

## Catatan

GitHub Pages hanya bisa menampilkan website statis dari `index.html`. Aplikasi Flask membutuhkan server Python dan tidak bisa dijalankan langsung di GitHub Pages.