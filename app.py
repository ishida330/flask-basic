from flask import Flask
#import os

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
#port = os.getenv('PORT', '5000') # portはIBM Cloud環境から割り当てられたものを利用

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=int(port), debug=True) # Procfile内でpython hello.pyで起動
    app.run(host='0.0.0.0', port=8090)
