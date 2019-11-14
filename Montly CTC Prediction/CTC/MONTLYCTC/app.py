import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('SVR.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    User =request.form['msg']
    
    user = np.array(User)
    user = user.reshape(-1,1)
    user = model.predict(user)
    
    

    

    return render_template('index.html', prediction_text="Candidate Position {},  Montly CTC {}INR " .format(User,user))
    #return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)
