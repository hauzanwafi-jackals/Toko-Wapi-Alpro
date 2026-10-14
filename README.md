# Ruang Belanja

Website toko sederhana yang dibuat dengan HTML, CSS, dan JavaScript agar bisa dipublikasikan di GitHub Pages.

## Fitur

- Cari produk, filter kategori, dan urutkan katalog berdasarkan harga atau nama.
- Simpan produk favorit dan tampilkan favorit saja; pilihan tersimpan di browser.
- Kelola jumlah barang di keranjang; keranjang juga tersimpan di browser.
- Simulasi checkout untuk melihat ringkasan pesanan demo.

Checkout masih berupa simulasi. Pembayaran dan pengiriman belum terhubung.

## Cara menjalankan lokal

1. Buka folder project.
2. Jalankan server lokal:

```bash
python -m http.server 8000
```

3. Buka browser ke:

```text
http://localhost:8000/
```

## Cara upload ke GitHub

1. Buka GitHub dan buat repository baru.
2. Upload file `index.html` ke repository.
3. Masuk ke `Settings` → `Pages`.
4. Pada bagian `Build and deployment`, pilih:
   - Source: `Deploy from a branch`
   - Branch: `main` atau `master`
   - Folder: `/root`
5. Klik `Save`.
6. Tunggu beberapa saat, lalu GitHub akan memberi URL seperti:

```text
https://username.github.io/nama-repository/
```

## Catatan

GitHub Pages hanya bisa menampilkan website statis. Karena Flask adalah aplikasi Python server-side, ia tidak bisa langsung dipublish di GitHub Pages tanpa backend.