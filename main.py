import requests
from ultralytics import YOLO
import os

# --- 1. 配置區 ---
BOT_TOKEN = "8685953963:AAHHOHWMP2OMxzTFnOk_8OmiqChuXMfgXP8"
CHAT_ID = "1441936253" 
MODEL_PATH = "weights/best.pt"
PHOTO_PATH = "test_data/PPE_test_image.jpg"

def send_alert(message, image_path=None):
    try:
        text_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(text_url, json={"chat_id": CHAT_ID, "text": message})
        if image_path and os.path.exists(image_path):
            img_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
            with open(image_path, "rb") as photo:
                requests.post(img_url, data={"chat_id": CHAT_ID}, files={"photo": photo})
    except Exception as e:
        print(f"發送失敗: {e}")

# --- 2. 執行偵測 ---
model = YOLO(MODEL_PATH)


# 提高準確度：加入 augment=True 並稍微提升解析度
results = model.predict(
    source=PHOTO_PATH, 
    conf=0.5, 
    augment=True, 
    device="mps",
    show=True,     # This opens the image window
    save=True      # This saves the predicted image to a folder
)

alert_sent_helmet = False 
alert_sent_gloves = False 

print("🚀 監控系統啟動：正在掃描安全帽與手套佩戴情況...")

for result in results:
    classes = result.boxes.cls.tolist()
    
    # --- 檢查沒戴安全帽 (ID 7) ---
    if 7 in classes and not alert_sent_helmet:
        print("⚠️ 偵測到未佩戴安全帽！")
        alert_img = "violation_helmet.jpg"
        result.save(filename=alert_img)
        send_alert("🚨 [PPE 警報] 發現人員未佩戴【安全帽】！", alert_img)
        alert_sent_helmet = True 

    # --- 檢查沒戴手套 (ID 5) ---
    if 5 in classes and not alert_sent_gloves:
        print("⚠️ 偵測到未佩戴手套！")
        alert_img = "violation_gloves.jpg"
        result.save(filename=alert_img)
        send_alert("🚨 [PPE 警報] 發現人員未佩戴【工作手套】！", alert_img)
        alert_sent_gloves = True 

    # 如果兩者都發過通知了，可以選擇提早結束或繼續跑完影片
    if alert_sent_helmet and alert_sent_gloves:
        print("✅ 所有類型違規已偵測並通知完畢。")
        # break # 如果只想各傳一次就停止，可以取消這行註釋

print("分析結束。")
