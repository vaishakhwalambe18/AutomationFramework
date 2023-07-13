from Framework.lib_String import lib_String

# execution_driver()
# from Framework.lib_util import *
#
# str_end_point = 'https://reqres.in/api/users/?q=id=507'
# # response = requests.get(str_end_point)
# # print(response)
# # print(response.json())
# # print(response.status_code)
# resposne = kyAPI.get_API( str_end_point, '', '', '', '', '200')
# print(resposne.json())

# to add this on fwk level
f = open("C:\AutomationFramework\logs.txt", "r+")
f.truncate(0)
strs = "s1s2\n"
# lib_String.kyRemoveLineBreak(strs)
print(lib_String.kySearchString(strs,"s1"))




