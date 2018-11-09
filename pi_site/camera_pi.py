import io
import time
import picamera
from base_camera import BaseCamera
import datetime
from PIL import Image
from pytz import timezone
import json

tokyo_tz = timezone('Asia/Tokyo')

def get_timestamp():
   #curr_time = datetime.datetime.now() - timedelta(hours=2)
   #return curr_time.strftime('%Y-%m-%d_%H-%M-%S')
    return datetime.datetime.now(tokyo_tz).strftime('%Y-%m-%d_%H-%M-%S')

def get_rec_flag():
    with open('flags.json', 'r+') as f:
        data = json.load(f)

        return data['recording']

class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            # let camera warm up
            time.sleep(2)
            camera.resolution = (640, 480)
            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()
                curr_time = datetime.datetime.now()
                seconds = curr_time.strftime('%S')
                if int(seconds) % 10 == 0 and get_rec_flag() == "True":
                    print("Saving image!")
                    image = Image.open(stream)
                    image.save('static/pi_photos/' + get_timestamp() + ".png", "PNG")

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
