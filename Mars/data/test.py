from requests import get, post
import datetime

print(get('http://localhost:5000/api/jobs').json())
print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1,
                 'job': 'Это работа',
                 'work_size': 15,
                 # 'start_date': datetime.datetime.now(),
                 # 'end_date': datetime.datetime.now(),
                 'collaborators': '2,3',
                 'is_finished': False}).json())
print(get('http://localhost:5000/api/jobs').json())