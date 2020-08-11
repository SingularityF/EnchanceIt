import requests
import uuid
import os

supported_types = [
        "image/jpeg",
        "image/png",
        ]
max_content_length = 5 * 1024 * 1024 # Bytes


def header_check(url):
    res = requests.head(url)
    header = res.headers
    assert ("image" in header['Content-Type']), "Url is not an image"
    assert (header['Content-Type'] in supported_types), "Image format not supported"
    assert (int(header['Content-Length']) < max_content_length), "Image file size too large"
    extension = header['Content-Type'].split('/')[1]
    return extension


def download(url, ext):
    res = requests.get(url)
    if not os.path.exists('downloads'):
        os.mkdir('downloads')
    filename = str(uuid.uuid4())
    filepath = f"downloads/{filename}.{ext}"
    with open(filepath, "wb") as f:
        f.write(res.content)
    return filepath


def check_and_download(url):
    ext = header_check(url)
    filepath = download(url, ext)
    return filepath


if __name__ == "__main__":
    url = ""
    try:
        print(check_and_download(url))
    except AssertionError as error:
        print(error)
    except:
        print("The app has encountered an unexpected error")
