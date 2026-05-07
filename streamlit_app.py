import streamlit as st
from google import genai

# タイトル
st.title("Gemini AI テスト")

# APIキー入力
api_key = st.text_input("Google AI APIキーを入力", type="password")

# 質問入力
prompt = st.text_area(
    "質問を入力してください",
    "Explain how AI works in a few words"
)

# 実行ボタン
if st.button("送信"):
    if not api_key:
        st.warning("APIキーを入力してください")
    else:
        try:
            # クライアント作成
            client = genai.Client(api_key=api_key)

            # Geminiへ送信
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt,
            )

            # 結果表示
            st.subheader("AIの回答")
            st.write(response.text)

        except Exception as e:
            st.error(f"エラー: {e}")