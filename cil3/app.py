from flask import Flask, jsonify, request

app = Flask(__name__)
students = {}
int_id = 1

@app.route('/getstudents', methods=['GET'])
def get_students():
    return jsonify(list(students.values()))

@app.route('/students', methods=['POST'])
def add_students():
    global int_id
    data = request.get_json()
    students[int_id] = {'id': int_id, 'name': data['name'], 'roll': data['roll']}
    int_id += 1
    return jsonify(students)

@app.route('/delete', methods=['POST'])
def delete_students():
    data = request.get_json()
    students.pop(data['id'], None)
    return jsonify({'status': 'deleted'})

if __name__ == '__main__':
    app.run(port=5000)