

import numpy as np;
import pandas as pd;
#import seaborn as sns;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle


data=pd.read_csv('apy.csv',na_values='=')




                             










data2=data
data2=data2.dropna(axis=0)



aa=data2['Season']
cropnames=set(aa)
print(cropnames)
data2['Season']=data2['Season'].map({'Rabi       ':1, 'Whole Year ':2, 'Autumn     ':3, 'Winter     ':4, 'Summer     ':5, 'Kharif     ':6})
seasonlist={'Rabi       ':1, 'Whole Year ':2, 'Autumn     ':3, 'Winter     ':4, 'Summer     ':5, 'Kharif     ':6}

print(data2['Season'])
data2['Crop']=data2['Crop'].map({'Soyabean':1, 'Bajra':2, 'Cardamom':3, 'Onion':4, 'Coffee':5, 'Beans & Mutter(Vegetable)':6, 'Lab-Lab':7, 'Sweet potato':8, 'Moth':9, 'Tea':10, 'Small millets':11, 'Linseed':12, 'Paddy':13, 'Rubber':14, 'Khesari':15, 'Arecanut':16, 'Lemon':17, 'Turnip':18, 'Rajmash Kholar':19, 'Other Cereals & Millets':20, 'Jowar':21, 'Arcanut (Processed)':22, 'Sunflower':23, 'Citrus Fruit':24, 'Moong(Green Gram)':25, 'Cucumber':26, 'Redish':27, 'Bottle Gourd':28, 'Oilseeds total':29, 'Pome Granet':30, 'Colocosia':31, 'Banana':32, 'Jack Fruit':33, 'Carrot':34, 'Brinjal':35, 'Papaya':36, 'Cowpea(Lobia)':37, 'Niger seed':38, 'Ash Gourd':39, 'Atcanut (Raw)':40, 'Guar seed':41, 'Masoor':42, 'Varagu':43, 'Cond-spcs other':44, 'Sannhamp':45, 'Peas  (vegetable)':46, 'Cotton(lint)':47, 'Other Fresh Fruits':48, 'Pulses total':49, 'Bean':50, 'Ragi':51, 'Bhindi':52, 'Dry chillies':53, 'Tobacco':54, 'Rice':55, 'Cashewnut Processed':56, 'other oilseeds':57, 'Orange':58, 'Ginger':59, 'Pineapple':60, 'Horse-gram':61, 'Cauliflower':62, 'Other Kharif pulses':63, 'Mango':64, 'Groundnut':65, 'Cashewnut Raw':66, 'Perilla':67, 'Kapas':68, 'Castor seed':69, 'Yam':70, 'Korra':71, 'Coriander':72, 'Urad':73, 'Tomato':74, 'Sapota':75, 'Mesta':76, 'Apple':77, 'Wheat':78, 'Barley':79, 'Grapes':80, 'Bitter Gourd':81, 'Ber':82, 'Lentil':83, 'Jobster':84, 'Pear':85, 'Snak Guard':86, 'Garlic':87, 'Tapioca':88, 'Other Citrus Fruit':89, 'Arhar/Tur':90, 'Peas & beans (Pulses)':91, 'Other Vegetables':92, 'Dry ginger':93, 'Turmeric':94, 'Blackgram':95, 'Cashewnut':96, 'Other  Rabi pulses':97, 'Other Dry Fruit':98, 'Peach':99, 'Beet Root':100, 'Total foodgrain':101, 'Plums':102, 'Ribed Guard':103, 'Jute':104, 'Black pepper':105, 'other misc. pulses':106, 'other fibres':107, 'Drum Stick':108, 'Water Melon':109, 'Safflower':110, 'Maize':111, 'Sugarcane':112, 'Litchi':113, 'Rapeseed &Mustard':114, 'Ricebean (nagadal)':115, 'Samai':116, 'Gram':117, 'Cabbage':118, 'Jute & mesta':119, 'Potato':120, 'Pump Kin':121, 'Coconut ':122, 'Sesamum':123, 'Pome Fruit':124})
croplist={'Soyabean':1, 'Bajra':2, 'Cardamom':3, 'Onion':4, 'Coffee':5, 'Beans & Mutter(Vegetable)':6, 'Lab-Lab':7, 'Sweet potato':8, 'Moth':9, 'Tea':10, 'Small millets':11, 'Linseed':12, 'Paddy':13, 'Rubber':14, 'Khesari':15, 'Arecanut':16, 'Lemon':17, 'Turnip':18, 'Rajmash Kholar':19, 'Other Cereals & Millets':20, 'Jowar':21, 'Arcanut (Processed)':22, 'Sunflower':23, 'Citrus Fruit':24, 'Moong(Green Gram)':25, 'Cucumber':26, 'Redish':27, 'Bottle Gourd':28, 'Oilseeds total':29, 'Pome Granet':30, 'Colocosia':31, 'Banana':32, 'Jack Fruit':33, 'Carrot':34, 'Brinjal':35, 'Papaya':36, 'Cowpea(Lobia)':37, 'Niger seed':38, 'Ash Gourd':39, 'Atcanut (Raw)':40, 'Guar seed':41, 'Masoor':42, 'Varagu':43, 'Cond-spcs other':44, 'Sannhamp':45, 'Peas  (vegetable)':46, 'Cotton(lint)':47, 'Other Fresh Fruits':48, 'Pulses total':49, 'Bean':50, 'Ragi':51, 'Bhindi':52, 'Dry chillies':53, 'Tobacco':54, 'Rice':55, 'Cashewnut Processed':56, 'other oilseeds':57, 'Orange':58, 'Ginger':59, 'Pineapple':60, 'Horse-gram':61, 'Cauliflower':62, 'Other Kharif pulses':63, 'Mango':64, 'Groundnut':65, 'Cashewnut Raw':66, 'Perilla':67, 'Kapas':68, 'Castor seed':69, 'Yam':70, 'Korra':71, 'Coriander':72, 'Urad':73, 'Tomato':74, 'Sapota':75, 'Mesta':76, 'Apple':77, 'Wheat':78, 'Barley':79, 'Grapes':80, 'Bitter Gourd':81, 'Ber':82, 'Lentil':83, 'Jobster':84, 'Pear':85, 'Snak Guard':86, 'Garlic':87, 'Tapioca':88, 'Other Citrus Fruit':89, 'Arhar/Tur':90, 'Peas & beans (Pulses)':91, 'Other Vegetables':92, 'Dry ginger':93, 'Turmeric':94, 'Blackgram':95, 'Cashewnut':96, 'Other  Rabi pulses':97, 'Other Dry Fruit':98, 'Peach':99, 'Beet Root':100, 'Total foodgrain':101, 'Plums':102, 'Ribed Guard':103, 'Jute':104, 'Black pepper':105, 'other misc. pulses':106, 'other fibres':107, 'Drum Stick':108, 'Water Melon':109, 'Safflower':110, 'Maize':111, 'Sugarcane':112, 'Litchi':113, 'Rapeseed &Mustard':114, 'Ricebean (nagadal)':115, 'Samai':116, 'Gram':117, 'Cabbage':118, 'Jute & mesta':119, 'Potato':120, 'Pump Kin':121, 'Coconut ':122, 'Sesamum':123, 'Pome Fruit':124}
# new_data1=pd.get_dummies(data2,drop_first=True)
cropprice={'Soyabean':3710, 'Bajra':2000, 'Cardamom':3256, 'Onion':4000, 'Coffee':5000, 'Beans & Mutter(Vegetable)':6000, 'Lab-Lab':7000, 'Sweet potato':1300, 'Moth':1200, 'Tea':30000, 'Small millets':4000, 'Linseed':8000, 'Paddy':4000, 'Rubber':5000, 'Khesari':5000, 'Arecanut':20000, 'Lemon':6000, 'Turnip':1800, 'Rajmash Kholar':14000, 'Other Cereals & Millets':6000, 'Jowar':8000, 'Arcanut (Processed)':4500, 'Sunflower':4800, 'Citrus Fruit':8000, 'Moong(Green Gram)':11100, 'Cucumber':2800, 'Redish':50000, 'Bottle Gourd':25000, 'Oilseeds total':100000, 'Pome Granet':3000, 'Colocosia':3211, 'Banana':2000, 'Jack Fruit':2500, 'Carrot':2200, 'Brinjal':1500, 'Papaya':3000, 'Cowpea(Lobia)':3000, 'Niger seed':7500, 'Ash Gourd':3900, 'Atcanut (Raw)':4000, 'Guar seed':5000, 'Masoor':6000, 'Varagu':4000, 'Cond-spcs other':3600, 'Sannhamp':5000, 'Peas  (vegetable)':7000, 'Cotton(lint)':4700, 'Other Fresh Fruits':4800, 'Pulses total':4000, 'Bean':6000, 'Ragi':3200, 'Bhindi':2000, 'Dry chillies':16000, 'Tobacco':2230, 'Rice':5200, 'Cashewnut Processed':5600, 'other oilseeds':4600, 'Orange':5800, 'Ginger':6000, 'Pineapple':4000, 'Horse-gram':6890, 'Cauliflower':7800, 'Other Kharif pulses':7000, 'Mango':5000, 'Groundnut':6000, 'Cashewnut Raw':4000, 'Perilla':7000, 'Kapas':4000, 'Castor seed':3000, 'Yam':1800, 'Korra':4000, 'Coriander':5467, 'Urad':6754, 'Tomato':4000, 'Sapota':16500, 'Mesta':6000, 'Apple':11000, 'Wheat':3850, 'Barley':4300, 'Grapes':4000, 'Bitter Gourd':21000, 'Ber':2400, 'Lentil':5800, 'Jobster':8400, 'Pear':2000, 'Snak Guard':4000, 'Garlic':6000, 'Tapioca':5500, 'Other Citrus Fruit':5000, 'Arhar/Tur':5000, 'Peas & beans (Pulses)':8500, 'Other Vegetables':3000, 'Dry ginger':14000, 'Turmeric':12000, 'Blackgram':9900, 'Cashewnut':53000, 'Other  Rabi pulses':6000, 'Other Dry Fruit':10000, 'Peach':8000, 'Beet Root':10000, 'Total foodgrain':6500, 'Plums':7600, 'Ribed Guard':6500, 'Jute':5600, 'Black pepper':4500, 'other misc. pulses':4200, 'other fibres':6700, 'Drum Stick':4300, 'Water Melon':7800, 'Safflower':6750, 'Maize':1950, 'Sugarcane':1600, 'Litchi':8000, 'Rapeseed &Mustard':4000, 'Ricebean (nagadal)':6000, 'Samai':4900, 'Gram':3000, 'Cabbage':6000, 'Jute & mesta':6500, 'Potato':3000, 'Pump Kin':2300, 'Coconut ':5000, 'Sesamum':2900, 'Pome Fruit':7600}
 

