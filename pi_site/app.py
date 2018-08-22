#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response, request, jsonify
import json
import glob
import requests

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera

app = Flask(__name__)

PIC_FOLDER = os.path.join('static', 'pi_photos')
app.config['UPLOAD_FOLDER'] = PIC_FOLDER

def get_recording_status():
    uri = "http://163.221.68.237:5000/is_recording"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    return Jresponse

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print("POST!")
        text = request.form['text']
        with open('flags.json', 'r+') as f:
          data = json.load(f)
          #TODO: Change text of recording button
          if data['recording'] == "False":
              data['recording'] = "True"
              recording_state = "Stop recording"
          else:
              data['recording'] = "False"
              recording_state = "Start recording"
          f.seek(0)        # <--- should reset file position to the beginning.
          json.dump(data, f, indent=4)
          f.truncate()     # remove remaining part

        status = get_recording_status()
        return render_template('index.html', extra_text=status)
    """Video streaming home page."""

    status = get_recording_status()
    return render_template('index.html', extra_text=status)


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def get_latest_file():
    list_of_files = glob.glob(app.config['UPLOAD_FOLDER'] + '/*') # * means all if need specific format then *.csv
    if len(list_of_files) > 0:
      latest_file = max(list_of_files, key=os.path.getctime)
      return latest_file
    else:
      return ""

@app.route('/pi_photos')
def pi_photos():
    latest_file = {'path': get_latest_file()}
    return jsonify(latest_file)

@app.route('/is_recording')
def is_recording():
    with open('flags.json', 'r+') as f:
        data = json.load(f)
        status = {}
        status['status'] = data['recording']

        f.close()
    return status['status']

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# def update_json_flags(flag, newbool):
#     with open('flags.json', 'r+') as f:
#       data = json.load(f)
#       data[flag] = newbool
#       f.seek(0)
#       json.dump(data, f, indent=4)
#       f.truncate()

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)
