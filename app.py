import os
from flask import Flask, render_template_string

app = Flask(__name__)

PRODUCTS = [
    {"id": "kopi-nusantara", "name": "Kopi Nusantara", "category": "Minuman", "price": 45000, "icon": "☕", "description": "Kopi pilihan dengan aroma yang kaya."},
    {"id": "teh-melati", "name": "Teh Melati", "category": "Minuman", "price": 32000, "icon": "🍵", "description": "Teh harum untuk jeda yang menenangkan."},
    {"id": "tas-kanvas", "name": "Tas Kanvas", "category": "Aksesori", "price": 85000, "icon": "👜", "description": "Tas serbaguna untuk aktivitas harian."},
    {"id": "dompet-kulit", "name": "Dompet Kulit", "category": "Aksesori", "price": 72000, "icon": "👛", "description": "Dompet ringkas dengan banyak ruang."},
    {"id": "tanaman-mini", "name": "Tanaman Mini", "category": "Dekorasi", "price": 35000, "icon": "🪴", "description": "Sentuhan hijau untuk meja favoritmu."},
    {"id": "lilin-aroma", "name": "Lilin Aroma", "category": "Dekorasi", "price": 54000, "icon": "🕯️", "description": "Aroma lembut untuk suasana nyaman."},
    {"id": "buku-catatan", "name": "Buku Catatan", "category": "Alat tulis", "price": 28000, "icon": "📓", "description": "Teman untuk ide dan catatan harian."},
    {"id": "pena-gel", "name": "Pena Gel", "category": "Alat tulis", "price": 12000, "icon": "🖊️", "description": "Tulisan halus untuk setiap halaman."},
]

HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ruang Belanja</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            min-height: 100vh;
            background: #f6f5f0;
            color: #20251f;
            font-family: Arial, sans-serif;
        }
        header {
            background: #fff;
            border-bottom: 1px solid #e8e8e1;
            padding: 18px 6%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .brand { font-size: 22px; font-weight: 700; color: #276749; }
        .cart {
            background: #276749;
            color: #fff;
            border: 0;
            border-radius: 9px;
            padding: 11px 16px;
            font-size: 15px;
        }
        main { width: min(1080px, 90%); margin: 48px auto; }
        .intro { margin-bottom: 30px; }
        .intro h1 { font-size: clamp(28px, 5vw, 40px); margin-bottom: 9px; }
        .intro p { color: #69716a; line-height: 1.6; }
        .products {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }
        .card {
            background: #fff;
            border: 1px solid #e8e8e1;
            border-radius: 15px;
            padding: 18px;
            box-shadow: 0 5px 18px rgba(30, 40, 30, .04);
        }
        .product-icon {
            height: 145px;
            display: grid;
            place-items: center;
            background: #eef5ed;
            border-radius: 11px;
            font-size: 64px;
            margin-bottom: 17px;
        }
        .category { color: #758078; font-size: 13px; margin-bottom: 7px; }
        .card h2 { font-size: 19px; margin-bottom: 12px; }
        .card-bottom {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 10px;
        }
        .price { font-weight: 700; color: #276749; }
        .add-button {
            border: 0;
            border-radius: 8px;
            padding: 9px 12px;
            background: #e5f2e7;
            color: #205a3b;
            font-weight: 700;
            cursor: pointer;
        }
        .add-button:hover { background: #d4ead8; }
        .summary {
            margin-top: 28px;
            padding: 20px;
            background: #fff;
            border: 1px solid #e8e8e1;
            border-radius: 13px;
            display: flex;
            justify-content: space-between;
            gap: 12px;
            flex-wrap: wrap;
        }
        .summary span { color: #276749; font-weight: 700; }
        .header-actions, .catalog-tools, .cart-actions, .result-actions { display: flex; align-items: center; gap: 10px; }
        .history-button, .plain-button { border: 1px solid #e5e7df; border-radius: 6px; padding: 10px 12px; background: #fff; color: #20251f; cursor: pointer; }
        .catalog-tools { display: grid; grid-template-columns: minmax(180px, 1.5fr) 1fr 1fr; margin: 20px 0 14px; }
        .catalog-tools input, .catalog-tools select, .checkout-form input, .checkout-form textarea { width: 100%; min-height: 42px; border: 1px solid #d9ddd4; border-radius: 5px; background: #fff; padding: 9px 11px; }
        .favorite-filter { display: flex; align-items: center; gap: 8px; font-size: 14px; }
        .favorite-button { float: right; border: 1px solid #e5e7df; border-radius: 50%; width: 36px; height: 36px; background: #fff; color: #9a533f; font-size: 22px; cursor: pointer; }
        .favorite-button[aria-pressed="true"] { background: #fff2ed; }
        .description { min-height: 36px; color: #69716a; font-size: 13px; line-height: 1.45; margin-bottom: 14px; }
        .empty-results { grid-column: 1 / -1; padding: 32px 12px; text-align: center; color: #69716a; }
        dialog { width: min(520px, calc(100% - 28px)); max-height: 82vh; margin: auto 0 auto auto; border: 0; padding: 0; color: #20251f; box-shadow: -12px 0 40px rgba(20,30,20,.18); }
        dialog::backdrop { background: rgba(19,30,21,.42); }
        .dialog-content { padding: 22px; }
        .dialog-head { display: flex; justify-content: space-between; align-items: center; gap: 12px; padding-bottom: 14px; border-bottom: 1px solid #e5e7df; }
        .cart-items, .order-list { display: grid; gap: 14px; max-height: 42vh; overflow: auto; padding: 16px 0; }
        .cart-row { display: grid; grid-template-columns: 44px 1fr auto; gap: 10px; align-items: center; }
        .cart-row-icon { display: grid; place-items: center; width: 44px; height: 44px; background: #eef5ed; border-radius: 5px; font-size: 24px; }
        .cart-row h3 { font-size: 14px; margin-bottom: 4px; }
        .cart-row p, .order-record p, .order-record li { color: #69716a; font-size: 12px; line-height: 1.5; }
        .quantity-control { display: flex; align-items: center; gap: 8px; margin-top: 6px; }
        .quantity-control button { width: 26px; height: 26px; border: 1px solid #e5e7df; border-radius: 4px; background: #fff; }
        .remove-button { grid-column: 2 / -1; justify-self: start; border: 0; background: transparent; color: #9a533f; cursor: pointer; }
        .cart-total, .order-record-head, .order-record-total { display: flex; justify-content: space-between; gap: 10px; font-weight: 700; }
        .cart-total { border-top: 1px solid #e5e7df; padding-top: 14px; }
        .cart-actions { justify-content: space-between; margin-top: 16px; }
        .cart-actions .primary-button:disabled { opacity: .5; cursor: not-allowed; }
        .checkout-form { display: grid; gap: 12px; padding-top: 16px; }
        .checkout-form label { display: grid; gap: 5px; font-size: 13px; }
        .checkout-form textarea { min-height: 75px; resize: vertical; }
        .checkout-note, .checkout-result { color: #69716a; font-size: 13px; line-height: 1.5; }
        .checkout-result { padding-top: 16px; }
        .result-items { display: grid; gap: 5px; margin-top: 10px; color: #20251f; }
        .result-actions { margin-top: 14px; }
        .order-record { border-bottom: 1px solid #e5e7df; padding-bottom: 14px; }
        .order-record ul { margin: 7px 0; padding-left: 18px; }
        @media (max-width: 520px) {
            header { padding: 15px 5%; }
            main { margin: 32px auto; }
            .header-actions { gap: 6px; }
            .cart, .history-button { padding: 9px 10px; font-size: 12px; }
            .catalog-tools { grid-template-columns: 1fr 1fr; }
            .catalog-tools input, .favorite-filter { grid-column: 1 / -1; }
            .card { padding: 12px; }
            .card-bottom { align-items: flex-start; flex-direction: column; }
            .add-button { width: 100%; }
        }
    </style>
</head>
<body>
    <header>
        <div class="brand">Ruang Belanja</div>
        <div class="header-actions">
            <button class="history-button" id="open-orders" type="button">Pesanan: <span id="order-count">0</span></button>
            <button class="cart" id="open-cart" type="button" aria-haspopup="dialog">Keranjang: <span id="cart-count">0</span></button>
        </div>
    </header>

    <main>
        <section class="intro">
            <h1>Temukan barang favoritmu</h1>
            <p>Pilihan sederhana untuk menemani aktivitas sehari-hari.</p>
        </section>

        <section class="catalog-tools" aria-label="Cari dan atur produk">
            <input id="search-input" type="search" placeholder="Cari nama barang..." aria-label="Cari produk">
            <select id="category-filter" aria-label="Filter kategori"><option value="all">Semua kategori</option></select>
            <select id="sort-select" aria-label="Urutkan produk">
                <option value="featured">Urutan pilihan</option>
                <option value="price-asc">Harga terendah</option>
                <option value="price-desc">Harga tertinggi</option>
                <option value="name">Nama A–Z</option>
            </select>
            <label class="favorite-filter"><input id="favorites-only" type="checkbox"> Favorit saja</label>
        </section>
        <p id="result-count" aria-live="polite"></p>
        <section class="products" aria-label="Daftar produk" id="product-list"></section>

        <section class="summary" aria-live="polite">
            <div>Jumlah barang: <span id="item-count">0</span></div>
            <div>Total belanja: <span id="total-price">Rp0</span></div>
        </section>
    </main>

    <dialog id="cart-dialog" aria-labelledby="cart-title">
        <div class="dialog-content">
            <div class="dialog-head"><h2 id="cart-title">Keranjang belanja</h2><button class="plain-button" type="button" data-close="cart-dialog">Tutup</button></div>
            <div id="cart-items" class="cart-items"></div>
            <div class="cart-total"><span>Total</span><span id="cart-total">Rp0</span></div>
            <div class="cart-actions"><button class="plain-button" id="clear-cart" type="button">Kosongkan</button><button class="cart primary-button" id="checkout-button" type="button">Lanjut checkout</button></div>
        </div>
    </dialog>

    <dialog id="checkout-dialog" aria-labelledby="checkout-title">
        <div class="dialog-content">
            <div class="dialog-head"><h2 id="checkout-title">Data pemesan</h2><button class="plain-button" type="button" data-close="checkout-dialog">Tutup</button></div>
            <form id="checkout-form" class="checkout-form">
                <label>Nama lengkap<input name="name" autocomplete="name" required maxlength="80"></label>
                <label>Nomor WhatsApp<input name="phone" type="tel" autocomplete="tel" required pattern="\\+?[0-9 ]{8,19}" title="Masukkan 8–19 digit, boleh diawali tanda +"></label>
                <label>Alamat pengiriman<textarea name="address" autocomplete="street-address" required maxlength="300"></textarea></label>
                <p class="checkout-note">Checkout ini simulasi. Pembayaran dan pengiriman belum terhubung.</p>
                <button class="cart primary-button" type="submit">Buat pesanan demo</button>
            </form>
            <div id="checkout-result" class="checkout-result" role="status" hidden>
                <p id="checkout-result-text"></p>
                <div id="checkout-result-items" class="result-items"></div>
                <div class="result-actions"><button class="cart primary-button" id="view-orders-after-checkout" type="button">Lihat riwayat</button><button class="plain-button" type="button" data-close="checkout-dialog">Selesai</button></div>
            </div>
        </div>
    </dialog>

    <dialog id="orders-dialog" aria-labelledby="orders-title">
        <div class="dialog-content">
            <div class="dialog-head"><h2 id="orders-title">Riwayat pesanan</h2><button class="plain-button" type="button" data-close="orders-dialog">Tutup</button></div>
            <div id="order-list" class="order-list"></div>
        </div>
    </dialog>

    <script>
        const products = {{ products|tojson }};
        const formatRupiah = (amount) => "Rp" + amount.toLocaleString("id-ID");
        const productList = document.getElementById("product-list");
        const categoryFilter = document.getElementById("category-filter");
        const favoritesOnly = document.getElementById("favorites-only");
        const cartDialog = document.getElementById("cart-dialog");
        const checkoutDialog = document.getElementById("checkout-dialog");
        const ordersDialog = document.getElementById("orders-dialog");
        const cartKey = "ruang-belanja-cart-v2";
        const favoritesKey = "ruang-belanja-favorites-v1";
        const ordersKey = "ruang-belanja-orders-v1";
        const readStorage = (key, fallback) => {
            try { return JSON.parse(localStorage.getItem(key) || JSON.stringify(fallback)); }
            catch { return fallback; }
        };
        let cart = readStorage(cartKey, {});
        let favorites = readStorage(favoritesKey, []);
        let orders = readStorage(ordersKey, []);

        if (!cart || typeof cart !== "object" || Array.isArray(cart)) cart = {};
        cart = Object.fromEntries(Object.entries(cart).filter(([id, quantity]) =>
            products.some((product) => product.id === id) && Number.isInteger(quantity) && quantity > 0
        ));
        if (!Array.isArray(favorites)) favorites = [];
        favorites = new Set(favorites.filter((id) => products.some((product) => product.id === id)));
        if (!Array.isArray(orders)) orders = [];
        orders = orders.map((order) => {
            if (!order || typeof order.id !== "string" || !Number.isFinite(Date.parse(order.createdAt)) || !Array.isArray(order.items)) return null;
            const items = order.items.filter((item) => item && products.some((product) => product.id === item.id) && Number.isInteger(item.quantity) && item.quantity > 0)
                .map((item) => ({ id: item.id, quantity: item.quantity }));
            return items.length ? { id: order.id, createdAt: order.createdAt, items } : null;
        }).filter(Boolean);

        function saveCart() { localStorage.setItem(cartKey, JSON.stringify(cart)); }
        function cartTotals() {
            return Object.entries(cart).reduce((totals, [id, quantity]) => {
                const product = products.find((item) => item.id === id);
                if (product) { totals.count += quantity; totals.price += product.price * quantity; }
                return totals;
            }, { count: 0, price: 0 });
        }
        function renderProducts() {
            const query = document.getElementById("search-input").value.trim().toLocaleLowerCase("id");
            const category = categoryFilter.value;
            const sort = document.getElementById("sort-select").value;
            let visible = products.filter((product) =>
                (category === "all" || product.category === category) &&
                (!favoritesOnly.checked || favorites.has(product.id)) &&
                `${product.name} ${product.category} ${product.description}`.toLocaleLowerCase("id").includes(query)
            );
            if (sort === "price-asc") visible.sort((a, b) => a.price - b.price);
            if (sort === "price-desc") visible.sort((a, b) => b.price - a.price);
            if (sort === "name") visible.sort((a, b) => a.name.localeCompare(b.name, "id"));
            document.getElementById("result-count").textContent = `${visible.length} produk ditemukan`;
            productList.innerHTML = visible.length ? visible.map((product) => `
                <article class="card">
                    <button class="favorite-button" type="button" data-favorite="${product.id}" aria-pressed="${favorites.has(product.id)}" aria-label="${favorites.has(product.id) ? "Hapus dari" : "Tambahkan ke"} favorit">${favorites.has(product.id) ? "♥" : "♡"}</button>
                    <div class="product-icon" aria-hidden="true">${product.icon}</div>
                    <p class="category">${product.category}</p><h2>${product.name}</h2>
                    <p class="description">${product.description}</p>
                    <div class="card-bottom"><span class="price">${formatRupiah(product.price)}</span><button class="add-button" type="button" data-add="${product.id}">Tambah</button></div>
                </article>
            `).join("") : '<p class="empty-results">Produk tidak ditemukan. Coba filter lain.</p>';
        }
        function renderCart() {
            const totals = cartTotals();
            document.getElementById("cart-count").textContent = totals.count;
            document.getElementById("item-count").textContent = totals.count;
            document.getElementById("total-price").textContent = formatRupiah(totals.price);
            document.getElementById("cart-total").textContent = formatRupiah(totals.price);
            document.getElementById("checkout-button").disabled = totals.count === 0;
            const rows = Object.entries(cart).map(([id, quantity]) => {
                const product = products.find((item) => item.id === id);
                return `<article class="cart-row"><div class="cart-row-icon" aria-hidden="true">${product.icon}</div><div><h3>${product.name}</h3><p>${formatRupiah(product.price)} / item</p><div class="quantity-control"><button type="button" data-change="-1" data-id="${id}" aria-label="Kurangi ${product.name}">−</button><span>${quantity}</span><button type="button" data-change="1" data-id="${id}" aria-label="Tambah ${product.name}">+</button></div></div><strong class="price">${formatRupiah(product.price * quantity)}</strong><button class="remove-button" type="button" data-remove="${id}">Hapus</button></article>`;
            }).join("");
            document.getElementById("cart-items").innerHTML = rows || '<p class="empty-results">Keranjangmu masih kosong.</p>';
            saveCart();
        }
        function renderOrders() {
            document.getElementById("order-count").textContent = orders.length;
            const list = document.getElementById("order-list");
            if (!orders.length) { list.innerHTML = '<p class="empty-results">Belum ada pesanan demo.</p>'; return; }
            list.replaceChildren(...orders.map((order) => {
                const items = order.items.map((item) => ({ ...products.find((product) => product.id === item.id), quantity: item.quantity }));
                const article = document.createElement("article");
                article.className = "order-record";
                const heading = document.createElement("div");
                heading.className = "order-record-head";
                const number = document.createElement("span"); number.textContent = order.id;
                const status = document.createElement("span"); status.textContent = "Demo";
                heading.append(number, status);
                const date = document.createElement("p"); date.textContent = new Date(order.createdAt).toLocaleString("id-ID");
                const itemList = document.createElement("ul");
                items.forEach((item) => { const row = document.createElement("li"); row.textContent = `${item.name} × ${item.quantity} — ${formatRupiah(item.price * item.quantity)}`; itemList.appendChild(row); });
                const total = items.reduce((sum, item) => sum + item.price * item.quantity, 0);
                const totalRow = document.createElement("div"); totalRow.className = "order-record-total";
                const label = document.createElement("span"); label.textContent = "Total";
                const price = document.createElement("span"); price.textContent = formatRupiah(total);
                totalRow.append(label, price); article.append(heading, date, itemList, totalRow);
                return article;
            }));
        }

        [...new Set(products.map((product) => product.category))].sort().forEach((category) => {
            const option = document.createElement("option"); option.value = category; option.textContent = category; categoryFilter.appendChild(option);
        });
        document.getElementById("search-input").addEventListener("input", renderProducts);
        categoryFilter.addEventListener("change", renderProducts);
        document.getElementById("sort-select").addEventListener("change", renderProducts);
        favoritesOnly.addEventListener("change", renderProducts);
        productList.addEventListener("click", (event) => {
            const favoriteButton = event.target.closest("[data-favorite]");
            if (favoriteButton) {
                const id = favoriteButton.dataset.favorite;
                if (favorites.has(id)) favorites.delete(id); else favorites.add(id);
                localStorage.setItem(favoritesKey, JSON.stringify([...favorites])); renderProducts(); return;
            }
            const button = event.target.closest("[data-add]");
            if (button) { cart[button.dataset.add] = (cart[button.dataset.add] || 0) + 1; renderCart(); }
        });
        document.getElementById("cart-items").addEventListener("click", (event) => {
            const change = event.target.closest("[data-change]");
            const remove = event.target.closest("[data-remove]");
            if (change) { const id = change.dataset.id; cart[id] = (cart[id] || 0) + Number(change.dataset.change); if (cart[id] <= 0) delete cart[id]; renderCart(); }
            if (remove) { delete cart[remove.dataset.remove]; renderCart(); }
        });
        document.getElementById("open-cart").addEventListener("click", () => cartDialog.showModal());
        document.getElementById("open-orders").addEventListener("click", () => { renderOrders(); ordersDialog.showModal(); });
        document.getElementById("clear-cart").addEventListener("click", () => { cart = {}; renderCart(); });
        document.querySelectorAll("[data-close]").forEach((button) => button.addEventListener("click", () => document.getElementById(button.dataset.close).close()));
        document.getElementById("checkout-button").addEventListener("click", () => {
            cartDialog.close(); document.getElementById("checkout-form").hidden = false;
            document.getElementById("checkout-result").hidden = true; checkoutDialog.showModal();
        });
        document.getElementById("checkout-form").addEventListener("submit", (event) => {
            event.preventDefault(); if (!event.currentTarget.reportValidity()) return;
            const items = Object.entries(cart).map(([id, quantity]) => ({ id, quantity })); if (!items.length) return;
            const order = { id: `RB-${Date.now().toString(36).toUpperCase()}`, createdAt: new Date().toISOString(), items };
            orders.unshift(order); localStorage.setItem(ordersKey, JSON.stringify(orders));
            const total = items.reduce((sum, item) => sum + products.find((product) => product.id === item.id).price * item.quantity, 0);
            cart = {}; renderCart(); event.currentTarget.hidden = true;
            document.getElementById("checkout-result-text").textContent = `Pesanan demo ${order.id} berhasil dibuat. Total ${formatRupiah(total)}. Pembayaran dan pengiriman belum diproses.`;
            document.getElementById("checkout-result-items").replaceChildren(...items.map((item) => {
                const product = products.find((entry) => entry.id === item.id); const row = document.createElement("p");
                row.textContent = `${product.name} × ${item.quantity} — ${formatRupiah(product.price * item.quantity)}`; return row;
            }));
            document.getElementById("checkout-result").hidden = false; renderOrders();
        });
        document.getElementById("view-orders-after-checkout").addEventListener("click", () => {
            checkoutDialog.close(); renderOrders(); ordersDialog.showModal();
        });
        renderProducts(); renderCart(); renderOrders();
    </script>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML, products=PRODUCTS)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5001)),
        debug=False,
    )
