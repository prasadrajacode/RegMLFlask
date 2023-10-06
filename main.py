from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)

# Load the pre-trained linear regression model
with open('reg_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    test_score = float(data['Test Score'])
    interview_score = float(data['Interview Score'])
    experience = float(data['Experience'])
    input_data = [test_score, interview_score, experience]
    prediction = loaded_model.predict([input_data])
    response = {
        'prediction': prediction[0]
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
