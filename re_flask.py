import requests
from flask import *
app=Flask(__name__)
@app.route('/')
def House():
    print("This is Home Page")
@app.route('/about')
def sing():
    return redirect('login.html')
    email=request.form.get('email')
    name=request.form.get('password')
    if email=='satya@gmail.com' and name=='1234':
        return 'Welcome'
@app.route('/home')
def homee():
    return redirect('/home/about')
if __name__=="__main__":
    app.run(debug=True)