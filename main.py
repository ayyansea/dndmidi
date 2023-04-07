import keyboard
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:9500")

while True:
    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_DOWN and event.name == "space":
        socket.send(b"play")
        message = socket.recv()
        print(message)
