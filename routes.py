from app import app
from flask import redirect, render_template, request
import messages,users,category


@app.route("/")
def index():
    list=messages.get_list()
    aiheet=category.get_category()
    onkoadmin=users.get_adminrole()
    return render_template("index.html", count=len(list),messages=list, categories=aiheet, adminstatus=onkoadmin)  

@app.route("/<int:id>", methods=["GET","POST"])
def aiheet(id):
    aiheen_id=id
    aiheen_nimi=category.get_category_name(aiheen_id)
    aiheenviestit=messages.get_category_messages(aiheen_id)
    viestin_id=messages.get_message_id("Aihe vapaa")
    if request.method=="GET":
        return render_template("category_messages.html", count=len(aiheenviestit), category_messages=aiheenviestit, category_name=aiheen_nimi[0], message_id=viestin_id)
        #return render_template("error.html")


@app.route("/Aihevapaa/None",methods=["GET"])
def thread():
    return render_template("thread.html")

@app.route("/new")
def new():
    aiheet=category.get_category()
    return render_template("new.html", categories=aiheet)

@app.route("/supersalainenalue", methods=["GET","POST"])
def supersalainenalue():
    onkoadmin=users.get_adminrole()
    kayttajat=users.get_users()
    if request.method=="GET":
        return render_template("supersalainenalue.html", adminstatus=onkoadmin, users=kayttajat)
    if request.method=="POST":
        user_id=request.form["id"]
        if request.form["action"]=="Poista moderointioikeus":
            if users.delete_adminrole(user_id):
                return redirect("/supersalainenalue")
            else:
                return render_template("error.html", message="Käyttöoikeuden poisto ei onnistunut.")

@app.route("/salainenalue", methods=["GET","POST"])
def salainenalue():
    onkoadmin=users.get_adminrole()
    kayttajat=users.get_users()
    if request.method=="GET":
        return render_template("salainenalue.html", adminstatus=onkoadmin, users=kayttajat)
    if request.method=="POST":
        user_id=request.form["id"]
        if request.form["action"]=="Lisää moderaattoriksi":
            if users.set_adminrole(user_id):
                return redirect("/salainenalue")
            else:
                return render_template("error.html", message="Käyttöoikeuden lisäys ei onnistunut.")




@app.route("/newcategory", methods=["GET","POST"])
def new_category():
    onkoadmin=users.get_adminrole()
    if request.method=="GET":
        return render_template("newcategory.html", adminstatus=onkoadmin)
    if request.method=="POST":
        aihe = request.form["aihe"]
        user_account_id=users.user_id()
        if category.set_category(aihe,user_account_id):
            return redirect("/")
        else:
            return render_template("error.html", message="Keskusteluaihe on jo olemassa.")

@app.route("/send",methods=["POST"])
def send():
    subject = request.form["subject"]
    content =request.form["content"]
    category_name=request.form["categories"]
    if len(content)<1:
        return render_template("error.html", message="Viestissä ei ole sisältöä.")
    if len(content)>5000:
        return render_template("error.html", message="Viesti on liian pitkä.")
    if messages.send(subject,content,category_name):
        return redirect("/")
        #return render_template("error.html", message=category_name)
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

