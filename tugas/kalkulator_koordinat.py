"""
Nama : Mauliana Mutiara
NIM  : 2225250078
Kelas: 3A
"""

x1 = float(input("Masukkan x titik A: "))
y1 = float(input("Masukkan y titik A: "))
x2 = float(input("Masukkan x titik B: "))
y2 = float(input("Masukkan y titik B: "))

dx = x2 - x1
dy = y2 - y1

jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

titik_tengah_x = (x1 + x2) / 2
titik_tengah_y = (y1 + y2) / 2

print("\n===== KALKULATOR KOORDINAT =====")
print(f"Titik A              : ({x1:.2f}, {y1:.2f})")
print(f"Titik B              : ({x2:.2f}, {y2:.2f})")
print(f"Perubahan dx         : {dx:.2f}")
print(f"Perubahan dy         : {dy:.2f}")
print(f"Jarak A ke B         : {jarak:.2f}")
print(f"Titik tengah         : ({titik_tengah_x:.2f}, {titik_tengah_y:.2f})")