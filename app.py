from flask import Flask, redirect, render_template, request
import json

users = [{"user": "rotem", "pass": "12345"},{"user": "leon", "pass": "12345"}]
MY_DATA = 'users.txt' # new
app = Flask(__name__)

ary = ['rotem','leon']

def save_2_file(): # new
    with open(MY_DATA, 'w') as filehandle:
        json.dump(users, filehandle)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login" , methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        if user == "rotem" or "leon" and pwd == "12345": 
            return render_template("succes.html",new_user=user)
    return render_template("login.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")




@app.route("/register" , methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        mail= request.form["mail"]
        nick= request.form["nick"]
        users.append({"user": user, "pwd": pwd , "mail": mail , "nick":nick})
        save_2_file()
        return render_template("succes.html", new_user=user)
    return render_template("register.html")

    #     if user == "rotem"  and pwd == "12345" and mail == "rotem@" and nick == "roshem" :         
    #         return redirect("succes.html")
    # return render_template("index.html")



if __name__ == "_main_":
    app.run(debug=True)