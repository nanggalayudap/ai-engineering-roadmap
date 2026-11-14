"""
LATIHAN LOOPING PYTHON (for & while)
====================================
Cara pakai:
    1. Isi setiap fungsi yang ada tulisan TODO.
    2. Jalankan:  python latihan_looping.py
    3. Target: semua test jadi OK.

Aturan latihan:
    - Jangan pakai slicing [::-1] untuk membalik string (latihan no. 6).
    - Jangan pakai sum(), max(), min() untuk no. 2 dan 8 (pakai loop manual).
    - Jangan pakai perpustakaan luar, cukup Python standar.

---------------------------------------------------------------------------
CHEATSHEET SINGKAT
---------------------------------------------------------------------------
for  -> dipakai kalau jumlah putarannya sudah diketahui
        (range, list, dict, string, file)

    for i in range(5):                 # 0,1,2,3,4
    for i in range(1, 6):              # 1,2,3,4,5
    for i in range(10, 0, -2):         # 10,8,6,4,2
    for i, huruf in enumerate("abc"):  # (0,'a') (1,'b') (2,'c')
    for a, b in zip([1, 2], "xy"):     # (1,'x') (2,'y')
    for kunci, nilai in dict.items():  # iterasi dictionary

while -> dipakai kalau jumlah putarannya belum diketahui
         (menunggu kondisi berubah, baca input, dsb)

    n = 100
    while n > 1:                       # Collatz
        n = n // 2 if n % 2 == 0 else 3 * n + 1

Kontrol alur:
    break      -> keluar dari loop sekarang juga
    continue   -> lewati sisa putaran ini, lanjut putaran berikutnya
    else       -> dijalankan hanya jika loop selesai tanpa break

Hati-hati infinite loop: pastikan variabel kondisi di dalam while
selalu berubah menuju kondisi berhenti.
"""


# ===========================================================================
# BAGIAN 1 - PEMANASAN
# ===========================================================================

