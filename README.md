# MANHAJ BOOKS (كتب المنهج)

## Proyek E-Commerce - Tugas 2 PBP


## 1.)Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step 
### 1. Membuat Proyek Baru
* **Membuat folder baru bernama manhaj-books**
* **Menginisialisasi Git didalam manhaj-books**
* **membuat repository baru di Github dengan nama manhaj-books**
* **Membuka folder manhaj-books dengan VScode**
* **Membuat env python(dengan command: python -m venv env)**
* **Mengaktifkan env(dengan command: env\Scripts\activate)**
* **Membuat txt file bernama requirements.txt**
* **menginstall segala yang terdapat pada requirements.txt**
* **Membuat proyek Django manhaj_books yang menjadi sebuah folder**
* **mengedir ALLOWED_HOSTS**
* **Membuat .gitignore melalui VScode**
* **melakukan add, commit, push pada github**


### 2. Membuat aplikasi main pada proyek

* **Melakukan startapp main untuk membuat aplikasi dengan arsitektur django bernama main**

### 3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main

* **Memasukkan main pada settings.py tepatnya pada INSTALLED_APPS**

### 4. Membuat models

* **Membuat folder baru bernama templates**
* **membuat file templates\main.html dan mulai berkarya dengan visual**
* **Membuat class Product pada models.py yang berisi atribut nama, price, description**

### 5. Membuat Function pada views.py

* **Memberi nama function show_main dengan parameter request**
* **Membuat List of Dictionary didalam function dengan nama products yang berisi nama, harga, dan deskripsi barang**
* **Membuat Dictionary bernama context untuk menyimpan beberapa variabel untuk  dipakai pada html**

### 6. Membuat sebuah routing pada urls.py aplikasi main

* **Mengisi urlpatterns dengan nama function yang terdapat pada views.py**

### 7. Melakukan deployment ke PWS

* **add remote PWS**
* **Check the branch, use master branch**
* **lalu push ke PWS dan masukkan username dan password**

### 8. Membuat README.md file ini

## 2.) bagan yang berisi request client ke web aplikasi berbasis Django
![image about client](image.png)

## 3.) Jelaskan fungsi git dalam pengembangan perangkat lunak!

* **Bisa menjadi pelacak perubahan kode sehingga ketika berkolaborasi dengan tim masing-masing dari mereka dapat melacak perubahan kode, dan juga membuat perangkat lunak seakan-akan memiliki versi-versi pada setiap commitnya**
## 4.) Mengapa Memilih Django sebagai Framework Pembelajaran?

Django merupakan pilihan yang populer untuk memulai pembelajaran pengembangan web karena beberapa alasan berikut:

* **Konvensi lebih baik daripada konfigurasi:** Django menyediakan struktur yang jelas dan konsisten, sehingga pengembang dapat fokus pada logika bisnis.
* **Komunitas yang besar:** Django memiliki komunitas pengguna yang sangat aktif, sehingga mudah menemukan dokumentasi, tutorial, dan bantuan jika diperlukan.
* **Fitur lengkap:** Django menyediakan berbagai fitur bawaan, seperti ORM, form handling, dan admin interface, yang sangat berguna untuk membangun aplikasi web yang kompleks.
* **Python:** Django menggunakan bahasa pemrograman Python yang dikenal mudah dipelajari dan memiliki sintaks yang bersih.

## 5.) Mengapa model pada Django disebut sebagai ORM?

### Sesuai dengan namanya yaitu ORM(--Object-Relational Mapper--)
* **Object :** Model-model dalam Django adalah objek Python. Mereka memiliki atribut (fields) yang merepresentasikan kolom dalam tabel database, dan metode-metode untuk melakukan operasi pada data.
* **Relational :** Database relasional menggunakan tabel untuk menyimpan data, dengan hubungan antar tabel (relasi). ORM Django memetakan hubungan-hubungan ini menjadi hubungan antara model-model Python.
* **Mapper** ORM bertindak sebagai "pemeta" yang menerjemahkan antara representasi objek dalam Python dan representasi relasional dalam database.

Dinamai ORM sebab ORM memungkinkan kita berinteraksi dengan database menggunakan sintaks Python yang lebih intuitif, tanpa harus menulis query SQL secara langsung. Kita bisa membuat, membaca, memperbarui, dan menghapus data dalam database seolah-olah kita sedang berinteraksi dengan objek Python.

