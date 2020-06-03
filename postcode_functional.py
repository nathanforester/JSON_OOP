import requests



path = 'http://api.postcodes.io/postcodes/'
argument = ''


def postcode_checker(postcode):
    output1 = 'fail, try again'
    output2 = 'success'
    response = requests.get(path + postcode)
    response_status_codes = response.status_code
    if response_status_codes == 400:
        return output1
    elif response_status_codes == 200:
        return output2
    else:
        return output1


def return_values(postcode):
    response = requests.get(path + postcode)
    response_dict = response.json()
    value_dict = response_dict['result']
    long = value_dict['longitude value']
    lat = value_dict["latitude value"]
    parl = ['parliamentary_constituency']
    nuts = ['nuts value']
    output = f'your long value is {long}, your lat value is {lat}, your parl is {parl}, your nuts is {nuts}'
    return output


user_input = input('please enter your postcode: ')
print(postcode_checker(user_input), return_values(user_input))
