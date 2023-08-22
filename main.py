from flask import Flask, render_template_string
import requests

app = Flask(__name__)

REPO_URL = "https://raw.githubusercontent.com/sergeymalyaroff/SM_HW_webtest/main/index.html"

@app.route('/')
def index():
    response = requests.get(REPO_URL)
    if response.status_code == 200:
        return render_template_string(response.text)
    else:
        return "Ошибка при получении данных с репозитория.", 500

if __name__ == "__main__":
    app.run(debug=True)
