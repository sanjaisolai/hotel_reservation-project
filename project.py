from flask import Flask,redirect,render_template,request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("user_portal.html",details=False)


@app.route('/details',methods=["GET","POST"])
def get_details():
    if request.method=="POST":
            name=request.form["username"]
            number=request.form["number_of_people"]
            email=request.form["email"]
            contact=request.form["contact"]
            time=request.form["time_slot"]
            print(name,number,email,contact,time)
            return render_template("user_portal.html",detail=True)



app.run(debug=True)