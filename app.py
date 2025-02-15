import streamlit as st
import cv2
import numpy as np
import easyocr

st.title("Text Detection UI dengan Streamlit")
st.write("Unggah gambar untuk mendeteksi teks di dalamnya.")

# Widget untuk mengunggah file gambar
uploaded_file = st.file_uploader("Pilih file gambar", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file is not None:
    # Membaca file gambar dari streamlit
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    if image is None:
        st.error("Gagal membaca gambar!")
    else:
        # Inisialisasi EasyOCR Reader
        reader = easyocr.Reader(['en'], gpu=False)
        results = reader.readtext(image)
        
        threshold = 0.25  # Ambang skor
        
        # Proses hasil deteksi teks
        for bbox, text, score in results:
            if score > threshold:
                # Konversi koordinat ke integer
                pt1 = (int(bbox[0][0]), int(bbox[0][1]))
                pt2 = (int(bbox[2][0]), int(bbox[2][1]))
                # Gambar rectangle pada area teks
                cv2.rectangle(image, pt1, pt2, (0, 255, 0), 2)
                # Tambahkan teks hasil pendeteksian
                cv2.putText(image, text, pt1, cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
        
        # Konversi BGR ke RGB agar warnanya tampil benar di Streamlit
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        st.image(image_rgb, caption="Hasil Deteksi Teks", use_container_width=True)
