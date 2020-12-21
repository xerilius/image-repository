from flask import Flask, render_template, jsonify, session, redirect, flash
import time
from os import environ

# app = Flask(__name__, static_folder="../react-app/build/static", template_folder="../react-app/build")
app = Flask(__name__, static_folder="../react-app/build/static", static_url_path='/')
# app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/api/time')
def show_time():
  return {'time': '3:24PM'}

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  # return render_template("index.html")
  return app.send_static_file('index.html')

# Note that if you’re using React Router to route your pages, you’ll need to take an additional step and handle this on the server. To prevent it from returning a 404 not found error on the routes you’ve specified on your React app, simply redirect it to index.html.
@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')
# Use as script
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))