from os import path
import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='./dist/views/',
            static_folder='/dist/')

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory(path.join(os.getcwd(), 'dist'), filename)

@app.route('/assets/icons/svg/<path:filename>')
def serve_svg(filename):
    return send_from_directory(path.join(os.getcwd(), 'src', 'public', 'assets', 'icons', 'svg'), filename)

@app.route('/assets/icons/<path:filename>')
def serve_icons(filename):
    return send_from_directory(path.join(os.getcwd(), 'src', 'public', 'assets', 'icons'), filename)

@app.route('/assets/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(path.join(os.getcwd(), 'src', 'public', 'assets', 'images'), filename)

if __name__ == '__main__':
    app.run(debug=True)
