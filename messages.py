from db import db
import users,category

def get_list():
    sql = "SELECT C.category_name, M.messages_subject, M.content, U.username, M.sent_at FROM category C, messages M, user_account U WHERE M.category_id=C.id AND M.user_account_id=U.id ORDER BY M.user_account_id"
    result=db.session.execute(sql)
    return result.fetchall()

def get_message_id(message_content):
    sql="SELECT M.id FROM messages M WHERE M.content LIKE :message_content"
    result= db.session.execute(sql,{"message_content":message_content})
    return result.fetchone()

def get_category_messages(category_id):
    sql = "SELECT M.category_id, M.messages_subject, M.content, U.username, U.id, M.user_account_id, M.sent_at FROM messages M, user_account U WHERE M.category_id=:category_id AND M.user_account_id=U.id"
    result= db.session.execute(sql,{"category_id":category_id})
    return result.fetchall()


def send(subject, content,category_name):
    user_id=users.user_id()
    category_id=category.get_category_id(category_name)
    #category_id=4
    #category_id=?? pitää keksiä miten saada aiheen id et voi lisätä tauluun eli
    #pitää myös lisätä alla olevaan SQL komentoon. 
    if user_id==0:
        return False
    sql = "INSERT INTO messages (messages_subject, content, user_account_id, category_id, sent_at) VALUES (:subject, :content, :user_id, :category_id, NOW())"
    db.session.execute(sql, {"subject":subject,"content":content, "user_id":user_id,"category_id":category_id})
    db.session.commit()
    return True
