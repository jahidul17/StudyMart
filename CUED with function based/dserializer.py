import requests
import json

URL="http://127.0.0.1:8000/aicreate/"

data={
    'teacher_name':'Nikola',
    'course_name':'Machine Learning',
    'course_duration':2,
    'seat':25,
    
}

json_data = json.dumps(data)
re = requests.post(url=URL,data=json_data)
data = re.json()
print(data)