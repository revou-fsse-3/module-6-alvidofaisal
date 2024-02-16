import unittest
from app import app
from flask import json

class FlaskTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Reset data to its original state
        global animals, employees, feedings, visitors, revenue
        # Animals data
        animals = [
            # Lion
            {
                'id': 1,
                'species': 'Lion',
                'age': 10,
                'gender': 'Male',
                'special_requirements': 'Meat diet'
            },
            # Giraffe
            {
                'id': 2,
                'species': 'Giraffe',
                'age': 18,
                'gender': 'Male',
                'special_requirements': 'Vegetarian diet'
            },
            # Hippo
            {
                'id': 3,
                'species': 'Hippo',
                'age': 27,
                'gender': 'Female',
                'special_requirements': 'Vegetarian diet'
            },
            # Penguin
            {
                'id': 4,
                'species': 'Penguin',
                'age': 12,
                'gender': 'Male',
                'special_requirements': 'Fish diet'
            },
            # Zebra
            {
                'id': 5,
                'species': 'Zebra',
                'age': 25,
                'gender': 'Male',
                'special_requirements': 'Vegetarian diet'
            },
        ]

        # Employees data
        employees = [
            {    
                'id': 1,
                'name': 'Agus',
                'email': 'agus@rafp.com',
                'phone_number': '',
                'role': 'Zookeeper',
                'schedule': '9 AM - 5 PM'
            },
            {    
                'id': 2,
                'name': 'Faisal',
                'email': 'dwi@rafp.com',
                'phone_number': '',
                'role': 'Zookeeper',
                'schedule': '5 PM - 1 AM'
            },
            {    
                'id': 3,
                'name': 'Eko',
                'email': 'Eko@rafp.com',
                'phone_number': '',
                'role': 'Zookeeper',
                'schedule': '1 AM - 9 AM'
            },
            {    
                'id': 4,
                'name': 'Siti',
                'email': 'siti@rafp.com',
                'phone_number': '',
                'role': 'Guest Service Agent',
                'schedule': '9 AM - 5 PM'
            },
            {    
                'id': 5,
                'name': 'Dewi',
                'email': 'dewi@rafp.com',
                'phone_number': '',
                'role': 'Zoo Tour Guide',
                'schedule': '9 AM - 5 PM'
            },
            {    
                'id': 6,
                'name': 'Putri',
                'email': 'putri@rafp.com',
                'phone_number': '',
                'role': 'Veterinarian',
                'schedule': '9 AM - 5 PM'
            },
        ]

        # Feeding Schedules
        feedings = [
            # Lion 
            {    
                'id': 1,
                'animal_id': 1,
                'enclosure_id': 101,
                'food_type': 'Meat',
                'feeding_time': '2 PM' 
            },
            # Giraffe 
            {    
                'id': 2,
                'animal_id': 2,
                'enclosure_id': 102,
                'food_type': 'Vegetables',
                'feeding_time': '10:45 AM'
            },
            {    
                'id': 3,
                'animal_id': 2,
                'enclosure_id': 102,
                'food_type': 'Vegetables',
                'feeding_time': '1:50 PM'
            },
            {    
                'id': 4,
                'animal_id': 2,
                'enclosure_id': 102,
                'food_type': 'Vegetables',
                'feeding_time': '3:45 PM'
            },
            # Hippo 
            {    
                'id': 5,
                'animal_id': 3,
                'enclosure_id': 103,
                'food_type': 'Vegetables',
                'feeding_time': '2 PM'
            },
            # Penguin 
            {    
                'id': 6,
                'animal_id': 4,
                'enclosure_id': 104,
                'food_type': 'Fish',
                'feeding_time': '10:30 AM'
            },
            {    
                'id': 7,
                'animal_id': 4,
                'enclosure_id': 104,
                'food_type': 'Fish',
                'feeding_time': '2:30 PM'
            },
            # Zebra
            {    
                'id': 8,
                'animal_id': 5,
                'enclosure_id': 105,
                'food_type': 'Vegetables',
                'feeding_time': '10:15 AM'
            },
            {    
                'id': 9,
                'animal_id': 5,
                'enclosure_id': 105,
                'food_type': 'Vegetables',
                'feeding_time': '2:15 PM'
            }
        ]

        # Visitors data
        visitors = [
            {'id': 1, 'type': 'Adult', 'date': '2024-02-10', 'feedback': 'Positive'},
            {'id': 2, 'type': 'Child', 'date': '2024-02-11', 'feedback': 'Positive'},
            {'id': 3, 'type': 'Adult', 'date': '2024-02-11', 'feedback': 'Negative'},
            {'id': 4, 'type': 'Adult', 'date': '2024-02-12', 'feedback': 'Positive'},
            {'id': 5, 'type': 'Child', 'date': '2024-02-13', 'feedback': 'Positive'},
            {'id': 6, 'type': 'Adult', 'date': '2024-02-13', 'feedback': 'Negative'},
            {'id': 7, 'type': 'Adult', 'date': '2024-02-14', 'feedback': 'Positive'},
            {'id': 8, 'type': 'Child', 'date': '2024-02-17', 'feedback': 'Positive'},
            {'id': 9, 'type': 'Adult', 'date': '2024-02-17', 'feedback': 'Negative'},
            {'id': 10, 'type': 'Adult', 'date': '2024-02-17', 'feedback': 'Negative'},
        ]

        # Revenue data 
        revenue = [
            {'id': 1, 'ticket_type': 'Adult', 'event_type': 'Regular', 'date': '2024-02-10', 'amount': '100000'},
            {'id': 2, 'ticket_type': 'Child', 'event_type': 'Regular', 'date': '2024-02-11', 'amount': '75000'},
            {'id': 3, 'ticket_type': 'Adult', 'event_type': 'Special Event', 'date': '2024-02-12', 'amount': '150000'},
            {'id': 4, 'ticket_type': 'Adult', 'event_type': 'Special Event', 'date': '2024-02-12', 'amount': '150000'},
            {'id': 5, 'ticket_type': 'Child', 'event_type': 'Regular', 'date': '2024-02-13', 'amount': '75000'},
            {'id': 6, 'ticket_type': 'Adult', 'event_type': 'Regular', 'date': '2024-02-13', 'amount': '100000'},
            {'id': 7, 'ticket_type': 'Adult', 'event_type': 'Special Event', 'date': '2024-02-14', 'amount': '150000'},
            {'id': 8, 'ticket_type': 'Child', 'event_type': 'Regular', 'date': '2024-02-17', 'amount': '75000'},
            {'id': 9, 'ticket_type': 'Adult', 'event_type': 'Regular', 'date': '2024-02-17', 'amount': '100000'},
            {'id': 10, 'ticket_type': 'Adult', 'event_type': 'Regular', 'date': '2024-02-17', 'amount': '100000'},
        ]

    # API Endpoint Tests

    ################# Animals #################

    ## Test GET all animals
    def test_get_all_animals(self):       
        response = self.app.get('/animals', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    ## Test POST new animal
    def test_post_animal(self):    
        response = self.app.post('/animals', json={
            'species': 'Elephant', 
            'age': 10,
            'gender': 'Female',
            'special_requirements': 'Vegetarian Diet'
            })
        self.assertEqual(response.status_code, 201)

    ## Test PUT update existing animal
    def test_put_animal_valid_id(self):
        
    # First create a new animal
        post_response = self.app.post('/animals', json={
            'species': 'Tiger', 
            'age': 5,
            'gender': 'Female',
            'special_requirements': 'Meat Diet'
        })
        new_animal_id = json.loads(post_response.data)['id']

        # Now update the newly created animal
        put_response = self.app.put(f'/animals/{new_animal_id}', json={"species": "Updated Tiger"})
        self.assertEqual(put_response.status_code, 200)


    def test_put_animal_invalid_id(self):
        response = self.app.put('/animals/999', json={"species": "Updated Species"})
        self.assertEqual(response.status_code, 404)

    ## Test DELETE an animal
    def test_delete_animal_valid_id(self):
        response = self.app.delete('/animals/1')
        self.assertEqual(response.status_code, 204)

    def test_delete_animal_invalid_id(self):
        response = self.app.delete('/animals/999')
        self.assertEqual(response.status_code, 404)

    ################# Employees #################

    ## Test GET employees
    def test_get_all_employees(self):
        response = self.app.get('/employees')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    ## Test GET a specific employee
    def test_get_employee_valid_id(self):
        # Assuming an employee with id 1 exists
        response = self.app.get('/employees/2')
        self.assertEqual(response.status_code, 200)

    def test_get_employee_invalid_id(self):
        response = self.app.get('/employees/999') 
        self.assertEqual(response.status_code, 404)

    ## Test POST add new employee
    def test_post_employee(self):
        new_employee = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone_number": "123456789",
            "role": "Zookeeper",
            "schedule": "9 AM - 5 PM"
        }
        response = self.app.post('/employees', json=new_employee)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['name'], "John Doe")

    ## Test PUT Update an existing employee
    def test_put_employee_valid_id(self):
        update_data = {"name": "Jane Doe"}
        response = self.app.put('/employees/2', json=update_data) 
        self.assertEqual(response.status_code, 200)

    def test_put_employee_invalid_id(self):
        update_data = {"name": "Jane Doe"}
        response = self.app.put('/employees/999', json=update_data) 
        self.assertEqual(response.status_code, 404)
    
    ## Test DELETE remove an employee
    def test_delete_employee_valid_id(self):
        response = self.app.delete('/employees/1') 
        self.assertEqual(response.status_code, 204)

    def test_delete_employee_invalid_id(self):
        response = self.app.delete('/employees/999') 
        self.assertEqual(response.status_code, 404)

    ################# Feedings #################
    
    ## Test GET all feeding schedules
    def test_get_all_feedings(self):
        response = self.app.get('/feedings')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)
    
    ## Test GET a specific feeding schedule
    def test_get_feeding_valid_id(self):
        response = self.app.get('/feedings/2')
        self.assertEqual(response.status_code, 200)

    def test_get_feeding_invalid_id(self):
        response = self.app.get('/feedings/999') 
        self.assertEqual(response.status_code, 404)
    
    ## Test POST add new feeding schedule
    def test_post_feeding(self):
        new_feeding = {
            "animal_id": 1,
            "enclosure_id": 101,
            "food_type": "Meat",
            "feeding_time": "9 AM"
        }
        response = self.app.post('/feedings', json=new_feeding)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['food_type'], "Meat")
    
    ## Test PUT update existing feeding schedule
    def test_put_feeding_valid_id(self):
        update_data = {"feeding_time": "3 PM"}
        response = self.app.put('/feedings/2', json=update_data) 
        self.assertEqual(response.status_code, 200)

    def test_put_feeding_invalid_id(self):
        update_data = {"feeding_time": "3 PM"}
        response = self.app.put('/feedings/999', json=update_data)
        self.assertEqual(response.status_code, 404)

    ## Test DELETE a feeding schedule
    def test_delete_feeding_valid_id(self):
        response = self.app.delete('/feedings/1') 
        self.assertEqual(response.status_code, 204)

    def test_delete_feeding_invalid_id(self):
        response = self.app.delete('/feedings/999') 
        self.assertEqual(response.status_code, 404)

    ################# Reports #################
    
    ## Animal Report
    def test_get_animal_report(self):
        response = self.app.get('/reports/animals')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), dict)
    
    ## Visitor Report
    def test_get_visitor_report(self):
        response = self.app.get('/reports/visitors')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), dict)
    
    ## Revenue Report
    def test_get_revenue_report(self):
        response = self.app.get('/reports/revenue')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), dict)




if __name__ == '__main__':
    unittest.main()