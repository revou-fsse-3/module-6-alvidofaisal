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