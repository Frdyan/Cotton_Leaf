import streamlit as st
from PIL import Image
from model import load_model, predict_image

# Konfigurasi halaman
st.set_page_config(
    page_title="Daun Kapas"
)

# Judul dan deskripsi aplikasi
st.title("Aplikasi Klasifikasi Penyakit Daun Kapas")
st.write('Muat gambar daun kapas untuk klasifikasi penyakitnya.')
st.sidebar.success("You're At Homepage Now")

# Load model
model = load_model()

# Upload gambar
uploaded_file = st.file_uploader("Pilih gambar daun kapas...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Tampilkan gambar yang diunggah
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar yang diunggah', use_column_width=True)
    
    # Tombol prediksi
    if st.button('Prediksi'):
        # Placeholder untuk proses prediksi
        st.write('Memproses...')
        
        # Prediksi
        label = predict_image(model, image)
        
        # Tampilkan hasil prediksi
        if label == 0:
            st.write("Klasifikasi: Bacterial Blight")
        elif label == 1:
            st.write("Klasifikasi: Curl Virus")
        elif label == 2:
            st.write("Klasifikasi: Fusarium Wilt")
        elif label == 3:
            st.write("Klasifikasi: Healthy")
