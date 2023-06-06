import instaloader
from re import search

ig = instaloader.Instaloader()

def extract_shortcode_from_url(url):
    shortcode_match = search(r"/p/([A-Za-z0-9_-]+)/", url)
    if shortcode_match:
        return shortcode_match.group(1)
    return None

def download(url, system, path):
    system('cls')
    system('TITLE = Downloading...')
    #-->
    post = instaloader.Post.from_url(ig.context, extract_shortcode_from_url(url))
    ig.download_post(post, target=path.expanduser("~")+"/Downloads/")
    return True