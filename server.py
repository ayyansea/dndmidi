import zmq
import yaml
from pydub import AudioSegment
from pydub.playback import play

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:9500")

def load_config():
    with open('conf/dndmidi.yaml', 'r') as config:
        settings = yaml.safe_load(config)

    return settings

settings = load_config()
print(settings)

while True:
    message = socket.recv().decode()
    if message == "play":
        sound = AudioSegment.from_file("test.wav", format="wav")
        socket.send(b"Sound is playing.")
        play(sound)
