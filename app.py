from flask import Flask
import pyqrcode
import png

app = Flask(__name__)

@app.route("/<id>",methods=['GET'])
def index(id):
    code = pyqrcode.create(id)
    image_as_str = code.png_as_base64_str(scale=5)
    html_img = '<img src="data:image/png;base64,{}">'.format(image_as_str)
    return html_img

def main():
    app.run(port=5000)

if __name__ == "__main__":
    main()
    