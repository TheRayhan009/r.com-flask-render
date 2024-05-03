from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/photos')
def photo():
    return render_template("photos.html")
@app.route('/video')
def video():
    return render_template("video.html")
def fb_clon():
    return render_template("clon.html")
