# Let's use python to make an API call using package called requests
# # dependencies are pip
# import requests
# # import json
#
# post_api_response = requests.get("https://api.postcodes.io/postcodes/se120nb")
# if post_api_response.status_code == "200":
#     print("Thank you for request" + str(post_api_response.status_code))
# else:
#     print("Sorry the postcode is incorrect please enter the correct postcode")

# response_bbc = requests.get("https://www.bbc.co.uk/")
# # print(response_bbc)
# # print(response_bbc.headers)
#
# print(response_bbc.content)
# data_headers = response_bbc.headers
# for data_in in data_headers.keys():
#     print(data_in)
#
#
# # # json_data = response.bbc.json())
# # print(type(json_data))


# Create a program that request a post code
# check if the postcode is valid
# then uses an API call to fetch more data from post code
# display the data in user friendly format

import requests
post_api_response = requests.get("http://postcodes.io/docs")
user = input("please enter your postcode")
if post_api_response.status_code == "200":
    print(post_api_response.content)
else:
    print("Sorry the postcode is incorrect please enter the correct postcode")

