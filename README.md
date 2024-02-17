Welcome to the Zoo Manager API documentation. This document provides details on how to interact with the Zoo Manager's various endpoints and how to run the application.
Running the Application
To run the Zoo Manager application, follow these steps:
Prerequisites:
Ensure Docker is installed on your system.
Clone or download the application repository to your local machine.

Build the Docker Image:
Open a terminal and navigate to the project directory.
docker build -t zoo_manager .

Run the Application:
docker run -p 5000:5000 zoo_manager

Accessing the Application:
The application will be available at: http://localhost:5000/
You can now interact with the API endpoints as described in this documentation.

API Endpoints
Animals API
Retrieve All Animals
Endpoint: /animals
Method: GET
Description: Retrieves a list of all animals.
Response: JSON array of animals.

Retrieve a Specific Animal by ID
Endpoint: /animals/
Method: GET
Description: Retrieves details of a specific animal by ID.
Parameters: id - Animal ID.
Response: JSON object of the animal's details.

Add a New Animal
Endpoint: /animals
Method: POST
Description: Adds a new animal to the system.
Body: JSON object containing new animal details.
Response: JSON object of the added animal.

Update an Existing Animal
Endpoint: /animals/
Method: PUT
Description: Updates details of an existing animal.
Parameters: id - Animal ID.
Body: JSON object with updated animal details.
Response: JSON object of the updated animal.

Remove an Animal
Endpoint: /animals/
Method: DELETE
Description: Removes an animal from the system.
Parameters: id - Animal ID.
Response: HTTP Status Code 204 on successful deletion.

Employees API
[Similar structure as Animals API, with endpoints for /employees, /employees/, etc.]
Feedings API
[Similar structure as Animals API, with endpoints for /feedings, /feedings/, etc.]
Reporting API
Animal Report
Endpoint: /reports/animals
Method: GET
Description: Generates a report of animals.
Response: JSON object containing animal report.

Visitors Report
Endpoint: /reports/visitors
Method: GET
Description: Generates a report of visitors.
Response: JSON object containing visitors report.

Revenue Report
Endpoint: /reports/revenue
Method: GET
Description: Generates a report of revenue.
Response: JSON object containing revenue report.
