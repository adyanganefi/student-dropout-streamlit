import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model, scaler, dan label encoder
model = joblib.load('model/random_forest_model.pkl')
scaler = joblib.load('model/scaler.pkl')
label_encoder = joblib.load('model/label_encoder_status.pkl')

# Mapping nama fitur ke indeks (sesuai urutan saat training model)
feature_index = {
    'Curricular_units_2nd_sem_approved': 22,
    'Curricular_units_2nd_sem_grade': 25,
    'Curricular_units_1st_sem_approved': 12,
    'Curricular_units_1st_sem_grade': 15,
    'Admission_grade': 8,
    'Previous_qualification_grade': 6
}

# Ambil nama kolom dari scaler
try:
    columns = scaler.feature_names_in_
except AttributeError:
    # Jika scaler tidak menyimpan nama kolom, kita buat manual
    columns = [f'feature_{i}' for i in range(36)]

# UI Streamlit
st.title("Prediksi Risiko Dropout Mahasiswa")
st.markdown("Masukkan data mahasiswa untuk memprediksi status akhir (Dropout, Enrolled, Graduate)")

# Input dari pengguna
input_data = {}
input_data['Curricular_units_2nd_sem_approved'] = st.number_input("Jumlah mata kuliah semester 2 yang lulus", min_value=0, max_value=20, value=5)
input_data['Curricular_units_2nd_sem_grade'] = st.number_input("Rata-rata nilai semester 2", min_value=0.0, max_value=20.0, value=12.0)
input_data['Curricular_units_1st_sem_approved'] = st.number_input("Jumlah mata kuliah semester 1 yang lulus", min_value=0, max_value=20, value=6)
input_data['Curricular_units_1st_sem_grade'] = st.number_input("Rata-rata nilai semester 1", min_value=0.0, max_value=20.0, value=13.0)
input_data['Admission_grade'] = st.number_input("Nilai masuk institusi", min_value=0.0, max_value=200.0, value=140.0)
input_data['Previous_qualification_grade'] = st.number_input("Nilai kualifikasi sebelumnya", min_value=0.0, max_value=200.0, value=150.0)

# Saat tombol ditekan
if st.button("Prediksi"):
    full_feature_array = np.zeros(36)

    # Isi fitur utama sesuai indeks
    for name, value in input_data.items():
        idx = feature_index[name]
        full_feature_array[idx] = value

    input_df = pd.DataFrame([full_feature_array], columns=columns)

    # Transformasi scaling
    fitur_scaled = scaler.transform(input_df)

    # Prediksi
    pred = model.predict(fitur_scaled)
    pred_label = label_encoder.inverse_transform(pred)[0]

    # Output
    st.success(f"**Prediksi Status Mahasiswa:** {pred_label}")