dist=(data2['District_Name'])
distset=set(dist)
dd=list(distset)
dictOfWords = { dd[i] : i  for i in range(0, len(dd) ) }
data2['District_Name']=data2['District_Name'].map(dictOfWords)




ss=data2['State_Name']
st=set(ss)
st1=list(st)
statenames= { st1[i] : i  for i in range(0, len(st1) ) }
data2['State_Name']=data2['State_Name'].map(statenames)



data2['Area']=data2['Area'].astype('int')
data2['Production']=data2['Production'].astype('int')

























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
model = pickle.load(open('modelknn.pkl', 'rb'))
model1 = pickle.load(open('modelknn1.pkl', 'rb'))

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
              print(r11)
              print(r22)
              

# Open database connection
              if  r11==logu and  r22==passw:
                  print("if loop do")
                  return render_template('index.html')
                                               



                          
                     # print(value1[0:])
    
    
    
    

              
              # int_features3[0]==12345 and int_features3[1]==12345:
               #                      return render_template('index.html')
        
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
   


@app.route('/production')
def production(): 
    return render_template('index.html')


@app.route('/production/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [str(x) for x in request.form.values()]
    a=int_features
    print(str(a[0]))
    t1=(statenames[str(a[0])])
    int_features[0]=int(t1)

    print(str(a[1]))
    t2=(dictOfWords[str(a[1])])
    int_features[1]=int(t2)
    
    
    print(str(a[3]))
    t4=(seasonlist[str(a[3])])
    int_features[3]=int(t4)
    
    
    print(str(a[4]))
    t5=(croplist[str(a[4])])
    int_features[4]=int(t5)
    
    
    int_features2 = np.array(int_features)

    int_features1 = int_features2.reshape(1, -1)
    prediction = model.predict(int_features1)

    output = prediction[0]

    return render_template('index.html', prediction_text='production will be    {} quintles'.format(output))

@app.route('/crop')
def crop():
     return render_template('crop.html')



@app.route('/crop/predict1',methods=['POST'])
def predict1():
    '''
    For rendering results on HTML GUI
    '''
    int_features1 = [str(x) for x in request.form.values()]
    int_features2=['1','2','3','4','5','6']
    locationm=str(int_features1[6])
    
    
    
    import requests
    from pprint import pprint

    #city = input('Enter your city : ')

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=f62068f48bd72cb957e312620da07d11&units=metric'.format(locationm)

    res = requests.get(url)

    data = res.json()
    print(data)

    temp = data['main']['temp']
    wind_speed = data['wind']['speed']

    latitude = data['coord']['lat']
    longitude = data['coord']['lon']

    description = data['weather'][0]['description']

    pressure= data['main']['pressure']
    humidity= data['main']['humidity']

    print('Temperature : {} degree celcius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Description : {}'.format(description))
    print('Pressure : {}'.format(pressure))
    print('humidity : {}'.format(humidity))




    b=int_features1
    print(str(b[0]))
    t11=(statenames[str(b[0])])
    int_features2[2]=int(t11)

    print(str(b[1]))
    t22=(dictOfWords[str(b[1])])
    int_features2[3]=int(t22)
    
    
    print(str(b[3]))
    t44=(seasonlist[str(b[3])])
    int_features2[1]=int(t44)
    
    int_features2[0]=int_features1[2]
    int_features2[5]=int_features1[5]
    int_features2[4]=int_features1[4]
    
    
    
    int_features21 = np.array(int_features2)




    int_features11 = int_features21.reshape(1, -1)
    prediction1 = model1.predict(int_features11)

    output1 = prediction1[0]
    resultcrop = {value:key for key, value in croplist.items()}
    print(resultcrop)
    
    outputcrop=(resultcrop[int(output1)])
 
    

    

    return render_template('crop.html', prediction1_text='alternatively you can grow    {}   which will give the better production.'.format(outputcrop),temp1='temparature is {} celsius '.format(temp),wind_speed='wind speed is  is {} m/s'.format(wind_speed),latitude='latitude  is {}'.format(latitude),longitude='longitude is {}'.format(longitude),description='climate/sky is {}'.format(description),pressure='pressure  is {}'.format(pressure),humidity='humidity  is {}'.format(humidity))



if __name__ == "__main__":
    app.run(debug=True)
