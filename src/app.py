import os
import image_downloader
import save2bucket
import processing

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def process():
    url = request.args.get('url')
    # ===== Image Download =====
    try:
        assert (url is not None), "Empty GET parameter"
        downloaded_path = image_downloader.check_and_download(url)
    except AssertionError as error:
        return str(error)
    except:
        return "Image download failed"
    # ===== Image Super-resolution =====
    try:
        processed_path = processing.waifu2x_chainer(os.path.abspath(downloaded_path))
    except AssertionError as error:
        return str(error)
    except:
        return "The app has encountered an unexpected error"
    # ===== Image Upload to Bucket =====
    try:
        return_url = save2bucket.save(processed_path)
    except:
        return "The app has encountered an unexpected error"
    return return_url

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 80)))
