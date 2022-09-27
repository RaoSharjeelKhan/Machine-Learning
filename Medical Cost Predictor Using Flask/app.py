from flask import Flask, render_template, request
import pickle 


app = Flask(__name__)

Amin=64
Amax=18
Bmin=15.96
Bmax=53.13
Cmin=0
Cmax=5
Xmax=63770.428010
Xmin=1121.873900

model = pickle.load(open('model.pkl','rb')) #read mode
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        #access the data from form
        ## Age
        age = int(request.form["age"])
        age=(age-Amin)/(Amax-Amin)
        bmi = int(request.form["bmi"])
        bmi=(bmi-Amin)/(Bmax-Bmin)
        chld = int(request.form["children"])
        chld=(chld-Cmin)/(Cmax-Cmin)
        Sex = int(request.form["Sex"])
        Smoker = int(request.form["Smoker"])
        Region = int(request.form["Region"])
        #get prediction
    a=[0,0,0,0]
    a[Region]=1
    final=[age,bmi,chld,Sex,Smoker,*a]
    r=model.predict([final])[0]
    Xr=r*(Xmax-Xmin)+Xmin 
    
    return render_template("out.html", prediction_text='Your predicted annual Healthcare Expense is $ {0:.3f}'.format(Xr))
if __name__ == "__main__":
    app.run(debug=True)
