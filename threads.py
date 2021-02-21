from db import db
import users,category,routes,messages

#Hakee viestiketjut
def get_list():
    sql = "SELECT C.category_name, U.username, T.thread_subject, T.starting_message, T.created FROM category C, user_account U, threads T WHERE T.category_id=C.id AND t.user_account_id=u.id ORDER BY T.created DESC"
    result=db.session.execute(sql)
    return result.fetchall()

#Hakee viestiketjun id:n aiheen nimen perusteella
def get_thread_id(thread_subject):
    sql="SELECT T.id FROM threads T WHERE T.thread_subject LIKE :thread_subject"
    result= db.session.execute(sql,{"message_content":thread_subject})
    return result.fetchone()

#Hakee yksittäisen ketjun tiedot id:n perusteella
def get_thread(thread_id):
    sql="SELECT t.id, t.thread_subject, t.starting_message, t.created, u.username, u.id, t.category_id from threads T, user_account U WHERE t.id=:thread_id AND t.user_account_id=u.id"
    result=db.session.execute(sql,{"thread_id":thread_id})
    return result.fetchone()

#Hakee tiettyyn kategoriaan liittyvät viestiketjut
def get_category_threads(category_id):
    sql = "SELECT T.category_id, T.thread_subject, T.starting_message, T.id, U.username, U.id, T.created FROM threads T, user_account U WHERE T.category_id=:category_id AND T.user_account_id=U.id ORDER BY T.created DESC"
    result= db.session.execute(sql,{"category_id":category_id})
    return result.fetchall()

#Lisää uuden kategorian tietokantaan
def send(thread_subject, starting_message,category_name):
    category_id=category.get_category_id(category_name)
    user_id=users.user_id()
    if user_id==0:
        return False
    sql = "INSERT INTO threads (thread_subject, starting_message, category_id, user_account_id, created) VALUES (:thread_subject, :starting_message, :category_id, :user_account_id, NOW())"
    db.session.execute(sql, {"thread_subject":thread_subject, "starting_message":starting_message, "category_id":category_id, "user_account_id":user_id})
    db.session.commit()
    return True
