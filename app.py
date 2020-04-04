import os
from flask import Flask
from flask_cors import CORS
import pyqrcode
import png

app = Flask(__name__)
cors = CORS(app,resource={r"/*":{"origens":"*"}})

@app.route("/<id>",methods=['GET'])
def index(id):
    code = pyqrcode.create(id)
    image_as_str = code.png_as_base64_str(scale=5)
    html_img = '<img src="data:image/png;base64,{}">'.format(image_as_str)
    return html_img


def main():
    port = int(os.environ.get("PORT",5000))
    app.run(port=port)

if __name__ == "__main__":
    main()
    