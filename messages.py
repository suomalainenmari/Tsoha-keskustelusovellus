from db import db
import users,subjects

def get_list():
    sql = "SELECT M.content, U.username, M.sent_at FROM messages M, users U WHERE M.user_id=U.id ORDER BY M.id"
    result=db.session.execute(sql)
    return result.fetchall()

def get_message_id(message_content):
    sql="SELECT M.id FROM messages M WHERE M.content LIKE :message_content"
    result= db.session.execute(sql,{"message_content":message_content})
    return result.fetchone()

def get_subject_messages(subject_id):
    sql = "SELECT M.content, U.username, M.sent_at FROM messages M, users U WHERE M.subject_id=:subject_id"
    result= db.session.execute(sql,{"subject_id":subject_id})
    return result.fetchall()


def send(content,subject_name):
    user_id=users.user_id()
    subject_id=subjects.get_subject_id(subject_name)
    #subject_id=4
    #subject_id=?? pitää keksiä miten saada aiheen id et voi lisätä tauluun eli
    #pitää myös lisätä alla olevaan SQL komentoon. 
    if user_id==0:
        return False
    sql = "INSERT INTO messages (content, user_id, subject_id, sent_at) VALUES (:content, :user_id, :subject_id, NOW())"
    db.session.execute(sql, {"content":content, "user_id":user_id,"subject_id":subject_id})
    db.session.commit()
    return True
