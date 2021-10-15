from flask import Flask,jsonify,request
from Classifier import get_prediction

app = Flask(__name__)

@app.route("/predict-digit", methods=["POST"])
def predict_data():
    read_data = request.files.get("digit")
    prediction = get_prediction(read_data)

    return jsonify({
        "prediction" : prediction
    }), 200

if __name__ == "__main__":
    app.run(debug=True)