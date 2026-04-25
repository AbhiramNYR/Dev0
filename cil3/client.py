import requests

url = 'http://127.0.0.1:5000'

def add_student():
    name = input('Enter name: ')
    roll = input('Enter roll: ')
    res = requests.post(f'{url}/students', json={'name': name, 'roll': roll})
    print(f'Status: {res.status_code}, Response: {res.text}')

def get_students():
    res = requests.get(f'{url}/getstudents')
    print(f'Students List: {res.text}')

add_student()
get_students()