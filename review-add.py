from cloudant.client import Cloudant
from cloudant.error import CloudantException
import sys



# Post a review
def main(review):
    try:
        client = Cloudant.iam(
                account_name = "168f74c7-800c-44b4-81cb-807258c1ac04-bluemix",
                api_key = "wpsISj8MmMiQGx3fXWyDyqSBTV5cK6oIMJRb95nj6pwn",
                connect = True,
            )
    
        
        my_db = client['reviews']
        
        my_doc = my_db.create_document(review)
        if my_doc.exists:
            return {
                "status": 200,
                "message": "Success",
                "review": review
            }
        else:
            return {
                "status": 500,
                "message": "Something went wrong on the server"
            }
    except:
        return {
            "status": 500,
            "message": "Something went wrong on the server"
        }        
        
