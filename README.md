
# Strategic Revenue & Logistics Optimization: E-Commerce Case Study

## Project Background

Proyek ini menganalisis **Brazilian E-Commerce Public Dataset by Olist** yang berisi data transaksi riil dari 100.000 pesanan di pasar Brasil selama periode 2016 hingga 2018. Dataset ini memiliki struktur relasional kompleks yang menghubungkan informasi pesanan, detail item, spesifikasi produk, hingga data logistik. Fokus utama analisis ini adalah mengevaluasi performa pendapatan, akurasi janji pengiriman (SLA), dan dampak biaya logistik terhadap retensi pesanan.

## Business Insights Analysis

### 1. Revenue Drivers & Market Trend

Analisis dilakukan untuk mengidentifikasi kategori produk penyumbang pendapatan terbesar dan memantau fluktuasi pasar.

* **Kategori Utama**: `beleza_saude` (kecantikan & kesehatan) dan `relogios_presentes` (jam tangan & kado) secara konsisten menjadi kontributor pendapatan tertinggi.
* **Momentum Musiman**: Terjadi lonjakan volume pesanan yang signifikan pada November 2017, didorong oleh efektivitas kampanye promosi akhir tahun.
* **Stabilitas Sektor**: Sektor peralatan rumah tangga (`cama_mesa_banho`) menunjukkan performa stabil dengan permintaan yang konsisten sepanjang tahun.

### 2. Logistics & Operational Efficiency

Analisis ini membandingkan realita waktu pengiriman dengan janji estimasi yang diberikan kepada pelanggan di tahun 2018.

* **Performa SLA**: Rata-rata durasi pengiriman aktual (di bawah 15 hari) jauh lebih cepat dibandingkan estimasi perusahaan yang berada di kisaran 20-24 hari.
* **Peningkatan Efisiensi**: Terdapat tren penurunan waktu pengiriman dari kuartal pertama ke kuartal ketiga tahun 2018, menunjukkan optimalisasi pada proses distribusi.
* **Peluang Kompetitif**: Selisih waktu yang lebar antara aktual dan estimasi memberi ruang bagi bisnis untuk menjanjikan waktu pengiriman yang lebih singkat guna menarik pelanggan baru.

### 3. Pricing Sensitivity & Order Cancellations

Analisis rasio biaya pengiriman terhadap harga barang untuk memahami perilaku pembatalan pesanan.

* **Beban Ongkir**: Kategori seperti `telefonia` memiliki rasio biaya pengiriman yang sangat tinggi terhadap harga barang (mencapai ~0.5), yang memengaruhi keputusan akhir pembeli.
* **Korelasi Pembatalan**: Tingginya rasio ongkir berkontribusi langsung pada tingkat pembatalan pesanan, terlihat jelas pada kategori `utilidades_domesticas` yang memiliki *cancellation rate* tertinggi.
* **Strategi Mitigasi**: Untuk kategori dengan barang ringan namun bernilai rendah, strategi subsidi ongkir atau *bundling* produk sangat disarankan untuk menekan angka pembatalan di keranjang belanja.

---

## Run Dashboard Locally

### 1. Setup Environment

Pastikan kamu sudah menginstal **Python** (disarankan versi 3.9 hingga 3.12 untuk stabilitas terbaik). Buka terminal atau command prompt, lalu buat *virtual environment* agar library tidak bentrok dengan proyek lain:

```bash
# Membuat virtual environment
python -m venv venv

# Mengaktifkan virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

```

### 2. Instal Dependencies
```bash
pip install -r requirements.txt

```
### 3. Jalankan Dashboard

```bash
streamlit run dashboard.py

```
cek pada url `http://localhost:8501`.
