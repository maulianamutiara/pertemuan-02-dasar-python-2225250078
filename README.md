# Pertemuan 02 - Dasar Python

## Identitas

**Nama:** Mauliana Mutiara  
**NIM:** 2225250078  
**Kelas:** 3A

## Tujuan Repositori

Repositori ini digunakan untuk mengumpulkan hasil latihan dan tugas pada Pertemuan 02 mata kuliah Algoritma dan Pemrograman.

Materi yang dipraktikkan meliputi variabel, konstanta, tipe data, input-output, konversi tipe data, operator, serta pembuatan program sederhana menggunakan Python di VS Code.

## Daftar Berkas dan Fungsi

### Folder `latihan`

1. `latihan/01_biodata.py`
   - Memasukkan nama, NIM, kelas, dan tahun lahir.
   - Menghitung perkiraan umur berdasarkan tahun sekarang.

2. `latihan/02_persegi_panjang.py`
   - Memasukkan panjang dan lebar persegi panjang.
   - Menghitung luas dan keliling persegi panjang.

3. `latihan/03_konversi_suhu.py`
   - Memasukkan suhu dalam Celsius.
   - Mengubah Celsius menjadi Fahrenheit dan Kelvin.

4. `latihan/04_nilai_akhir.py`
   - Memasukkan nilai tugas, UTS, dan UAS.
   - Menghitung nilai akhir dengan bobot:
     - Tugas = 20%
     - UTS = 30%
     - UAS = 50%

### Folder `tugas`

5. `tugas/kalkulator_koordinat.py`
   - Memasukkan koordinat titik A dan titik B.
   - Menghitung perubahan koordinat (`dx` dan `dy`).
   - Menghitung jarak antara dua titik.
   - Menghitung titik tengah antara dua titik.

## Cara Menjalankan Program

Program dapat dijalankan melalui Terminal pada VS Code.

### Latihan 1

```bash
python latihan/01_biodata.py
python latihan/02_persegi_panjang.py
python latihan/03_konversi_suhu.py
python latihan/04_nilai_akhir.py
python tugas/kalkulator_koordinat.py

## Hasil Pengujian Tugas Utama

| No. | Titik A | Titik B | Jarak | Titik Tengah |
|---|---|---|---|---|
| 1 | (0, 0) | (3, 4) | 5.00 | (1.50, 2.00) |
| 2 | (-2, 1) | (4, 1) | 6.00 | (1.00, 1.00) |
| 3 | (2.5, -1) | (2.5, 3) | 4.00 | (2.50, 1.00) |

## Hasil Pengujian Latihan

### Latihan 1 - Biodata

Input:
- Nama: Mauliana Mutiara
- NIM: 2225250078
- Kelas: 3A
- Tahun lahir: 2005

Hasil:
- Perkiraan umur: 21 tahun

### Latihan 2 - Persegi Panjang

Pengujian 1:
- Panjang = 8
- Lebar = 5
- Luas = 40.00
- Keliling = 26.00

Pengujian 2:
- Panjang = 2.5
- Lebar = 4
- Luas = 10.00
- Keliling = 13.00

### Latihan 3 - Konversi Suhu

Pengujian 1:
- Celsius = 0
- Fahrenheit = 32.00
- Kelvin = 273.15

Pengujian 2:
- Celsius = 100
- Fahrenheit = 212.00
- Kelvin = 373.15

### Latihan 4 - Nilai Akhir

Pengujian 1:
- Nilai tugas = 80
- Nilai UTS = 80
- Nilai UAS = 80
- Nilai akhir = 80.00

Pengujian 2:
- Nilai tugas = 70
- Nilai UTS = 80
- Nilai UAS = 90
- Nilai akhir = 83.00

## Refleksi

Pada pertemuan ini saya memahami penggunaan variabel, konstanta, tipe data, input-output, konversi tipe data, dan operator dalam Python.

Saya juga memahami bahwa input dari pengguna perlu menggunakan tipe data yang sesuai, seperti int untuk bilangan bulat dan float untuk bilangan desimal.

Kesalahan yang saya temukan selama mengerjakan latihan adalah kesalahan dalam penulisan kode dan tipe data. Saya memperbaikinya dengan memeriksa kembali kode dan menjalankan program menggunakan beberapa input.

Pada pertemuan berikutnya saya ingin lebih memahami penggunaan percabangan dan membuat program yang lebih kompleks.

## Sumber

- Bahan Ajar Dasar Python di VS Code dan Pengumpulan melalui GitHub, Pertemuan ke-2, Algoritma dan Pemrograman, S1 Pendidikan Matematika FKIP Untirta.
- Python Tutorial.
- Visual Studio Code - Getting Started with Python.
- GitHub Docs.