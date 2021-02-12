from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username,password):
    sql= "SELECT password, id FROM user_account WHERE username=:username"
    result= db.session.execute(sql,{"username":username})
    user=result.fetchone()

    if user==None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"]=user[1]
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username,password):
    hash_value=generate_password_hash(password)
    try:
        sql="INSERT INTO user_account (username,password, created) VALUES (:username,:password,NOW())"
        db.session.execute(sql, {"username":username,"password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username,password)

def user_id():
    return session.get("user_id",0)

def get_users():
    sql="SELECT id, username, is_admin FROM user_account"
    result=db.session.execute(sql)
    return result.fetchall()
    


def get_adminrole():
    user_id= session.get("user_id",0)
    sql="SELECT is_admin FROM user_account WHERE id=:user_id" 
    result= db.session.execute(sql,{"user_id":user_id})
    tulos=result.fetchone()
    try:
        if tulos[0]!=None:
            return True
        else:
            return False
    except:
        return False
       

def set_adminrole(user_account_id):
    try:
        sql="UPDATE user_account SET is_admin=TRUE WHERE id=:user_account_id;"
        db.session.execute(sql, {"user_account_id":user_account_id})
        db.session.commit()
    except:
        return False
    return True

def delete_adminrole(user_account_id):
    try:
        sql="UPDATE user_account SET is_admin=NULL WHERE id=:user_account_id;"
        db.session.execute(sql, {"user_account_id":user_account_id})
        db.session.commit()
    except:
        return False
    return True
