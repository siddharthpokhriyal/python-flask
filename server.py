from flask import redirect,url_for,request,Flask
app=Flask(__name__)
@app.route('/pass/<name>')
def passs(name):
    return "Welcome %s" %name
@app.route("/login",method=['POST','GET',]) 
def login():
    if request.method=='POST':
        user=request.form['nm']
        return redirect(url_for('pass',name=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('pass',name=user))
if __name__ == "__main__":
    app.run(debug=True)