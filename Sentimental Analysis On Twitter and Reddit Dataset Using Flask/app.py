from flask import Flask,render_template,request
import pickle


app=Flask(__name__)

model=pickle.load(open('model.pkl','rb'))
dd
#vec=pickle.load(open('TFIDF.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])



def predict():
    if request.method == 'POST':
        text = str(request.form["text"])
        text=transform(text)
        #prediction = model.predict(input_cols)
        
        t_matrix=vec.transform(text)
        result=mod5.predict(t_matrix).mean()
        if result> 0:
            result=1
        elif result== 0:
            result=0
        else:
            result=-1
        return render_template("out.html", result = result, text = text)
   
if __name__ == "__main__":
  app.debug = True
  app.run()

