import os
import sys
import requests
import json
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai


app = Flask(__name__)

GOOGLE_API_KEY = "AIzaSyBiJP5jccCgmtz3FaQz9UAOKo470f9EuGE"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            response = detect_dark_patterns(url)
            return jsonify(result=response)
        except Exception as e:
            return jsonify(error=str(e)), 500
    return render_template('index.html')


def detect_dark_patterns(url):
    try:
        rply = model.generate_content(f"identify and detect dark patterns in the {url}")
        return rply.text
    except Exception as e:
        raise e

if __name__ == '__main__':
    app.run(debug=True)