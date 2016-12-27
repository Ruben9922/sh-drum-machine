from sense_hat import SenseHat
from queue import Queue
from time import sleep

def print_options():
    for option in options:
        print("  '" + option[0] + "': " + option[1])

def get_option_pixels(char):
    for option in options:
        if (char == option[0]):
            return option[2]
    return []

def display_queue():
    sense.clear()
    size = queue.qsize()
    for i in range(size):
        temp = queue.get_nowait()
        for j in range(len(temp)):
            sense.set_pixel(i, 7 - j, temp[j])
        queue.put_nowait(temp)

# Initial setup
sense = SenseHat()
sense.set_rotation(180)
sense.low_light = True

options = [
    ('k', "Kick", [[0, 0, 0], [255, 0, 0]]),
    ('s', "Snare", [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 255, 0]]),
    (' ', "Rest", [])
]
delay = 0.2

# print("Welcome to Drum Machine!")
# print_options()

# string = input("Enter string of above sounds: ")
string = "k k s   "
queue = Queue(maxsize=8)

for i in range(8):
    queue.put_nowait([])

for i in range(16):
    print(i, end='\r')
    for c in string:
        c = c.lower()
        pixels = get_option_pixels(c)
        if (queue.full()):
            queue.get_nowait()
        queue.put_nowait(pixels)

        display_queue()

        sleep(delay)

for i in range(8):
    if (queue.full()):
        queue.get_nowait()
    queue.put_nowait([])

    display_queue()

    sleep(delay)

sense.low_light = False
