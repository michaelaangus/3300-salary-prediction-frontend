from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Point this to YOUR Azure API from Assignment 1
api_url = "https://mnangus-salary-api-gzfdejb5c8affccm.eastus2-01.azurewebsites.net/predict"

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form values
    data = {
        "age": int(request.form['age']),
        "gender": int(request.form['gender']),
        "country": int(request.form['country']),
        "highest_deg": int(request.form['highest_deg']),
        "coding_exp": int(request.form['coding_exp']),
        "title": int(request.form['title']),
        "company_size": int(request.form['company_size'])
    }

    # Send to Azure API
    response = requests.post(api_url, json=data)
    result = response.json()
    predicted_salary = result['predicted_salary']

    return render_template('index.html', predicted_salary=predicted_salary)

if __name__ == '__main__':
    app.run(debug=True)