#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
pickle.dump(model,open('rdf.pkl','wb'))
from flask import Flask, render_template, request
import numpy as np
import pickle
app = Flask(__name__)
model = pickle.load(open(r'rdf.pkl','rb'))
scale = pickle.load(open(r'scale1.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')
import pandas as pd
@app.route('/submit',methods=["POST","GET"])
def submit():
    
    input_feature=[int(x) for x in request.form.values() ]
    
    input_feature=[np.array(input_feature)]
    print(input_feature)
    names = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome'
             'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
        data = pandas.DataFrame(input_feature,columns = names)     
        print(data)
             
             
             
             prediction=model.predict(df)
             print(prediction)
             prediction = int(prediction)
             print(type(prediction))
             
             if (prediction ==0)
               return render=template("output.html",result = "Loan will not be Approved")
             else:
               return render_template("output.html",result = Loan will be Approved)
        if __name__ == "__main__":
    
    port=int(os.environ.get('PORT',50000))
    app.run(debug=False)


# In[ ]:




