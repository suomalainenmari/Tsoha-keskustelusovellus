from db import db
import users,category

#Hakee viestit
def get_list():
    sql = "SELECT C.category_name, M.messages_subject, M.content, U.username, M.sent_at FROM category C, messages M, user_account U WHERE M.category_id=C.id AND M.user_account_id=U.id ORDER BY M.user_account_id"
    result=db.session.execute(sql)
    return result.fetchall()

#Hakee yksittäisen viestin id:n sisällön perusteella
def get_message_id(message_content):
    sql="SELECT M.id FROM messages M WHERE M.content LIKE :message_content"
    result= db.session.execute(sql,{"message_content":message_content})
    return result.fetchone()

#Hakee viestit joissa tietty kategoria
def get_category_messages(category_id):
    sql = "SELECT M.category_id, M.messages_subject, M.content, M.id, U.username, U.id, M.user_account_id, M.sent_at FROM messages M, user_account U WHERE M.category_id=:category_id AND M.user_account_id=U.id"
    result= db.session.execute(sql,{"category_id":category_id})
    return result.fetchall()

#Hakee viestit jotka kuuluvat tiettyyn viestiketjuun
def get_thread_messages(thread_id):
    sql="SELECT M.messages_subject, M.content, M.id, U.username, U.id, M.sent_at, M.thread_id, M.category_id FROM messages M, user_account U WHERE M.thread_id=:thread_id AND M.user_account_id=U.id"
    result= db.session.execute(sql, {"thread_id":thread_id})
    return result.fetchall()

#Muokkaa viestiä tietokannassa
def modify_message(message_content,message_id):
    try:
        sql="UPDATE messages set content=:message_content where id=:message_id"
        db.session.execute(sql,{"message_content":message_content, "message_id":message_id})
        db.session.commit()
    except:
        return False
    return True

#Poistaa viestin tietokannasta
def delete_message(message_id):
    try:
        sql="DELETE from messages where id=:message_id"
        db.session.execute(sql,{"message_id":message_id})
        db.session.commit()
    except:
        return False
    return True

#Lisää viestin tietokantaan
def send(subject, content,category_id,thread_id):
    user_id=users.user_id()
    if user_id==0:
        return False
    sql = "INSERT INTO messages (messages_subject, content, user_account_id, thread_id, category_id, sent_at) VALUES (:subject, :content, :user_id, :thread_id, :category_id, NOW())"
    db.session.execute(sql, {"subject":subject,"content":content, "user_id":user_id,"thread_id":thread_id,"category_id":category_id})
    db.session.commit()
    return True
