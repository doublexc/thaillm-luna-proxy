#uv run --with fastapi --with uvicorn --with requests --with python-dotenv python thaillm_proxy.py
from fastapi import FastAPI, Request
import requests
import uvicorn
import os
from dotenv import load_dotenv # เพิ่มบรรทัดนี้

app = FastAPI()

@app.post("/v1/chat/completions")
async def proxy_translate(request: Request):
    luna_data = await request.json()
    
    # 1. ลองใช้ URL แบบ New แต่ระบุ IP หรือ Host ให้ชัดเจน (ลองใช้ http ตามตัวอย่างเขาก่อน)
    url = "http://thaillm.or.th/api/v1/chat/completions"
    
    # 2. Key จากภาพของคุณ (เช็คตัวอักษรให้ดีว่าก๊อปมาครบไหม)
    load_dotenv() # เพิ่มบรรทัดนี้เพื่อให้อ่านไฟล์ .env
    api_key = os.getenv("THAILLM_API_KEY", "YOUR_API_KEY_HERE")
    
    headers = {
        "Content-Type": "application/json",
        "apikey": api_key  # ใช้ตัวเล็กทั้งหมดตามตัวอย่าง curl ในภาพ
    }

    try:
        # ตัดพารามิเตอร์ที่ไม่จำเป็นออกก่อน เผื่อ Luna ส่งอะไรที่เขาไม่รองรับไป
        payload = {
            "model": "thalle-0.2-thaillm-8b-fa",
            "messages": luna_data.get("messages", []),
            "temperature": luna_data.get("temperature", 0.3),
            "max_tokens": 2048
        }

        response = requests.post(url, json=payload, headers=headers, timeout=30)
        
        print(f"\n--- Debug Log ---")
        print(f"Sending to: {url}")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            res_json = response.json()
            content = res_json['choices'][0]['message']['content']
            print(f"Success! Translation: {content}")
            return res_json
        else:
            print(f"Error Content: {response.text}")
            return response.json()

    except Exception as e:
        print(f"Proxy Error: {str(e)}")
        return {"error": str(e)}

if __name__ == "__main__":
    print("--- ThaiLLM Proxy is Ready ---")
    uvicorn.run(app, host="127.0.0.1", port=8000)