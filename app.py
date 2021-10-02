from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
 return render_template("index.html")

@app.route('/login',methods = ['POST'])  
def login():  
 uname=request.json
 ans={'outputcode':uname['inputcode']}
 return ans 


app.run(debug=True)