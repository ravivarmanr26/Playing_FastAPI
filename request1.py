import requests
import os 

url ='http://localhost:8000/poem_generator'

headers ={
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
  "topic": "ai",
  "lines": 5
}

response = requests.post(url,headers=headers,json=data)
# Check if the request was successful
if response.status_code == 200:
    # Print the response object
    print(response)
    
    # Print the JSON response
    print(response.json())
    
    # Write the JSON response to a file
    with open('file1.txt', 'w') as f:
        f.write(str(response.json()))
else:
    print(f"Request failed with status code {response.status_code}")


url ='http://localhost:8000/code_generator'

headers ={
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
  "Language": "Python",
  "Problem": "write a program to find a factorial of number"
}

response = requests.post(url,headers=headers,json=data)
# Check if the request was successful
if response.status_code == 200:
    # Print the response object
    print(response)
    
    # Print the JSON response
    print(response.json())
    
    # Write the JSON response to a file
    with open('file.txt', 'w') as f:
        f.write(str(response.json()))
else:
    print(f"Request failed with status code {response.status_code}")
