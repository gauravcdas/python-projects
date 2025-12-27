# Importing the required libraries
import pyttsx3
from PyPDF2 import PdfReader
import threading
import keyboard

pdf = None
stop_thread = False #variable to signal stopping the playback

def play(PdfReader):
    global pdf
    global stop_thread

    speaker = pyttsx3.init()

    for page_num in range(len(PdfReader.pages)):
        if stop_thread:
            break
        text = PdfReader.pages[page_num].extract_text()
        speaker.say(text)
        speaker.runAndWait() # to produce the sound
    speaker.stop()

def stop_playback():
    global stop_thread
    input("Press enter to stop playback")
    stop_thread = True

file = input("Enter your pdf file name: -")

while True:
    try:
        pdf = PdfReader(file)
        break
    except Exception as e:
        print("An error occurred:\n", e)
        print("\nEnter the file name again:\n")
        file = input("Enter your PDF file name: ")

# Create a sequence thread to playback
playback_thread = threading.Thread(target=play, args=(pdf,))
playback_thread.start()

# Start a thread for stopping playback with keyboard input
keyboard.add_hotkey("q", lambda : stop_playback())
keyboard.wait('esc') # wait the hotkey event

# wait for the playback to finish
playback_thread.join()


