# Taken from https://android.jlelse.eu/handmade-backend-for-android-app-using-python-flask-framework-b173ba2bb3aa
from flask import Flask, request, jsonify

app = Flask(__name__)

# root
@app.route("/")
def index():
  """
  this is a root dir of the server
  :return: str
  """
  return "This is the root"

# POST
@app.route("/api/upload_photo", methods=["POST"])
def get_image_prediction():
  """
  predicts requested images whether it is an empanada
  :return: json
  """
  json = request.get_json()
  print(json)
  return jsonify({"this is the response": json })

# running web app in local machine
if __name__ == "__main__":
  app.run(host="0.0.0.0", port="8080")