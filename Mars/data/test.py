from requests import get, post
from sqlalchemy import delete

print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/1').json())
print(get('http://localhost:5000/api/v2/users/999').json())
print(get('http://localhost:5000/api/v2/users/q').json())
print(delete('http://localhost:5000/api/v2/users/2').json())
print(delete('http://localhost:5000/api/v2/users/999').json())
print(delete('http://localhost:5000/api/v2/users/qwe').json())
print(post('http://localhost:5000/api/v2/users',json={ "name":"Dan", "surname":"Olegovich", "age":22, "position":"doctor",
           "speciality":"bio", "address":"block_1", "email":'danchik@mail.ru'}).json())
print(post('http://localhost:5000/api/v2/users',json={ "name":"Dan", "surname":"Olegovich"}).json())
