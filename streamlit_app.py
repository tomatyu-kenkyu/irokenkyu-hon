import streamlit as st
from google import genai
from PIL import Image
import time

st.title("Gemini OCR")

api_key = st.text_input("Google AI APIキー", type="password")

uploaded_file = st.file_uploader(
    "画像をアップロード",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file and api_key:

    image = Image.open(uploaded_file)

    st.image(image, caption="アップロード画像", use_container_width=True)

    if st.button("OCR実行"):

        try:
            client = genai.Client(api_key=api_key)

            # リトライ処理
            max_retry = 3

            for i in range(max_retry):

                try:
                    response = client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=[
                            image,
                            "画像内の文字をすべてOCRしてください。"
                        ]
                    )

                    st.subheader("OCR結果")
                    st.write(response.text)
                    break

                except Exception as e:

                    # 503時は再試行
                    if "503" in str(e):

                        if i < max_retry - 1:
                            st.warning(f"混雑中です。再試行 {i+1}/{max_retry}")
                            time.sleep(3)
                        else:
                            st.error("Geminiサーバーが混雑しています。時間を空けてください。")

                    else:
                        st.error(f"エラー: {e}")
                        break

        except Exception as e:
            st.error(f"エラー: {e}")