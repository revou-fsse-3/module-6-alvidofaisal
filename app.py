from flask import Flask, jsonify, request
from models import animals, employees, feedings, visitors, revenue

app = Flask(__name__) 


# API endpoints
@app.route('/')
def welcome():
    return 'Welcome to Zoo Manager!'


################ Animals API Endpoints ##################

## Retrieve All Animals
@app.route('/animals', methods=['GET']) 
def get_animals():
    return jsonify(animals)

## Retrieve a Specific Animal by ID
@app.route('/animals/<int:id>', methods=['GET'])
def get_animal(id):
    animal = next((a for a in animals if a.get('id') == id), None)
    return jsonify(animal) if animal else ('', 404)

## Add a New Animal
@app.route('/animals', methods=['POST'])
def add_animal():
    new_animal = request.json
    new_id = len(animals) + 1  # Assign a new ID
    new_animal['id'] = new_id  # Add the ID to the animal's data
    animals.append(new_animal)
    return jsonify(new_animal), 201


## Update an Existing Animal
@app.route('/animals/<int:id>', methods=['PUT'])
def update_animal(id):
    animal = next((a for a in animals if a.get('id') == id), None)
    if not animal: 
        return jsonify({'error': 'Animal not found'}), 404 
    
    animal_update = request.json
    for key in animal_update:
        if key in animal:
            animal[key] = animal_update[key]
    return jsonify(animal)

## Remove an Animal
@app.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    global animals
    animal = next((a for a in animals if a.get('id') == id), None)
    if not animal:
        return jsonify({'error': 'Animal not found'}), 404  

    animals = [a for a in animals if a.get('id') != id]
    return '', 204    

################ Employee API Endpoints ##################

## Retrieve All Employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

## Retrieve a Specific Employee by ID
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = next((e for e in employees if e.get('id') == id), None)
    return jsonify(employee) if employee else ('', 404)

## Add New Employee
@app.route('/employees', methods=['POST'])
def add_employee():
    new_employee = request.json
    employees.append(new_employee)
    return jsonify(new_employee), 201

## Update an Existing Employee
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = next((e for e in employees if e.get('id') == id), None)
    if not employee: 
        return jsonify({'error': 'Employee not found'}), 404  # Return 404 if not found

    employee_update = request.json
    for key in employee_update:
        if key in employee:
            employee[key] = employee_update[key]
    return jsonify(employee)

## Remove an Employeee
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    global employees
    employee = next((e for e in employees if e.get('id') == id), None)
    if not employee:
        return jsonify({'error': 'Employee not found'}), 404  

    employees = [e for e in employees if e.get('id') != id]
    return '', 204
    

################ Feedings API Endpoints ##################

## Retrieve All Feeding Schedules
@app.route('/feedings', methods=['GET'])
def get_feedings():
    return jsonify(feedings)

## Retrieve a Specific Feeding Schedule by ID
@app.route('/feedings/<int:id>', methods=['GET'])
def get_feeding(id):
    feeding = next((f for f in feedings if f.get('id') == id), None)
    return jsonify(feeding) if feeding else ('', 404)

## Add a New Feeding Schedule
@app.route('/feedings', methods=['POST'])
def add_feeding():
    new_feeding = request.json
    feedings.append(new_feeding)
    return jsonify(new_feeding), 201

## Update an Existing Feeding Schedule
@app.route('/feedings/<int:id>', methods=['PUT'])
def update_feeding(id):
    feeding = next((f for f in feedings if f.get('id') == id), None)
    if not feeding:
        return '', 404
    feeding_update = request.json
    for key in feeding_update:
        if key in feeding:
            feeding[key] = feeding_update[key]
    return jsonify(feeding)

## Remove a Feeding Schedule
@app.route('/feedings/<int:id>', methods=['DELETE'])
def delete_feeding(id):
    global feedings
    feeding = next((f for f in feedings if f.get('id') == id), None)
    if not feeding:
        return jsonify({'error': 'Feeding schedule not found'}), 404
    
    feedings = [f for f in feedings if f.get('id') != id]
    return '', 204



################ Reporting API Endpoints ##################

## Animal Report
@app.route('/reports/animals', methods=['GET'])
def get_animal_report():
    report = {}
    for animal in animals:
        key = f"{animal['species']}-{animal['gender']}-{animal['special_requirements']}"
        if key not in report:
            report[key] = 0
        report[key] += 1
    return jsonify(report)

## Visitors Report
@app.route('/reports/visitors', methods=['GET'])
def get_visitor_report():
    report = {}
    for visitor in visitors:
        key = f"{visitor['type']}-{visitor['date']}-{visitor['feedback']}"
        if key not in report:
            report[key] = 0
        report[key] += 1
    return jsonify(report)

@app.route('/reports/revenue', methods=['GET'])
def get_revenue_report():
    report = {}
    for entry in revenue:
        key = f"{entry['ticket_type']}-{entry['event_type']}-{entry['date']}"
        if key not in report:
            report[key] = 0
        report[key] += int(entry['amount'])
    return jsonify(report)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 
