# Proyek Akhir: Memprediksi Risiko Dropout Mahasiswa Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut adalah institusi pendidikan tinggi yang sedang menghadapi tantangan signifikan terkait angka dropout mahasiswa. Tingginya jumlah mahasiswa yang keluar sebelum menyelesaikan studinya menyebabkan kerugian bagi institusi, baik dari segi keuangan, reputasi, maupun efektivitas pengelolaan sumber daya.

Untuk itu, institusi membutuhkan solusi berbasis data guna mengidentifikasi mahasiswa yang berisiko tinggi dropout sedini mungkin. Dengan adanya sistem prediktif, institusi dapat mengambil tindakan intervensi lebih awal seperti memberikan bimbingan akademik, konseling, atau program remedial.

### Permasalahan Bisnis

- Tingginya angka mahasiswa yang dropout menyebabkan kerugian pada institusi.
- Tidak adanya sistem atau metode yang dapat mengidentifikasi mahasiswa yang berisiko tinggi untuk dropout secara otomatis.
- Intervensi terhadap mahasiswa bermasalah sering dilakukan terlambat karena tidak ada peringatan dini berbasis data.

### Cakupan Proyek

- Membangun model machine learning untuk memprediksi risiko dropout mahasiswa berdasarkan data historis akademik dan demografis.
- Menyiapkan dashboard interaktif untuk memahami pola data dan memantau faktor penting yang memengaruhi performa mahasiswa.
- Menyediakan prototype sistem prediksi berbasis data yang bisa digunakan sebagai alat bantu pengambilan keputusan.

### Persiapan

**Sumber data:**  
Dataset diperoleh dari:  
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

**Setup environment:**
```python
# Import library yang dibutuhkan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

import joblib
```

## Business Dashboard

Dashboard yang dibuat menyajikan informasi penting untuk membantu tim akademik memantau performa mahasiswa. Visualisasi mencakup distribusi status akhir mahasiswa, pengaruh beasiswa, keterlambatan pembayaran UKT, serta distribusi nilai akademik.

Dashboard ini tidak hanya menampilkan tabel, tetapi juga berbagai grafik interaktif yang mudah dipahami untuk mengidentifikasi potensi risiko dropout sejak dini.

**Cara menjalankan dashboard Streamlit:**

1. Pastikan Anda sudah berada di dalam virtual environment (`venv`)  
2. Install dependencies dari `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan dashboard dengan perintah berikut dari root proyek:
   ```bash
   streamlit run dashboard/app.py
   ```
4. Akses dashboard di http://localhost:8501/

5. File `students_performance.csv` harus berada di root folder proyek (satu level di atas folder `dashboard/`).

---

## Menjalankan Sistem Machine Learning

Sistem machine learning menggunakan algoritma **Random Forest Classifier** yang telah dilatih menggunakan 36 fitur akademik mahasiswa. Dari hasil analisis Feature Importance, dipilih **6 fitur paling berpengaruh** yang digunakan untuk prediksi pada aplikasi.

Model dan proses preprocessing (scaler dan label encoder) telah disimpan dalam bentuk `.pkl` untuk digunakan.

Prediksi dapat dilakukan melalui **aplikasi Streamlit interaktif** pada file `prototype/streamlit_app.py`.

### Fitur yang digunakan untuk prediksi:
- Curricular_units_2nd_sem_approved  
- Curricular_units_2nd_sem_grade  
- Curricular_units_1st_sem_approved  
- Curricular_units_1st_sem_grade  
- Admission_grade  
- Previous_qualification_grade  

**Cara menjalankan aplikasi prediksi (prototype):**

1. Pastikan Anda sudah berada di dalam virtual environment (`venv`)  
2. Install dependencies dari `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan aplikasi dengan perintah berikut dari root proyek:
   ```bash
   streamlit run prototype/app.py
   ```
4. Akses di http://localhost:8501/

5. Masukkan data mahasiswa melalui form.

6. Sistem akan memberikan hasil prediksi status akhir:
   - Dropout
   - Enrolled
   - Graduate

### Menjalankan Aplikasi di Cloud

Aplikasi prediksi ini juga telah dideploy ke **Streamlit Community Cloud** dan dapat diakses secara online melalui link berikut:

