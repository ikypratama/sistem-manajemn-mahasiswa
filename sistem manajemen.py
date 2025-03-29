# Sistem Manajemen Data Mahasiswa

# Mendefinisikan dictionary untuk menyimpan data mahasiswa
mahasiswa_data = {}

# Fungsi untuk menambahkan data mahasiswa
def tambah_mahasiswa(nama, nim, jurusan, tugas, uts, uas):
    mahasiswa_data[nim] = {
        'nama': nama,
        'jurusan': jurusan,
        'tugas': tugas,
        'uts': uts,
        'uas': uas
    }
    print(f"Data mahasiswa {nama} berhasil ditambahkan.")

# Fungsi untuk menghapus data mahasiswa
def hapus_mahasiswa(nim):
    if nim in mahasiswa_data:
        del mahasiswa_data[nim]
        print(f"Data mahasiswa dengan NIM {nim} berhasil dihapus.")
    else:
        print(f"Data mahasiswa dengan NIM {nim} tidak ditemukan.")

# Fungsi untuk menampilkan data mahasiswa
def tampilkan_mahasiswa():
    for nim, data in mahasiswa_data.items():
        print(f"NIM: {nim}, Nama: {data['nama']}, Jurusan: {data['jurusan']}")

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(nim):
    if nim in mahasiswa_data:
        tugas = mahasiswa_data[nim]['tugas']
        uts = mahasiswa_data[nim]['uts']
        uas = mahasiswa_data[nim]['uas']
        nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)
        return nilai_akhir
    else:
        return None

# Fungsi untuk mengecek status kelulusan
def status_kelulusan(nim):
    nilai_akhir = hitung_nilai_akhir(nim)
    if nilai_akhir is not None:
        if nilai_akhir >= 60:
            print(f"Mahasiswa dengan NIM {nim} dinyatakan LULUS.")
        else:
            print(f"Mahasiswa dengan NIM {nim} dinyatakan TIDAK LULUS.")
    else:
        print(f"Data mahasiswa dengan NIM {nim} tidak ditemukan.")

# Contoh penggunaan
tambah_mahasiswa("Rizki Pratama Putra", "12345", "Teknik Informatika", 80, 70, 90)
tampilkan_mahasiswa()
status_kelulusan("12345")
hapus_mahasiswa("12345")
tampilkan_mahasiswa()