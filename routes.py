from app import app
from flask import redirect, render_template, request, url_for
import messages,users,category,threads


#Homepage routing
@app.route("/home")
def home():
    list=threads.get_list()
    aiheet=category.get_category()
    onkoadmin=users.get_adminrole()
    return render_template("index.html", count=len(list),threads=list, categories=aiheet, adminstatus=onkoadmin) 

#Routes to startingpage
@app.route("/")
def index():
    return render_template("start.html")  


#Route to a category and it's threads
@app.route("/<int:category_id>", methods=["GET","POST"])
def aiheet(category_id):
    onkoadmin=users.get_adminrole()
    aiheen_nimi=category.get_category_name(category_id)
    aiheen_threadit=threads.get_category_threads(category_id)
    if request.method=="GET":
        return render_template("category_threads.html", adminstatus=onkoadmin, count=len(aiheen_threadit), category_threads=aiheen_threadit, category_name=aiheen_nimi[0], category_id=category_id)
        

#Route to a thread and it's messages
@app.route("/<int:category_id>/<int:thread_id>",methods=["GET", "POST"])
def thread(category_id,thread_id):
    onkoadmin=users.get_adminrole()
    aiheen_nimi=category.get_category_name(category_id)
    aloitus_threadi=threads.get_thread(thread_id)
    threadin_viestit=messages.get_thread_messages(thread_id)
    if request.method=="GET":
        return render_template("thread.html", adminstatus=onkoadmin, category_name=aiheen_nimi[0],starting_thread=aloitus_threadi,thread_messages=threadin_viestit)
    if request.method=="POST":
        subject=request.form["subject"]
        content=request.form["content"]
        if messages.send(subject, content, category_id, thread_id):
                return redirect(url_for('thread', category_id=category_id, thread_id=thread_id))
        else:
            return render_template("error.html", message="Failed to respond to a thread. Please try again later.")


#Route to delete a message
@app.route("/<int:category_id>/<int:thread_id>/delete/<int:user_account_id>", methods=["GET","POST"])
def deletemessage(category_id,thread_id,user_account_id):
    onkoadmin=users.get_adminrole()
    aiheen_nimi=category.get_category_name(category_id)
    aloitus_threadi=threads.get_thread(thread_id)
    threadin_viestit=messages.get_thread_messages(thread_id)
    if request.method=="GET":
        return render_template("deletemessages.html", adminstatus=onkoadmin, category_name=aiheen_nimi[0],starting_thread=aloitus_threadi,thread_messages=threadin_viestit, user_account_id=user_account_id )
    if request.method=="POST":
        message_id=request.form["message_id"]
        if messages.delete_message(message_id):
            return redirect(url_for('thread', category_id=category_id, thread_id=thread_id))
        else:
            return render_template("error.html", message="Failed to respond to a thread. Please try again later.")

#Route to modify a message
@app.route("/<int:category_id>/<int:thread_id>/modify/<int:user_account_id>", methods=["GET","POST"])
def modifymessage(category_id,thread_id,user_account_id):
    onkoadmin=users.get_adminrole()
    aiheen_nimi=category.get_category_name(category_id)
    aloitus_threadi=threads.get_thread(thread_id)
    threadin_viestit=messages.get_thread_messages(thread_id)
    if request.method=="GET":
        return render_template("modifymessages.html", adminstatus=onkoadmin, category_name=aiheen_nimi[0],starting_thread=aloitus_threadi,thread_messages=threadin_viestit, user_account_id=user_account_id )
    if request.method=="POST":
        message_id=request.form["message_id"]
        message_content=request.form["viesti"]
        if messages.modify_message(message_content,message_id):
            return redirect(url_for('thread', category_id=category_id, thread_id=thread_id))
        else:
            return render_template("error.html", message="Failed to respond to a thread. Please try again later.")

#Route to creating a new thread
@app.route("/new")
def new():
    aiheet=category.get_category()
    onkoadmin=users.get_adminrole()
    return render_template("new.html", categories=aiheet, adminstatus=onkoadmin)

#Route to searchresults
#@app.route("/searchresults")
#def searchresult():



#Route to user: admin site
@app.route("/supersalainenalue", methods=["GET","POST"])
def supersalainenalue():
    onkoadmin=users.get_adminrole()
    kayttajat=users.get_users()
    if request.method=="GET":
        return render_template("supersalainenalue.html", adminstatus=onkoadmin, users=kayttajat)
    if request.method=="POST":
        user_id=request.form["id"]
        if request.form["action"]=="Remove moderator status":
            if users.delete_adminrole(user_id):
                return redirect("/supersalainenalue")
            else:
                return render_template("error.html", message="Failed to remove moderator status.")

#Route to moderator site
@app.route("/salainenalue", methods=["GET","POST"])
def salainenalue():
    onkoadmin=users.get_adminrole()
    kayttajat=users.get_users()
    if request.method=="GET":
        return render_template("salainenalue.html", adminstatus=onkoadmin, users=kayttajat)
    if request.method=="POST":
        user_id=request.form["id"]
        if request.form["action"]=="Add as a moderator":
            if users.set_adminrole(user_id):
                return redirect("/salainenalue")
            else:
                return render_template("error.html", message="Failed to add moderator status.")

#Route to adding a new category for threads
@app.route("/newcategory", methods=["GET","POST"])
def new_category():
    onkoadmin=users.get_adminrole()
    if request.method=="GET":
        return render_template("newcategory.html", adminstatus=onkoadmin)
    if request.method=="POST":
        aihe = request.form["aihe"]
        user_account_id=users.user_id()
        if category.set_category(aihe,user_account_id):
            return redirect("/home")
        else:
            return render_template("error.html", message="Category already exists.")

#Route to sending a new message
@app.route("/send",methods=["POST"])
def send():
    onkoadmin=users.get_adminrole()
    thread_subject = request.form["subject"]
    starting_message =request.form["content"]
    category_name=request.form["categories"]
    category_id=category.get_category_id(category_name)
    if len(starting_message)<1:
        return render_template("error.html", message="Your message has no content.")
    if len(starting_message)>500:
        return render_template("error.html", message="Your message is too long.")
    if threads.send(thread_subject,starting_message,category_name):
       return redirect(url_for('aiheet', category_id=category_id))
    else:
        return render_template("error.html", message="Failed to create a new thread. Please try again later.")   

#Route to login
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method=="POST":
        username= request.form["username"]
        password=request.form["password"]
        if users.login(username,password):
            return redirect("/home")
        else:
            return render_template("error.html",message="Wrong password or username.")

#Route to logout
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

#Route to register
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        if users.register(username,password):
            return redirect("/home")
        else:
            return render_template("error.html", message="Registration failed. Please try again.")

