from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Azure Python App is Working! in KIOT"

if __name__ == '__main__':
    app.run()
