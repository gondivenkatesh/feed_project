import requests
import json
 
url = "https://jsonplaceholder.typicode.com/comments"
 
response = requests.get(url)
 
with open("raw_data/comments.json", "w") as file:
    json.dump(response.json(), file, indent=4)
 
print("Feedback Data Stored Successfully")
 