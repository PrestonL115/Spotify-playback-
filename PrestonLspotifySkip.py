import subprocess
import sys

#function will install package if not already installed
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#installs modules needed for hotkeys and integrates spotify web api
install_package("pynput")
install_package("spotipy")

# imports the previously installed packages
from pynput import keyboard
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#sets up Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="6ec8772385d747f5a342b4622de72ac3",
    client_secret="1915d18c51054ba2b2e2739719045645",
    redirect_uri="http://localhost:8080/callback/",
    scope="user-modify-playback-state user-read-playback-state"
))
# retrieves current playback status, check playback status, then toggles playback
def play_pause():
    current_playback = sp.current_playback()
    if current_playback and current_playback['is_playing']:
        sp.pause_playback()
    else:
        sp.start_playback()

def next_track():
    sp.next_track()

def previous_track():
    sp.previous_track()

#set up hotkey listener, will wait until hotkey is pressed, when one is pressed it will execute function
def on_press(key):
    try:
        if key == keyboard.Key.f5:  # Play/pause when F5 is pressed
            play_pause()
        elif key == keyboard.Key.f6:  # Skip track with F6
            next_track()
        elif key == keyboard.Key.f7:  # Previous track with F7
            previous_track()
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