👉 [Akses Prototype di Streamlit Cloud](https://student-dropout-app-8te672oahjewzmv2mbrvjq.streamlit.app/)

---

## Conclusion

Berdasarkan proses eksplorasi, pemodelan, dan evaluasi terhadap dataset mahasiswa **Jaya Jaya Institut**, diperoleh beberapa kesimpulan utama sebagai berikut:

1. **Model yang digunakan**  
   Algoritma **Random Forest Classifier** dipilih karena kemampuannya menangani klasifikasi multikelas, ketahanannya terhadap outlier, serta memberikan interpretabilitas melalui *feature importance*.

2. **Performa model**  
   Model mencapai **akurasi sebesar 76.38%** pada data uji. Ia memberikan performa prediksi terbaik untuk kelas **Graduate**, cukup baik untuk **Dropout**, namun masih kurang dalam membedakan kelas **Enrolled**, kemungkinan karena distribusi data yang tidak seimbang.

3. **Distribusi kelas target**  
   - Graduate: 50%  
   - Dropout: 32%  
   - Enrolled: 18%  
   ➤ Ketidakseimbangan ini dapat menyebabkan bias prediksi terhadap kelas mayoritas (Graduate), dan kesulitan dalam klasifikasi kelas minoritas (Enrolled).

4. **Fitur yang paling berpengaruh terhadap prediksi status akhir mahasiswa**:  
   - `Curricular_units_2nd_sem_approved`  
   - `Curricular_units_2nd_sem_grade`  
   - `Curricular_units_1st_sem_approved`  
   ➤ Ini menunjukkan bahwa **performa akademik pada semester awal** sangat menentukan keberhasilan studi mahasiswa. Mahasiswa dengan jumlah mata kuliah yang tidak lulus banyak dan nilai yang rendah di semester awal cenderung memiliki risiko lebih tinggi untuk dropout.

5. **Karakteristik umum mahasiswa yang dropout**:  
   - Rata-rata **nilai semester rendah**, baik dari segi jumlah mata kuliah yang tidak lulus maupun nilai keseluruhan.  
   - Banyak dari mereka juga **tidak memperoleh beasiswa** dan **memiliki keterlambatan pembayaran UKT**.  
   - **Marital status** dan usia juga berpengaruh, di mana mahasiswa yang sudah menikah atau berusia lebih tua cenderung lebih berisiko mengalami dropout karena mungkin menghadapi beban tanggung jawab keluarga atau pekerjaan.

---

### Rekomendasi Actionable Items

Berdasarkan temuan tersebut, berikut adalah rekomendasi yang lebih teknis dan actionable untuk pihak akademik Jaya Jaya Institut:

1. **Sistem Early Warning**  
   - Terapkan *early warning system* berbasis model prediksi ini untuk mendeteksi mahasiswa dengan performa rendah sejak semester pertama dan kedua.  
   - Sistem ini bisa diintegrasikan dalam sistem informasi akademik kampus.

2. **Dukungan Akademik Spesifik**  
   - Mahasiswa dengan jumlah mata kuliah yang tidak lulus banyak di semester awal dapat diberikan *remedial class* atau *mentoring akademik*.  
   - Libatkan dosen wali untuk mengawasi perkembangan nilai mereka.

3. **Pendekatan Finansial dan Sosial**  
   - Bagi mahasiswa yang terlambat membayar UKT atau tidak mendapat beasiswa, perlu dibuat skema keringanan pembayaran, cicilan UKT, atau informasi lebih terbuka mengenai beasiswa.  
   - Mahasiswa menikah dapat difasilitasi fleksibilitas jam belajar atau pendampingan psikologis agar tetap dapat mengikuti perkuliahan dengan baik.

4. **Model Iteratif dan Berbasis Data Terbaru**  
   - Update model secara berkala menggunakan data akademik terbaru agar sistem tetap relevan dan akurat.  
   - Lakukan eksplorasi dengan model alternatif seperti XGBoost untuk kemungkinan peningkatan performa prediksi.

5. **Visualisasi Interaktif**  
   - Dashboard berbasis **Streamlit** telah dikembangkan dan dapat digunakan dosen untuk memantau status mahasiswa. Ke depan bisa dikembangkan lebih lanjut menjadi sistem prediktif berbasis web kampus.
