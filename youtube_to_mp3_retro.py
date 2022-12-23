import pytube
import os

url = input("enter the url: ")
if url == " ":
    url = "https://www.youtube.com/watch?v=KMU0tzLwhbE"

path= "/Users/veerbhatia/Downloads"

audio = pytube.YouTube(url).streams.get_audio_only()
audio_download = audio.download(output_path=path)
base, ext = os.path.splitext(audio_download)
new_file = base + '.mp3'
os.rename(audio_download, new_file)

