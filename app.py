import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app,resource={r"/*":{"origens":"*"}})


@app.route("/",methods=['GET'])
def index():
    return "<h1> Hellow</h1>"

def main():
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=5000)

if __name__ == "__main__":
    main()
    