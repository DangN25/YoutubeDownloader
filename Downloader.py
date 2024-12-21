from pytubefix import YouTube

SAVE_TO = "Downloads"
link = str(input("Link: "))
ask = str(input("MP4 or MP3: ")).lower()
try:
    # object creation using YouTube 
    yt = YouTube(link) 
except: 
    #to handle exception 
    print("Connection Error") 

if ask == "mp3":
    stream = yt.streams.get_audio_only()
elif ask == "mp4":
    stream = yt.streams.get_highest_resolution()

try:
    stream.download(output_path=SAVE_TO)
    print("succesfully dowloaded ",'"', yt.title,'" as', ask)
except:
    print("ERROR!")



