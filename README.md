"# CloudAppDev_Capstone_Cloud_Funcs" 

dealership-get.js
- Description: IBM Cloud Function in Node.js used by two apis to get all dealerships or dealerships by state
- Parameters: 
    - (none)
    - state
- Output: List of dealerships with details:
    - all dealerships
    - dealerships by state
- Errors:
    - 404: The database is empty
    - 500: Something went wrong on the server

- apis:
    - Method: GET
        - https://f67d5725.eu-de.apigw.appdomain.cloud/api/dealership
        - https://f67d5725.eu-de.apigw.appdomain.cloud/api/dealership?state=[state]


reviews-by-dealer.py
- Description: IBM Cloud Function in Python used by a api to get all Get all reviews for a dealership
- Parameter: dealerId
- Output: List of reviews with details:
    - reviews by dealership
- Errors:
    - 404: dealerId does not exist
    - 500: Something went wrong on the server

- apis:
    - Method: GET
        - https://f67d5725.eu-de.apigw.appdomain.cloud/api/review?dealerId=[dealerId]



review-add.py
- Description: IBM Cloud Function in Python used by a api to post a review for dealership
- Parameters: [JSON review object]
- Errors:
    - 500: Something went wrong on the server

- apis:
    - Method: POST
        - https://f67d5725.eu-de.apigw.appdomain.cloud/api/review