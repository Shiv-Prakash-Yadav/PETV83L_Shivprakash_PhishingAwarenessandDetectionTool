from flask import Flask, render_template, request
from phishing_detector import detect_phishing

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    url = request.form['url']
    result = detect_phishing(url)
    return render_template('result.html', url=url, result=result)

if __name__ == '__main__':
    app.run(debug=True)