#step -1 # Importing flask module in the project is mandatory 

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.svm import SVR




#Step -2 Flask constructor takes the name of  
# current module (__name__) as argument.app = Flask(__name__)

app = Flask(__name__)

#Step -3 Load Trained Regression Model
model = pickle.load(open('SVR.pkl', 'rb'))


# Step -5 The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function


@app.route('/')
def home():
    return render_template('index.html')
# ‘/’ URL is bound with predict() function.
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    User =request.form['msg']
    
    if User==1:
        print("Business Analyst")
    
    elif User == 2:
        print("Junior Consultant")
    elif User ==3:
        print("Senior Consultant")
    elif User ==4:
        print("Manager")
    elif User == 5:
        print("Country Manager")
    elif User == 6:
        print("Region Manger")
    elif User == 7:
        print("Partner")
    elif User == 8:
        print("Senior Patner")
    elif User == 9:
        print("C-Level")
    elif User == 10:
        print("CEO")
    elif User > 10:
        print("Enter the position level between 1 to 10")
                                
    else:
        print("")

    user = np.array(User)
    user = user.reshape(-1,1)
    user = model.predict(user)
    print("Candidate Position Level:{}, Montly CTC {}INR " .format(User,user))
    
                                
    
    
   
    

    

    return render_template('index.html', prediction_text="Candidate Position Level:{}, Montly CTC {}INR " .format(User,user)


# main driver function
 # run() method of Flask class runs the application  
    # on the local development server.
    

    if __name__ == '__main__':
        app.run(debug=True)
