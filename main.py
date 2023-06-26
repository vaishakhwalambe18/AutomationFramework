# execution_driver()
import requests

str_end_point = 'https://reqres.in/api/users/?q=id=507'
response = requests.get(str_end_point)
print(response)
print(response.json())
print(response.status_code)