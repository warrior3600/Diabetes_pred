import numpy as np
from flask import Flask,request,render_template
from joblib import load

app = Flask(__name__)
model = load('random_forest.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    print(int_features)
    final_features = np.array([int_features])
    print(type(final_features))
    prediction = model.predict(final_features)
    print(prediction)
    print(prediction.shape)
    pred_final = ''
    if prediction.item(0) == 0:
        pred_final = "Non Diabetic!!, Don't Worry😇"
    else:
        pred_final = "Diabetic!!, Please consult the doctor"
    print(pred_final)
    return render_template('index.html',predicton_details = pred_final)

if __name__ == "__main__":
    app.run(debug=True)