from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech/<phrase>', methods=['GET'])
def speak(phrase):
  audio = requests.get('https://api.voicerss.org/?key=5965c450ab324b21b297ea2d6ce96846&hl=en-us&src='+phrase+'&f=44khz_16bit_stereo&ssml=false&b64=false')

  return audio.text

if __name__ == "__main__":
    app.run(debug=True)
