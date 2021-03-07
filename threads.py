from db import db
import users,category,routes,messages

#Returns all threads
def get_list():
    sql = "SELECT C.category_name, U.username, T.thread_subject, T.starting_message, T.created, c.id, t.id FROM category C, user_account U, threads T WHERE T.category_id=C.id AND t.user_account_id=u.id ORDER BY T.created DESC"
    result=db.session.execute(sql)
    return result.fetchall()

#Return the id of a thread based on category name
def get_thread_id(thread_subject):
    sql="SELECT T.id FROM threads T WHERE T.thread_subject LIKE :thread_subject"
    result= db.session.execute(sql,{"message_content":thread_subject})
    return result.fetchone()

#Returns one thread based on id 
def get_thread(thread_id):
    sql="SELECT t.id, t.thread_subject, t.starting_message, t.created, u.username, u.id, t.category_id from threads T, user_account U WHERE t.id=:thread_id AND t.user_account_id=u.id"
    result=db.session.execute(sql,{"thread_id":thread_id})
    return result.fetchone()

#Returns threads of choesn catagory
def get_category_threads(category_id):
    sql = "SELECT T.category_id, T.thread_subject, T.starting_message, T.id, U.username, U.id, T.created FROM threads T, user_account U WHERE T.category_id=:category_id AND T.user_account_id=U.id ORDER BY T.created DESC"
    result= db.session.execute(sql,{"category_id":category_id})
    return result.fetchall()

#Adds a new thread to database
def send(thread_subject, starting_message,category_name):
    category_id=category.get_category_id(category_name)
    user_id=users.user_id()
    if user_id==0:
        return False
    sql = "INSERT INTO threads (thread_subject, starting_message, category_id, user_account_id, created) VALUES (:thread_subject, :starting_message, :category_id, :user_account_id, NOW())"
    db.session.execute(sql, {"thread_subject":thread_subject, "starting_message":starting_message, "category_id":category_id, "user_account_id":user_id})
    db.session.commit()
    return True


#Returns threads where starting message is like condition
def searchthreads (content):
  sql= "SELECT t.id, t.thread_subject, t.starting_message, t.created, c.category_name, c.id from threads T, category C where T.starting_message LIKE :content AND t.category_id=c.id"
  result= db.session.execute(sql, {"content":"%"+content+"%"})
  return result.fetchall()


#Returns threads where the heading of the thread is like condition
def searchthreads_subject(content):
  sql= "SELECT t.id, t.thread_subject, t.starting_message, t.created, c.category_name, c.id from threads T, category C where T.thread_subject LIKE :content AND t.category_id=c.id"
  result= db.session.execute(sql, {"content":"%"+content+"%"})
  return result.fetchall()

#Deletes a thread and all of it's messages based on id
def delete_thread(thread_id):
  sql="DELETE FROM THREADS WHERE id=:thread_id"
  db.session.execute(sql, {"thread_id":thread_id})
  db.session.commit()
  return True

def modify_thread(thread_content,thread_id):
      try:
        sql="UPDATE threads set starting_message=:thread_content where id=:thread_id"
        db.session.execute(sql,{"thread_content":thread_content, "thread_id":thread_id})
        db.session.commit()
      except:
        return False
      return True

