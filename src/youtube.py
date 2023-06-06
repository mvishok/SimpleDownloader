from pytube import YouTube
from pytube.cli import on_progress

def download(url, system, path):
    system('cls')
    system('TITLE = Downloading...')
    yt=YouTube(url,on_progress_callback=on_progress)
    videos=yt.streams.get_highest_resolution()
    videos.download(path.expanduser("~")+"/Downloads/")
    return True