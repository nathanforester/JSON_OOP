import requests

path = 'http://api.postcodes.io/postcodes/'

arguments = 'cf336aa'

url_target = path + arguments

print(url_target)

# Make request and capture response

response = requests.get(url_target)
print(response)
response_status_code = requests.get('http://api.postcodes.io/postcodes/')

print(response_status_code.status_code)
if response_status_code.status_code != 400:
    print('successful')
elif response_status_code.status_code != 200:
    print('oops')
else:
    print('please try again')

print(type(response))

# Parsing or getting the dictionary out

print(response.json())
response_dictionary = response.json()
print(type(response_dictionary))
for key in response_dictionary.keys():
    print(key)
result_dictionary = response_dictionary['result']
print(result_dictionary)
for key in result_dictionary.keys():
    print(key, 'value:', result_dictionary[key])