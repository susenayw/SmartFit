import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Setup Halaman & Judul
st.set_page_config(page_title="SmartFit AI Dashboard", layout="wide")
st.title("🏃‍♂️ SmartFit: Re-kalibrasi BMI & Aktivitas")

# 2. Load Master Dataset
@st.cache_data
def load_data():
    return pd.read_csv('master_smartfit_final.csv')

df = load_data()

# 3. Sidebar: Input User (Interaktif)
st.sidebar.header("Input Data Fisik Baru")
gender = st.sidebar.selectbox("Gender", ["Pria", "Wanita"])
weight = st.sidebar.number_input("Berat Badan (kg)", min_value=30.0, max_value=200.0, value=70.0)
height = st.sidebar.number_input("Tinggi Badan (cm)", min_value=100.0, max_value=250.0, value=170.0)

# 4. Logika Kalkulasi Real-time
height_m = height / 100
bmi = round(weight / (height_m ** 2), 2)

st.subheader(f"Status BMI Anda Saat Ini: {bmi}")

# Menentukan Kategori
if bmi < 18.5:
    status = "Underweight"
    color = "blue"
elif 18.5 <= bmi < 25:
    status = "Normal"
    color = "green"
else:
    status = "Overweight/Obese"
    color = "red"

st.markdown(f"Status: <b style='color:{color}'>{status}</b>", unsafe_allow_html=True)

# 5. Dashboard Visualisasi
col1, col2 = st.columns(2)

with col1:
    st.write("### Sebaran User dalam Master Data")
    # Grafik Sebaran BMI vs Steps dari master_smartfit_final.csv
    fig = px.scatter(df, x='bmi', y='TotalSteps', color='Recommendation_Label',
                     title="Hubungan BMI vs Aktivitas (Data Historis)")
    # Tambahkan posisi user saat ini ke grafik
    fig.add_scatter(x=[bmi], y=[5000], mode='markers', name='Posisi Anda',
                    marker=dict(size=15, color='black', symbol='star'))
    st.plotly_chart(fig)

with col2:
    st.write("### Rekomendasi Re-kalibrasi")
    if status == "Overweight/Obese":
        st.warning("⚠️ Target: Turunkan BMI ke 24.9")
        st.info("💡 Rekomendasi: Minimal 10.000 langkah per hari & Defisit Kalori 500 kkal.")
    elif status == "Normal":
        st.success("✅ Pertahankan gaya hidup aktif Anda!")
        st.info("💡 Rekomendasi: 7.000 - 10.000 langkah per hari.")
    else:
        st.write("Fokus pada peningkatan massa otot dan asupan protein.")

# 6. Integrasi Dataset Nutrisi (Opsional)
st.write("---")
st.write("### 🥗 Saran Makanan Berdasarkan Preferensi")
st.caption("Data diambil dari library abbrev_cleaned.csv")
# Di sini kamu bisa menambahkan filter otomatis makanan favorit user