from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Nasa image of the day:
    url = "https://apod.nasa.gov/apod/image/2001/Hyades_Mtanous_1080.jpg"
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
