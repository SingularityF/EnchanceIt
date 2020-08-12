import os
import image_downloader
import save2bucket

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def process():
    url = request.args.get('url')
    try:
        downloaded_path = image_downloader.check_and_download(url)
        return_url = save2bucket.save(downloaded_path)
    except AssertionError as error:
        return str(error)
    except:
        return "The app has encountered an unexpected error"
    return return_url

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 80)))
