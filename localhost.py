from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def land():
    return render_template('landing.html')

@app.route("/css")
def style():
    return render_template("style.css")

@app.route("/js")
def js():
    return render_template("main.js")
    
app.run(debug=True)
