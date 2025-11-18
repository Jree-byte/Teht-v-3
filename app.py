from flask import Flask, render_template_string
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='VITTU',
        password='Moimoi33-',
        database='Ecard'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from MySQL!'")
    message = cursor.fetchone()[0]
    cursor.execute("SELECT NOW()")
    current_time = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>LEMP Home</title>
        <style>
            body {{
                background-color: #eef4fa;
                font-family: Arial, sans-serif;
                text-align: center;
                color: #2c3e50;
                padding-top: 60px;
            }}
            .box {{
                background-color: #ffffff;
                display: inline-block;
                padding: 30px 50px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }}
            h1 {{ color: #1a5276; }}
            p {{ font-size: 18px; }}
            a {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #1a5276;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }}
            a:hover {{ background-color: #154360; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Welcome to LEMP Home</h1>
            <p>{message}</p>
            <p>Current SQL Server Time: {current_time}</p>
            <p><a href="/data-analysis/" target="_blank">Go to Data Analysis (Streamlit)</a></p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

