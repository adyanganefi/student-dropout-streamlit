import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Setup halaman
st.set_page_config(page_title="Dashboard Kinerja Mahasiswa", layout="centered")
st.title("🎓 Dashboard Kinerja Mahasiswa")
st.write("Visualisasi interaktif untuk memonitor performa mahasiswa Jaya Jaya Institut.")

# Path ke file CSV
base_dir = os.path.dirname(__file__)
data_path = os.path.join(base_dir, "students_performance.csv")

# Load data
df = pd.read_csv(data_path, sep=";")

# Filter Sidebar
st.sidebar.header("🔍 Filter")
status_options = st.sidebar.multiselect("Status Mahasiswa", options=df['Status'].unique(), default=df['Status'].unique())
gender_options = st.sidebar.multiselect("Jenis Kelamin", options=df['Gender'].unique(), default=df['Gender'].unique())
df_filtered = df[(df['Status'].isin(status_options)) & (df['Gender'].isin(gender_options))]

# Visualisasi 1: Ringkasan
st.subheader("📊 Ringkasan Data")
col1, col2, col3 = st.columns(3)
col1.metric("Total Mahasiswa", len(df_filtered))
col2.metric("Rata-rata Nilai Masuk", round(df_filtered['Admission_grade'].mean(), 2))
col3.metric("Rata-rata Lulus Semester 1", round(df_filtered['Curricular_units_1st_sem_approved'].mean(), 1))

# Visualisasi 2 & 3: Bar Chart Status & Beasiswa
st.subheader("🎯 Status & Beasiswa Mahasiswa")
colA, colB = st.columns(2)

with colA:
    fig1, ax1 = plt.subplots(figsize=(5, 4))
    sns.countplot(data=df_filtered, x='Status', palette='Set2', order=df_filtered['Status'].value_counts().index, ax=ax1)
    ax1.set_ylabel("Jumlah")
    ax1.set_title("Distribusi Status Mahasiswa")
    st.pyplot(fig1)

with colB:
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    sns.countplot(data=df_filtered, x='Scholarship_holder', hue='Status', palette='pastel', ax=ax2)
    ax2.set_xticklabels(['Tidak', 'Ya'])
    ax2.set_title("Beasiswa vs Status")
    st.pyplot(fig2)

# Visualisasi 4 & 5: UKT & Nilai Masuk
st.subheader("💰 UKT & Nilai Masuk")
colC, colD = st.columns(2)

with colC:
    fig3, ax3 = plt.subplots(figsize=(5, 4))
    sns.countplot(data=df_filtered, x='Tuition_fees_up_to_date', hue='Status', palette='muted', ax=ax3)
    ax3.set_xticklabels(['Menunggak', 'Lunas'])
    ax3.set_title("UKT vs Status")
    st.pyplot(fig3)

with colD:
    fig4, ax4 = plt.subplots(figsize=(5, 4))
    sns.boxplot(data=df_filtered, x='Status', y='Admission_grade', palette='Set3', ax=ax4)
    ax4.set_title("Distribusi Nilai Masuk")
    st.pyplot(fig4)

# Footer
st.markdown("---")
st.caption("© 2025 Jaya Jaya Institut | Dicoding Data Science Academy Submission")
