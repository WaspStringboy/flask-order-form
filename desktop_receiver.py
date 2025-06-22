from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "我的訂單")
os.makedirs(desktop_path, exist_ok=True)
SAVE_FILE = os.path.join(desktop_path, "received_orders.txt")

@app.route('/receive', methods=['POST'])
def receive():
    data = request.get_json()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    item = data.get('item')
    quantity = data.get('quantity')
    address = data.get('address')

    with open(SAVE_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] 買什麼: {item}，幾個: {quantity}，地址: {address}\n")

    return {'status': 'ok'}, 200

if __name__ == '__main__':
    app.run(port=5000)

