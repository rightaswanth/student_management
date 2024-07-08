from flask import ( Flask,jsonify,
                   render_template,Blueprint,request)
import sqlite3
import json
from flaskapp.db import get_db,close_db

bp = Blueprint('student',__name__)

@bp.route('/school')
def school():
    return "You can add and get details"

@bp.route('/student',methods=('POST','GET'))
def admission():
    conn = get_db()
    if request.method == 'POST':
        data = request.get_json()
        conn.execute('INSERT INTO student (id,adm_no,first_name,last_name,class_id,parant_id)'
                   'VALUES (?,?,?,?,?,?)',(data['id'],data['adm_no'],data['first_name'],data['last_name'],
                    data['class_id'],data['parant_id'])
                    )
        conn.commit()
        return f"Succesfully Added the student"
    
    all_data = conn.execute('SELECT * FROM student').fetchall()
    student_data = [dict(row) for row in all_data]
    return jsonify(student_data)

@bp.route('/student',methods=['PATCH'])
def update_data():

    conn = get_db()
    data = request.get_json()
    conn.execute('UPDATE student SET first_name = ?,last_name=?',(data['first_name'],data['last_name']))
    conn.commit()
    return "Succesfully Updated the student data"
        
@bp.route('/student',methods=['PUT'])
def fully_update_data():
    conn = get_db()
    data = request.get_json()
    conn.execute('UPDATE student SET id = ?,adm_no=?,first_name=?,last_name=?,class_id=?,parant_id=? WHERE id = ?'
                 ,(data['id'],data['adm_no'],data['first_name'],data['last_name'],data['class_id'],data['parant_id'],data['id'])
                 )
    conn.commit()
    return "Succesfully updated student data"
    

@bp.route('/student',methods=['DELETE'])
def delete_student():
    conn = get_db()
    data = request.get_json()
    conn.execute('DELETE FROM student WHERE id = ?',(data['id'],)) 
    conn.commit()  
    return "Succesfully Deleted the student"





