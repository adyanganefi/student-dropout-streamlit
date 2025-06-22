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

Model ini dapat dikembangkan lebih lanjut menjadi API atau diintegrasikan ke dalam sistem informasi akademik.

---

## Conclusion

Berdasarkan hasil eksplorasi, pemodelan, dan evaluasi terhadap dataset mahasiswa Jaya Jaya Institut, diperoleh beberapa kesimpulan utama sebagai berikut:

1. **Model yang digunakan**  
   Algoritma **Random Forest Classifier** dipilih karena mampu menangani klasifikasi multikelas, robust terhadap outlier, dan memberikan interpretasi melalui feature importance.

2. **Performa model**  
   Model menunjukkan **akurasi sebesar 76.38%** pada data uji, dengan performa terbaik dalam memprediksi mahasiswa yang **Graduate**, namun masih kurang dalam membedakan kelas **Enrolled**.

3. **Distribusi kelas**  
   - Graduate: 50%  
   - Dropout: 32%  
   - Enrolled: 18%  
   ➤ Distribusi ini cukup timpang, yang mungkin memengaruhi kinerja prediksi terutama pada kelas Enrolled yang minoritas.

4. **Fitur yang paling berpengaruh**  
   Berdasarkan *feature importance*, tiga fitur paling menentukan status akhir mahasiswa adalah:
   - `Curricular_units_2nd_sem_approved`
   - `Curricular_units_2nd_sem_grade`
   - `Curricular_units_1st_sem_approved`  
   ➤ Ini menekankan pentingnya performa akademik sejak awal perkuliahan sebagai indikator risiko dropout.

---

### Rekomendasi Action Items

Berikut adalah beberapa rekomendasi strategis bagi Jaya Jaya Institut:

- **Bangun sistem peringatan dini (early warning system)** berdasarkan model ini, untuk mengidentifikasi mahasiswa yang berisiko dropout sejak semester awal.
- **Lakukan balancing data atau oversampling** pada kelas minoritas (Enrolled) untuk meningkatkan akurasi model secara menyeluruh.
- **Evaluasi dan uji model alternatif** seperti XGBoost atau Gradient Boosting untuk membandingkan performa prediksi.
- **Kembangkan dashboard interaktif** berbasis Streamlit atau BI tools agar dosen wali dan manajemen dapat menggunakan model ini secara real time.
- **Berikan dukungan akademik atau mentoring** secara khusus kepada mahasiswa dengan risiko tinggi menurut model prediksi.
