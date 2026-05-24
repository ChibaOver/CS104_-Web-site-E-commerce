from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# เชื่อมต่อฐานข้อมูล
def get_db_connection():
    conn = sqlite3.connect('web.db')
    conn.row_factory = sqlite3.Row
    return conn

# หน้าแรก
@app.route('/')
def home():
    conn = get_db_connection()

    # ดึงข้อมูลสินค้า
    products = conn.execute('SELECT * FROM products').fetchall()

    conn.close()

    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)