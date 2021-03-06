from crypt import methods
from flask import Flask, request, abort, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello Verteego!"

@app.route("/usecase", methods=['POST'])
def post_content():
  if not request.json or 'usecase' not in request.json:
    abort(400)
  return jsonify({'usecase': request.json['usecase'], 'param1':'value1'})

if __name__ == "__main__":
  app.run()