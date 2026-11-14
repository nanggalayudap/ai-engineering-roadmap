"""
LATIHAN DEBUG - FOR & WHILE LOOP
================================
Cara pakai:
    1. Jangan menghapus / mengubah nama fungsi maupun test otomatis di bawah.
    2. Jalankan:  python latihan_debug.py
    3. Semua test yang masih [XX] / [!!] mengandung bug. Temukan & perbaiki.
    4. Target akhir: semua test OK.

Petunjuk membaca hasil test:
    [XX] = tidak crash, tapi hasilnya salah
    [!!] = error saat dijalankan (crash)
    [  ] = TODO / belum diisi

Aturan main:
    - Boleh mengubah kode DI DALAM fungsi.
    - Jawab soal analisis (Bagian A) secara lisan/tulis di kertas dulu,
      baru lihat kunci di latihan_debug_solusi.py kalau buntu.
"""


# ===========================================================================
# BAGIAN A - ANALISIS KODE (JAWAB DI KERTAS, TIDAK PERLU DIJALANKAN)
# ===========================================================================
# A1. Kode ini tidak pernah berhenti, kenapa?
#
#     n = 5
#     while n < 10:
#         print("Halo", n)
#
# A2. Niat aslinya: cetak hanya angka genap 1..10.
#     Tapi yang dicetak cuma 2 saja. Kenapa?
#
#     for i in range(1, 11):
#         if i % 2 != 0:
#             break
#         print(i)
#
# A3. Mencoba menghapus semua elemen bernilai 0 dari list,
#     tapi hasilnya masih ada 0 yang tersisa. Kenapa?
#     (Petunjuk: iterasi list sambil mengubah list itu sendiri)
#
#     angka = [0, 1, 0, 2, 3, 0]
#     for a in angka:
#         if a == 0:
#             angka.remove(a)
#
# A4. is_lolos(90) seharusnya True, tapi program malah crash.
#     for i in range(len(nilai) + 1):
#         if nilai[i] >= 90:
#             return True
#     Pertanyaan: indeks mana yang bermasalah, dan kenapa?
#
# A5. Perulangan ini tidak pernah mencetak "Selesai".
#     i = 0
#     while i != 5:
#         i += 2
#         print(i)
#     else:
#         print("Selesai")
#     Pertanyaan: kenapa cabang else tidak pernah dieksekusi?
#
# A6. Kode di bawah error IndexError. Apa penyebab & perbaikannya?
#
#     buah = ["apel", "jeruk", "mangga"]
#     i = 0
#     while i <= len(buah):
#         print(buah[i])
#         i += 1


# ===========================================================================
# BAGIAN B - KODE BERMASALAH (PERBAIKI, LALU JALANKAN TEST)
# ===========================================================================

def cetak_1_sampai_10():
    """Bug #1 - Seharusnya mengembalikan [1, 2, ..., 10]."""
    hasil = []
    for i in range(1, 10):
        hasil.append(i)
    return hasil


def jumlah_1_sampai_100():
    """Bug #2 - Seharusnya mengembalikan 5050."""
    total = 0
    for i in range(1, 101):
        total = i
    return total


def fizzbuzz(n):
    """Bug #3 - Kelipatan 15 seharusnya 'FizzBuzz', bukan 'Fizz'."""
    hasil = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            hasil.append("Fizz")
        elif i % 5 == 0:
            hasil.append("Buzz")
        elif i % 15 == 0:
            hasil.append("FizzBuzz")
        else:
            hasil.append(str(i))
    return hasil


def balik_string(teks):
    """Bug #4 - Program crash (IndexError). Seharusnya 'nohtyp'."""
    hasil = ""
    i = len(teks)
    while i >= 0:
        hasil += teks[i]
        i -= 1
    return hasil


def huruf_vokal(teks):
    """Bug #5 - 'PYTHON' seharusnya ['O']. Hasil sekarang kosong."""
    hasil = []
    for huruf in teks:
        if huruf in "aeiou":
            hasil.append(huruf)
    return hasil


def is_prima(n):
    """Bug #6 - is_prima(9) seharusnya False (9 = 3 x 3)."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True


def cari_elemen(data, target):
    """Bug #7 - Deteksi first occurrence tidak bekerja.

    cari_elemen([3, 1, 4, 1, 5], 1) seharusnya mengembalikan indeks 1.
    """
    for i, nilai in enumerate(data):
        if nilai == target:
            continue
        return i
    return -1


def total_baris(matriks):
    """Bug #8 - Harusnya mengembalikan list total tiap baris.

    total_baris([[1, 2], [3, 4, 5]]) -> [3, 12]
    """
    hasil = []
    total = 0
    for baris in matriks:
        for ang in baris:
            total += ang
        hasil.append(total)
    return hasil


# ===========================================================================
# TEST OTOMATIS - jangan diubah
# ===========================================================================

def _jalankan_test():
    kasus = [
        ("Bug #1 cetak_1_sampai_10()", cetak_1_sampai_10, (),
         list(range(1, 11))),
        ("Bug #2 jumlah_1_sampai_100()", jumlah_1_sampai_100, (), 5050),
        ("Bug #3 fizzbuzz(15)", fizzbuzz, (15,),
         ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
          "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]),
        ("Bug #4 balik_string('python')", balik_string, ("python",), "nohtyp"),
        ("Bug #5 huruf_vokal('PYTHON')", huruf_vokal, ("PYTHON",), ["O"]),
        ("Bug #6 is_prima(9)", is_prima, (9,), False),
        ("Bug #6 is_prima(7)", is_prima, (7,), True),
        ("Bug #7 cari_elemen index ke-1", cari_elemen,
         ([3, 1, 4, 1, 5], 1), 1),
        ("Bug #8 total_baris", total_baris,
         ([[1, 2], [3, 4, 5]],), [3, 12]),
    ]

    lulus = 0
    for label, fungsi, argumen, harapan in kasus:
        try:
            hasil = fungsi(*argumen)
        except NotImplementedError:
            print(f"  [  ]  {label:<32} belum diisi")
            continue
        except Exception as e:
            lulus += 0
            print(f"  [!!]  {label:<32} error: {type(e).__name__}: {e}")
            continue

        if hasil == harapan:
            lulus += 1
            print(f"  [OK]  {label:<32} -> {hasil!r}")
        else:
            print(f"  [XX]  {label:<32} -> {hasil!r}  (harusnya {harapan!r})")

    print(f"\nSkor: {lulus}/{len(kasus)} test lulus")
    if lulus == len(kasus):
        print("Semua bug berhasil diperbaiki!")
    else:
        print("Masih ada bug. Baca ulang bagian yang [XX] / [!!].")


if __name__ == "__main__":
    print("Latihan Debug Loop Python - hasil test:\n")
    _jalankan_test()
