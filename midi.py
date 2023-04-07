import mido
import yaml
import zmq

# Connecting to server

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:9500")

# Reading config

with open('./conf/keys.yaml', 'r') as config:
    keys = yaml.safe_load(config)

device = keys['device']
notes = []

if type(keys['keys']) is str:
    rg = keys['keys'].split('...')
    for i in range(int(rg[0]), int(rg[1]) + 1):
        notes.append(i)
else:
    notes = keys['keys']

# Reading and sending events

with mido.open_input(device) as inport:
    for msg in inport:
        if msg.type == 'note_on' and msg.note in notes:
            socket.send(f'play {msg.note}'.encode())
            message = socket.recv()
            print(message)
