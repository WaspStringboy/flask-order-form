from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)

SAVE_FILE = "received_orders.txt"

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    item = request.form.get('item')
    quantity = request.form.get('quantity')
    address = request.form.get('address')

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(SAVE_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] 買什麼: {item}，幾個: {quantity}，地址: {address}\n")

    return redirect(url_for('success'))

@app.route('/success')
def success():
    return "<h2>✅ 資料已送出，感謝您的訂購！</h2><a href='/'>回到表單</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
