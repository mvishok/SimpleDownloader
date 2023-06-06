from validators import url as valid
from urllib.parse import urlparse

import window, youtube, insta

window.hideWindow()
window.add_hotkey('ctrl+f1', window.showWindow)
window.system('MODE CON: COLS=100 LINES=1')

def proc(url):

    #Check if valid url:
    if valid(url):
        host = '.'.join(urlparse(url).netloc.split('.')[-2:])
    else:
        return "Invalid URL"
    print(host)
    #Check which website:
    if 'youtu.be' in host or 'youtube.com' in host:
        window.system('cls')
        print('Downloading...')
        call = youtube.download(url, window.system, window.path)
        return call
    elif 'instagram' in host:
        window.system('cls')
        print('Downloading...')
        call = insta.download(url, window.system, window.path)
        return call
    else:
        return "Unkown website."
    
while True:
    window.system('TITLE = SimpleDownloader')
    inp = input('')
    if inp == '': continue
    out = proc(inp)
    if out != True:
        window.system('cls')
        window.system('TITLE = SimpleDownloader - Error')
        print(out, ' - Press enter to exit', end='')
        input()
        window.system('cls')
    else:
        window.system('cls')
        print('Downloaded to', window.path.expanduser("~")+"\Downloads\ ", " - Press enter to exit", end="")
        input()
        window.system('cls')

    window.hideWindow()