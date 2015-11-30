from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        query = request.form['query']
        answers = utils.answer(query)
        return render_template("answer.html", answers = answers, query=query)

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "whatever"
    app.run(host='0.0.0.0',port=8000)
            
