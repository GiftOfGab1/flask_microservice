# README

## Text-to-Speech-Microservice

## Dependencies
1. Check your python version by running 'python3 --version' from your commmand line.
2. Ensure python 3.8 is installed by running 'python3.8 -V'
 - you should see this in your terminal 'Python 3.8.5'
3. If you don't have python 3.8 installed, it here: https://www.python.org/ftp/python/3.8.0/python-3.8.0a2-macosx10.9.pkg
4. Next we'll need to setup our virtual environment by running 'source venv/bin/activate' | this will create a virtual environment to install your dependencies on locally
4. So now we can start installing our dependencies. Since we will be using Flask as the microservice let's start there: 'pip3 install Flask'
5. If everything ran smoothly there, we can run 'pip3 install gunicorn'
6. '$ pip3 install flask-cors' to enable cross origin resource sharing
7. '$ pip3 install requests'

### API Access
This microservice makes a call to the Voicerss API to retrieve an audio file from the string of text you send it, the voice you want it to be, and the rate you want your speech to be in.  Sign up for your personal API key here: http://www.voicerss.org/login.aspx

To run this application you will need to setup your local config for this api_key by following these steps:
1. in the root directory of your app, run the command: '$ export VOICERS_API_KEY=your_personal_api_key'
2. This should set the variable on line 9 in the 'app.py' file to your API key.
