import streamlit as st
from google import genai
from PIL import Image

st.title("Gemini OCR")

# APIキー
api_key = st.text_input("Google AI APIキー", type="password")

# 画像アップロード
uploaded_file = st.file_uploader(
    "画像をアップロード",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file and api_key:

    # 画像表示
    image = Image.open(uploaded_file)
    st.image(image, caption="アップロード画像", use_container_width=True)

    if st.button("OCR実行"):

        try:
            # Geminiクライアント
            client = genai.Client(api_key=api_key)

            # OCR実行
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    image,
                    "この画像内の文字をすべて抽出してください。"
                ]
            )

            # 結果表示
            st.subheader("OCR結果")
            st.write(response.text)

        except Exception as e:
            st.error(f"エラー: {e}")