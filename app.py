import os
import sys
import csv
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
headers = {
        'Authorization': 'Bearer ' + API_KEY,
        "accept": "application/json",
        "content-type": "application/json"
    }

def get_asset_id(assetTag):
    url = BASE_URL + 'hardware/bytag/' + assetTag
    response = requests.get(url, headers=headers)
    return response.json()['id']

def get_user_id(username):
    url = BASE_URL + 'users?username=' + username
    response = requests.get(url, headers=headers)
    return response.json()['rows'][0]['id']

def check_in(id, status_id):
    url = BASE_URL + 'hardware/' + str(id) + '/checkin'
    payload = {
        'status_id': status_id,
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def check_out_to_cart(asset_id, cart_id):
    url = BASE_URL + 'hardware/' + str(asset_id) + '/checkout'
    payload = {
        'checkout_to_type': 'asset',
        'assigned_asset': cart_id,
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Needs implementation
def check_out_to_user(asset_id, user_id):
    url = BASE_URL + 'users/' + str(asset_id) + '/checkout'
    payload = {
        'checkout_to_type': 'asset',
        'assigned_asset': user_id,
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# add a main read csv function that depending on the action (check_in, check_out, etc) calls
# another function to get the correct formating of that csv
def get_values_of_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['first_name'], row['last_name'])
        

# get arguments from command line
def App():
    # total arguments
    num_argv = len(sys.argv)
    print("Total arguments passed:", num_argv, end=' ')
    
    # Arguments passed
    print("\nName of Python script:", sys.argv[0], end=' ')
    print("\nArguments passed:", end = " ")
    for i in range(1, num_argv):
        print(sys.argv[i], end=' ')
    print('')

if (__name__ == '__main__'):
    App()


