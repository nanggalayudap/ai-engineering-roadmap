"""
KUNCI JAWABAN - LATIHAN DEBUG LOOP
===================================
Isi file ini ada di sini (harga sebenarnya), tapi untuk jaga-jaga
kalau file ini hilang, ini pembahasan lengkapnya:

--- JAWABAN BAGIAN A (ANALISIS) ---

A1. Variabel n tidak pernah berubah di dalam loop.
    Perbaikan: tambahkan n += 1 (atau ganti pakai for).

A2. `break` bukan `continue`.
    break menghentikan SELURUH loop saat bertemu angka ganjil pertama (1),
    jadi hanya 2 yang tercetak. Perbaikan: ganti break -> continue.

A3. Iterasi list sambil mengubah list itu sendiri (remove) bikin index
    "loncat" dan melewatkan beberapa elemen.
    Perbaikan: iterate over a copy: for a in angka[:]:
               atau list comprehension: angka = [a for a in angka if a != 0]

A4. range(len(nilai) + 1) membuat indeks berakhir di len(nilai),
    padahal indeks valid adalah 0 sampai len(nilai) - 1.
    Perbaikan: range(len(nilai))

A5. while i != 5: i += 2 -> i berjalan 2, 4, 6, 8, ... (genap),
    tidak pernah berhenti tepat di 5. else hanya jalan saat kondisi while
    FALSE (loop selesai normal), bukan saat break.
    Perbaikan: while i <= 5 atau gunakan kondisi yang pasti tercapai.

A6. while i <= len(buah) -> indeks maksimal len(buah) - 1.
    len(buah) = 3, indeks valid 0, 1, 2. Indeks 3 tidak ada.
    Perbaikan: while i < len(buah)

--- JAWABAN BAGIAN B (PERBAIKAN KODE) ---

Bug #1 - range(1, 10) -> range(1, 11)  (stop eksklusif)

Bug #2 - total = i -> total += i  (akumulasi, bukan replace)

Bug #3 - urutan cek salah: cek i % 15 (3 dan 5) harus SEBELUM i % 3 dan i % 5

Bug #4 - i = len(teks) -> i = len(teks) - 1  (indeks terakhir = panjang - 1)

Bug #5 - tidak ada penanganan huruf besar/kecil.
    Perbaikan: if huruf.lower() in "aeiou":
               hasil.append(huruf.upper())  # atau .lower() sesuai kebutuhan

Bug #6 - range(2, int(n ** 0.5)) -> range(2, int(n ** 0.5) + 1)
    range stop eksklusif, +1 diperlukan agar akar kuadrat ikut diperiksa.
    Contoh: n=9, int(9**0.5)=3, range(2,3)=[2] -> 3 tidak dicek.
    Perbaikan: range(2, int(n**0.5) + 1)

Bug #7 - logika continue terbalik.
    Harusnya: kalau nilai == target -> return i (langsung temukan)
              kalau bukan -> lanjut
    Kode salah: continue saat COCOK, return i saat TIDAK COCOK.
    Perbaikan:
        if nilai == target:
            return i

Bug #8 - total tidak di-reset antar baris.
    Perbaikan: pindahkan total = 0 ke dalam loop luar (setiap baris baru)
    atau gunakan sum(baris) langsung.

--- CARA CEK ---
Jalankan latihan_debug.py lagi setelah perbaikan. Semua test harus [OK].
"""