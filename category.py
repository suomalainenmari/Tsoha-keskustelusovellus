from db import db
import messages,users

from app import app
from flask import redirect, render_template, request
import messages,users,category

#Lisää kategorian tietokantaan
def set_category(aihe,user_account_id):
    try:
        sql="INSERT INTO category (category_name, creator, created) VALUES (:aihe, :user_account_id, NOW())"
        db.session.execute(sql, {"aihe":aihe, "user_account_id":user_account_id})
        db.session.commit()
        return True
    except:
        return False

#Hakee kategorioiden perustiedot tietokannasta
def get_category():
    sql = "SELECT id,category_name FROM category ORDER BY category_name"
    result=db.session.execute(sql)
    return result.fetchall()

#Hakee kategorian nimen id:n perusteella
def get_category_name(category_id):
    sql="SELECT category_name FROM category WHERE id=:category_id"
    result=db.session.execute(sql,{"category_id":category_id})
    return result.fetchone()

#Hakee kategorian id:n nimen perusteella
def get_category_id(category_name):
    sql = "SELECT id FROM category WHERE category_name=:category_name"
    result= db.session.execute(sql,{"category_name":category_name})
    tulos=result.fetchone()
    return tulos[0]



