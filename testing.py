import requests
mydata = {'id':6,'adm_no':'AE130','first_name':'aswanth','last_name':'appu','class_id':2,'parant_id':23}
update_data = {'first_name':'Abhinav','last_name':'C'}
student = {'id':6}
result = requests.put('http://127.0.0.1:5000/student',json=mydata)

print(result.text)