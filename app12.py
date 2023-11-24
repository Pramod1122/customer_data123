from flask import Flask,jsonify,render_template,request
import pickle
app=Flask(__name__)

@app.route("/")
def index():
    print("Welcome to customer Project")
    return render_template("index.html")

@app.route("/predict12",methods=["GET"])
def customer_data():
  
    with open("customer_data11.pkl","rb")as f:
        ml_model=pickle.load(f)


    data=request.args.get("name")
    print("DATA IS >>",data)
        
    CustomerID= eval(data["CustomerID"])
    Genre= eval(data["Genre"])
    Age= eval(data["Age"])
    Annual_Income= eval(data["Annual_Income"])
    
    result=ml_model.predict([[CustomerID,Genre,Age,Annual_Income]])
    
    return jsonify({"conclusion":f"The predicted score of customer is {result}"})

if __name__=='__main__':
    app.run(port=1995,debug=True)