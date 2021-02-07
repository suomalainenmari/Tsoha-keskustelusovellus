from db import db
import messages,users

from app import app
from flask import redirect, render_template, request
import messages,users,subjects


def set_subject(aihe):
    try:
        sql="INSERT INTO subjects (subject_name) VALUES (:aihe)"
        db.session.execute(sql, {"aihe":aihe})
        db.session.commit()
        return True
    except:
        return False

def get_subjects():
    sql = "SELECT S.subject_name FROM subjects S ORDER BY subject_name"
    result=db.session.execute(sql)
    return result.fetchall()

def get_subject_id(subject_name):

    sql = "SELECT id FROM subjects S WHERE S.subject_name=:subject_name"
    result= db.session.execute(sql,{"subject_name":subject_name})

    tulos=result.fetchone()
    return tulos[0]



