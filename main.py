# execution_driver()
from Framework.lib_util import *

str_end_point = 'https://reqres.in/api/users/?q=id=507'
# response = requests.get(str_end_point)
# print(response)
# print(response.json())
# print(response.status_code)
resposne = kyAPI.get_API( str_end_point, '', '', '', '', '200')
print(resposne.json())