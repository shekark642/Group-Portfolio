# https://flask.palletsprojects.com/en/1.1.x/api/
import data
from flask import Flask, render_template, request, redirect
from data import board
#create a Flask instance
app = Flask(__name__)


#connects default URL of server to a python function
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/Login")#for the pritn chess board from dictonaries
def Login():
    return render_template("Login.html", board=board)

@app.route("/index")#for the dragable chess file
def index():
    return render_template("index.html", display="")

@app.route("/add", methods=['GET','POST'],)#for the dragable chess file
def addition():
    if request.method == 'POST':
        form = request.form
        numberOne = int(form['numOne'])
        numberTwo = int(form['numTwo'])
        calc = numberOne + numberTwo
        return render_template("index.html", your_list = data.answersdata(calc))#data.playlist()

    return redirect("/index")

@app.route("/journals")#for storing all the links to the webpage
def journals():
  return render_template("journals.html",repl="repl of website", website ="link to personal website")#allows to define the text that is hyperlinked on the the personal journals

@app.route("/every")
def all_route():
    return render_template("taskall.html", datalist=data.alldata())


if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)