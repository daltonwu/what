from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        query = request.form['query']
        return render_template("home.html", answer = query)

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "whatever"
    app.run(host='0.0.0.0',port=8000)
            
