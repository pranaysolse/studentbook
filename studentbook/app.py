from flask import Flask, render_template, request
from forms import RegisterFormSt , RegisterFormte , RegisterFormco , LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='a92cede7a46f3d768a4895932bb47633'



@app.route("/")
def home():
    return render_template("home.html")

#for student
@app.route("/register_s",methods=['GET','POST'])
def register_s():
	form = RegisterFormSt()
	return render_template("register_student.html",title="Register-Student",form=form)

#for teacher
@app.route("/register_t",methods=['GET','POST'])
def register_t():
	form = RegisterFormte()
	return render_template("register_teacher.html",title="Register-Teacher",form=form)

#for committee
@app.route("/register_c",methods=['GET','POST'])
def register_c():
	form = RegisterFormco()
	return render_template("register_committee.html",title="Register-Committee",form=form)

#login for all
@app.route("/login",methods=['GET','POST'])
def login():
	form = LoginForm()
	return render_template("login.html",title="Login",form=form)

if __name__ == '__main__':
	app.run(debug=True)