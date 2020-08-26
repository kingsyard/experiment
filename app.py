



import pyrebase

config = {
	"apiKey": "AIzaSyAD6kvrK16x3nnQVQpnybP90YBSjz0X8Og",
  "authDomain": "agriculture-81f5b.firebaseapp.com",
  "databaseURL": "https://agriculture-81f5b.firebaseio.com",
  "projectId": "agriculture-81f5b",
  "storageBucket": "agriculture-81f5b.appspot.com",
  "messagingSenderId": "939998839868",
  "appId": "1:939998839868:web:bdba7971bfd933c1faef39",
  "measurementId": "G-9XLTMEPH2K"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
























import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html') 

@app.route('/logedin',methods=['POST'])
def logedin():
    
              int_features3 = [str(x) for x in request.form.values()]
              print(int_features3)
              logu=int_features3[0]
              passw=int_features3[1]
              
              register=db.child("names").get()

              r5=register[0].val()


              r11=r5["name"]
              r22=r5["pass"]

              


              if  r11==logu and  r22==passw:
                  print("if loop do")
                  return render_template('index.html')
                                                       
@app.route('/register',methods=['POST'])
def register():
    

    int_features2 = [str(x) for x in request.form.values()]
    #print(int_features2)
    #print(int_features2[0])
    #print(int_features2[1])
    r1=int_features2[0]
    print(r1)
    
    r2=int_features2[1]
    print(r2)
        
    
   
    db.child("names").push({"name":"king","pass":"123"})

#db.child("name").child("name").update({"name":"king1"})
    register=db.child("names").get()

    r5=register[0].val()


    r11=r5["name"]
    r22=r5["pass"]
    
   
   # if int_features2[0]==12345 and int_features2[1]==12345:



    return render_template('login.html')
   





if __name__ == "__main__":
    app.run(debug=True)
