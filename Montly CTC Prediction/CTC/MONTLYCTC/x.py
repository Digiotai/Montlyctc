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
    if User==1:
        
        jobtitle = "Business Analyst"
    
    elif User == 2:
        jobtitle = "Junior Consultant"
    elif User ==3:
        jobtitle  = "Senior Consultant"
    elif User ==4:
        jobtitle  = "Manager"
    elif User == 5:
        jobtitle = "Country Manager"
    elif User == 6:
        jobtitle = "Region Manger"
    elif User == 7:
        jobtitle = "Partner"
    elif User == 8:
        jobtitle = "Senior Patner"
    elif User == 9:
        jobtitle = "C-Level"
    elif User == 10:
        jobtitle = "CEO"
    else:
        jobtitle = "none"
    
    
                                
    
    res ={'jobtilte' :jobtitle}
    user = np.array(User)
    user = user.reshape(-1,1)
    user = model.predict(user)
    
    

    

    #return render_template('index.html', prediction_text="Candidate Position {},  Montly CTC {}INR " .format(User,user))
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)
