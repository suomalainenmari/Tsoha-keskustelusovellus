from app import app
from flask import redirect, render_template, request
import messages,users,subjects


@app.route("/")
def index():
    list=messages.get_list()
    aiheet=subjects.get_subjects()
    return render_template("index.html", count=len(list),messages=list, subjects=aiheet, kokolista=aiheet) 

@app.route("/<Aihevapaa>", methods=["GET","POST"])
def aiheet(Aihevapaa):
    aiheen_nimi="Aihe vapaa"
    aiheen_id=subjects.get_subject_id(aiheen_nimi)
    aiheenviestit=messages.get_subject_messages(aiheen_id)
    viestin_id=messages.get_message_id("Aihe vapaa")
    if request.method=="GET":
        return render_template("subject_messages.html", count=len(aiheenviestit), subject_messages=aiheenviestit, subject_name=aiheen_nimi, message_id=viestin_id)

@app.route("/Aihevapaa/None",methods=["GET"])
def thread():
    return render_template("thread.html")

@app.route("/new")
def new():
    aiheet=subjects.get_subjects()
    return render_template("new.html", subjects=aiheet)

@app.route("/newsubject", methods=["GET","POST"])
def new_subject():
    if request.method=="GET":
        return render_template("newsubject.html")
    if request.method=="POST":
        aihe = request.form["aihe"]
        if subjects.set_subject(aihe):
            return redirect("/")
        else:
            return render_template("error.html", message="Keskusteluaihe on jo olemassa.")

@app.route("/send",methods=["POST"])
def send():
    content =request.form["content"]
    subject_name=request.form["subjects"]
    if len(content)<1:
        return render_template("error.html", message="Viestissä ei ole sisältöä.")
    if len(content)>5000:
        return render_template("error.html", message="Viesti on liian pitkä.")
    if messages.send(content,subject_name):
        return redirect("/")
        #return render_template("error.html", message=subject_name)
    else:
        return render_template("error.html", message="Viestin lähetys epäonnistui.")   

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method=="POST":
        username= request.form["username"]
        password=request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä käyttäjätunnus tai salasana.")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

