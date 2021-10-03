from flask import Flask, render_template, request
import subprocess
def create_file(code):
    with open("eg1.c","w") as target_file:
        target_file.write(code)

def run_file(file_name):
    application="c:\\MinGW\\bin\\gcc.exe"
    with open("output.txt","w+") as output_file:
        with open("error.txt","w+") as error_file:
            subprocess.run([application,"eg1.c","-o","eg1.exe"],stdout=output_file,stderr=error_file)
            output_file.seek(0)
            error_file.seek(0)
            output=output_file.read()
            error=error_file.read()
    if len(error)>0:return error
    application="eg1.exe"
    with open("output.txt","w+") as output_file:
        with open("error.txt","w+") as error_file:
            subprocess.run([application,"eg1.c","-o","eg1.exe"],stdout=output_file,stderr=error_file)
            output_file.seek(0)
            error_file.seek(0)
            output=output_file.read()
            error=error_file.read()
    if len(output)>0:return output
app=Flask(__name__)

@app.route('/')
def home():
 return render_template("index.html")

@app.route('/login',methods = ['POST'])  
def login(): 
 print(request,type(request)) 
 uname=request.json
 print(uname,type(uname))
 code=uname['inputcode']
 create_file(code)
 output=run_file("eg1.c")
 ans={'outputcode':output}
 return ans 


app.run(debug=True)