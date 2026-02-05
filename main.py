import requests
import os

def check():
    # 從 GitHub Secrets 讀取金鑰
    token = os.environ.get('TG_TOKEN')
    chat_id = os.environ.get('TG_CHAT_ID')
    
    # 這是目前的測試訊息
    msg = "🚀 監理站監控雲端測試：成功！\n目前設定：台中市/普通重機/2月12日後。"
    
    # 發送 Telegram 訊息
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    res = requests.get(url)
    
    if res.status_code == 200:
        print("Telegram 訊息發送成功！")
    else:
        print(f"發送失敗，原因：{res.text}")

if _name_ == "_main_":
    check()
