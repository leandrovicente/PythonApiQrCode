import os
from flask import Flask
from flask_cors import CORS
import pyqrcode

app = Flask(__name__)

cors = CORS(app,resource={r"/*":{"origens":"*"}})


@app.route("/",methods=['GET'])
def index():
    url = pyqrcode.create('leandro')
    url.svg('qrCode.svg', scale = 8)
    arquivo = open('qrCode.svg')
    for a in arquivo:
        x = a
    print(x)

    return x

def main():
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)

if __name__ == "__main__":
    main()
    