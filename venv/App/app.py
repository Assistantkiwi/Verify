from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url)
            if response.status_code == 200:
                result = "URL is valid and reachable."
            else:
                result = f"URL returned status code {response.status_code}."
        except requests.exceptions.RequestException as e:
            result = f"Error: {e}"
        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)