from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    fuel_type = request.form.get('fuel')
    kms_driven = float(request.form.get('kms'))
    seller_type = request.form.get('seller')
    transmission = request.form.get('transmission')
    year = 2023 - int(request.form.get('year'))
    
    features = pd.DataFrame([[kms_driven, year, fuel_type, seller_type, transmission]],
                            columns=['Kms_Driven', 'age_of_the_car', 'Fuel_Type_Diesel', 'Seller_Type_Individual', 'Transmission_Manual'])
    
    prediction = model.predict(features)
    
    return render_template('index.html', prediction_text='The predicted selling price of the used car is {:.2f} lakhs.'.format(prediction[0]))

if __name__ == '__main__':
    app.run(debug=True)