def cetak_1_sampai_10():
    """No.1 - Kembalikan list berisi angka 1 sampai 10 (pakai for + range).

    Contoh: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    # TODO: tulis kode kamu di sini
    raise NotImplementedError


def jumlah_1_sampai_100():
    """No.2 - Jumlahkan 1 + 2 + ... + 100 dengan for loop.

    Hasil yang benar: 5050
    """
    # TODO: pakai variabel penampung (total = 0) lalu tambah di dalam loop
    raise NotImplementedError


# ===========================================================================
# BAGIAN 2 - WHILE LOOP
# ===========================================================================

def faktorial(n):
    """No.3 - Hitung n! memakai while loop.

    faktorial(5) -> 120   (5*4*3*2*1)
    faktorial(0) -> 1
    """
    # TODO: while n > 1: hasil *= n; n -= 1
    raise NotImplementedError


def balik_string(teks):
    """No.4 - Balik urutan string memakai while loop (TANPA [::-1]).

    balik_string("python") -> "nohtyp"
    Petunjuk: ambil karakter dari indeks terakhir, mundur sampai 0.
    """
    # TODO: hasil = ""; i = len(teks) - 1; while i >= 0: ...
    raise NotImplementedError


def jumlah_digit(angka):
    """No.5 - Jumlahkan semua digit sebuah bilangan bulat positif (while).

    jumlah_digit(1234) -> 10   (1+2+3+4)
    Petunjuk: digit terakhir = angka % 10, buang dengan angka //= 10.
    """
    # TODO
    raise NotImplementedError


def tebak_angka(rahasia, daftar_tebakan):
    """No.6 - Simulasi game tebak angka dengan while.

    Bandingkan tiap tebakan secara berurutan dengan `rahasia`.
    Kembalikan jumlah percobaan yang dipakai saat tebakan benar (1-based),
    atau None kalau semua tebakan habis dan tidak ada yang benar.

    tebak_angka(7, [1, 5, 7, 9]) -> 3
    tebak_angka(7, [1, 5, 9])    -> None
    """
    # TODO: gunakan indeks + while, bukan for
    raise NotImplementedError


def jumlah_sampai_nol(data):
    """No.7 - Jumlahkan isi list sampai bertemu angka 0 (sentinil).

    Angka 0 dan sisanya tidak ikut dijumlah.
    jumlah_sampai_nol([4, 6, 0, 100]) -> 10
    jumlah_sampai_nol([1, 2, 3])      -> 6      (tidak ada 0 -> semua dijumlah)
    """
    # TODO: while dengan sentinil, pakai break saat ketemu 0
    raise NotImplementedError


# ===========================================================================
# BAGIAN 3 - KOMBINASI FOR, BREAK, CONTINUE
# ===========================================================================

def fizzbuzz(n):
    """No.8 - FizzBuzz 1..n, kembalikan list of string.

    Kelipatan 3 -> "Fizz", kelipatan 5 -> "Buzz",
    kelipatan 3 dan 5 -> "FizzBuzz", selain itu string angkanya.

    fizzbuzz(5) -> ["1", "2", "Fizz", "4", "Buzz"]
    """
    # TODO: urutan cek penting -> cek 15 (3 dan 5) lebih dulu
    raise NotImplementedError


def is_prima(n):
    """No.9 - Tentukan bilangan prima memakai for + break/else (atau return).

    is_prima(7) -> True, is_prima(9) -> False, is_prima(1) -> False
    Petunjuk: cukup cek pembagi 2 sampai akar n (int(n ** 0.5)).
    """
    # TODO
    raise NotImplementedError


def huruf_vokal_unik(teks):
    """No.10 - Kumpulkan huruf vokal unik (a,i,u,e,o) dengan urutan kemunculan.

    huruf_vokal_unik("Belajar Python") -> ["e", "a", "o"]
    Petunjuk: continue kalau bukan vokal atau sudah pernah masuk hasil.
    """
    # TODO
    raise NotImplementedError


# ===========================================================================
# BAGIAN 4 - NESTED LOOP
# ===========================================================================

def tabel_perkalian(n):
    """No.11 - Tabel perkalian 1..n sebagai list of list.

    tabel_perkalian(3) -> [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    """
    # TODO: dua for bersarang
    raise NotImplementedError


def segitiga_bintang(n):
    """No.12 - Segitiga bintang rata kiri sebanyak n baris.

    segitiga_bintang(3) -> ["*", "**", "***"]
    """
    # TODO: boleh for bersarang, atau while + penggabungan string
    raise NotImplementedError


# ===========================================================================
# TEST OTOMATIS - jangan diubah, jalankan saja
# ===========================================================================

def _jalankan_test():
    kasus = [
        ("No.1  cetak_1_sampai_10()", cetak_1_sampai_10, (),
         list(range(1, 11))),
        ("No.2  jumlah_1_sampai_100()", jumlah_1_sampai_100, (), 5050),
        ("No.3  faktorial(5)", faktorial, (5,), 120),
        ("No.3  faktorial(0)", faktorial, (0,), 1),
        ("No.4  balik_string('python')", balik_string, ("python",), "nohtyp"),
        ("No.4  balik_string('a')", balik_string, ("a",), "a"),
        ("No.5  jumlah_digit(1234)", jumlah_digit, (1234,), 10),
        ("No.6  tebak_angka benar", tebak_angka, (7, [1, 5, 7, 9]), 3),
        ("No.6  tebak_angka habis", tebak_angka, (7, [1, 5, 9]), None),
        ("No.7  jumlah_sampai_nol", jumlah_sampai_nol, ([4, 6, 0, 100],), 10),
        ("No.8  fizzbuzz(5)", fizzbuzz, (5,),
         ["1", "2", "Fizz", "4", "Buzz"]),
        ("No.9  is_prima(7)", is_prima, (7,), True),
        ("No.9  is_prima(9)", is_prima, (9,), False),
        ("No.10 huruf_vokal_unik", huruf_vokal_unik, ("Belajar Python",),
         ["e", "a", "o"]),
        ("No.11 tabel_perkalian(3)", tabel_perkalian, (3,),
         [[1, 2, 3], [2, 4, 6], [3, 6, 9]]),
        ("No.12 segitiga_bintang(3)", segitiga_bintang, (3,),
         ["*", "**", "***"]),
    ]

    lulus = 0
    for label, fungsi, argumen, harapan in kasus:
        try:
            hasil = fungsi(*argumen)
        except NotImplementedError:
            print(f"  [  ]  {label:<32} belum diisi")
            continue
        except Exception as e:
            print(f"  [!!]  {label:<32} error: {type(e).__name__}: {e}")
            continue

        if hasil == harapan:
            lulus += 1
            print(f"  [OK]  {label:<32} -> {hasil!r}")
        else:
            print(f"  [XX]  {label:<32} -> {hasil!r}  (harusnya {harapan!r})")

    print(f"\nSkor: {lulus}/{len(kasus)} test lulus")
    if lulus == len(kasus):
        print("Semua latihan selesai. Lanjut ke file berikutnya!")
    else:
        print("Belum semua benar. Perbaiki bagian yang [XX] / [  ] di atas.")


if __name__ == "__main__":
    print("Latihan Looping Python - hasil test:\n")
    _jalankan_test()
