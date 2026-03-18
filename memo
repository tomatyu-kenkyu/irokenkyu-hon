import streamlit as st
from PIL import Image

st.title("画像の色割合分析")

# 画像アップロード
uploaded_file = st.file_uploader("画像をアップロードしてください", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # 画像を開く
    img = Image.open(uploaded_file)
    st.image(img, caption="アップロードされた画像", use_column_width=True)

    # ピクセル取得
    pixels = img.getdata()
    total_pixels = len(pixels)

    color_count = {}

    # 色ごとのカウント
    for pixel in pixels:
        color_count[pixel] = color_count.get(pixel, 0) + 1

    st.subheader("色ごとの割合")

    # 表示
    for color, count in color_count.items():
        ratio = count / total_pixels * 100
        st.write(f"{color}: {count} ピクセル ({ratio:.2f}%)")