from flask import Flask, render_template, request
import requests
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_envvar('APP_SETTINGS')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech/<phrase>/<rate>/<voice>', methods=['GET'])
def speak(phrase, rate, voice):
  audio = requests.get('https://api.voicerss.org/?key=5965c450ab324b21b297ea2d6ce96846&hl=en-us&src='+phrase+'&r='+rate+'&v='+voice+'')

  return audio.content

if __name__ == "__main__":
    app.run()
