from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import sys



# Get all reviews for a Dealership
def main(filter):
    try:
        client = Cloudant.iam(
                account_name = "168f74c7-800c-44b4-81cb-807258c1ac04-bluemix",
                api_key = "wpsISj8MmMiQGx3fXWyDyqSBTV5cK6oIMJRb95nj6pwn",
                connect = True,
            )
    
        my_db = client['reviews']
        result_collection = Result(my_db.all_docs, include_docs=True)

        lst = []
        print("dealerId: {0}".format(filter["dealerId"]))
    
        for doc in result_collection[1:]:
            if doc['doc'].get('dealership'):
                if doc['doc']['dealership'] == dict["dealerId"]:
                    purchase_date = ""
                    if "purchase_date" in doc['doc']:
                        purchase_date = doc['doc']['purchase_date']
                        
                    car_make = ""
                    if "car_make" in doc['doc']:
                        car_make = doc['doc']['car_make']
                    
                    car_model = ""
                    if "car_model" in doc['doc']:
                        car_model = doc['doc']['car_model']
                        
                    car_year = ""    
                    if "car_year" in doc['doc']:
                        car_year = doc['doc']['car_year']
                        
                    lst.append({
                        "id": doc['doc']['id'],
                        "name": doc['doc']['name'],
                        "dealership": doc['doc']['dealership'],
                        "review": doc['doc']['review'],
                        "purchase": doc['doc']['purchase'],
                        "purchase_date": purchase_date,
                        "car_make": car_make,
                        "car_model": car_model,
                        "car_year": car_year
                    })
    
        if len(lst) > 0:
            return {
                "status": 200,
                "message": "Success",
                "reviews": lst
            }
        else:
            return {
                "status": 404,
                "message": "DealerId does not exist"
            }
    except:
        return {
                "status": 500,
                "message": "Something went wrong on the server"
            }
        
