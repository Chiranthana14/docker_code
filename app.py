from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
   return 'Hello, this is my Python web application running in a Docker container!'
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')