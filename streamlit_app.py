import streamlit as st
import urllib.request
import urllib.parse
import hashlib
def generate_screenshot_api_url(customer_key, secret_phrase, options):
   api_url = 'https://api.screenshotmachine.com/?key=' + customer_key
   if secret_phrase:
       api_url += '&hash=' + hashlib.md5(
           (options.get('url') + secret_phrase).encode('utf-8')
       ).hexdigest()
   api_url += '&' + urllib.parse.urlencode(options)
   return api_url

st.title("Screenshot Machine Viewer")
# 入力欄
customer_key = st.text_input("Customer Key")
secret_phrase = st.text_input("Secret Phrase（任意）", value="")
target_url = st.text_input("スクリーンショットURL", value="https://www.google.com")
if st.button("スクリーンショット取得"):
   options = {
       'url': target_url,
       'dimension': '1366x768',
       'device': 'desktop',
       'cacheLimit': '0',
       'delay': '200',
       'zoom': '100'
   }
   api_url = generate_screenshot_api_url(customer_key, secret_phrase, options)
   # 画像表示
   st.image(api_url, caption="取得したスクリーンショット")
   # 保存処理
   output = 'output.png'
   opener = urllib.request.build_opener()
   opener.addheaders = [('User-agent', '-')]
   urllib.request.install_opener(opener)
   urllib.request.urlretrieve(api_url, output)
   st.success(f"Screenshot saved as {output}")