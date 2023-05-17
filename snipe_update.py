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

# need to implement error handling and let user know what is happening for all functions
# GET functions
def get_asset_id(assetTag):
    url = BASE_URL + 'hardware/bytag/' + assetTag
    response = requests.get(url, headers=headers)
    return response.json()['id']
def get_user_id(username):
    url = BASE_URL + 'users?username=' + username
    response = requests.get(url, headers=headers)
    return response.json()['rows'][0]['id']
def get_location_id(location):
    url = BASE_URL + 'locations?name=' + location
    response = requests.get(url, headers=headers)
    return response.json()['rows'][0]['id']

# POST functions
def check_in(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            asset_id = str(get_asset_id(row['asset_to_check_in']))
            status_id = int(row['status_id'])
            url = BASE_URL + 'hardware/' + asset_id + '/checkin'
            payload = {
                'status_id': status_id,
            }
            response = requests.post(url, json=payload, headers=headers)
            print(response.json())

def check_out_to_asset(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            child_asset_id = str(get_asset_id(row['asset_to_check_out']))
            parent_asset_id = int(get_asset_id(row['check_out_to']))

            url = BASE_URL + 'hardware/' + child_asset_id + '/checkout'
            payload = {
                'checkout_to_type': 'asset',
                'assigned_asset': parent_asset_id,
            }
            response = requests.post(url, json=payload, headers=headers)
            print(response.json())

def check_out_to_user(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            asset_id = str(get_asset_id(row['asset_to_check_out']))
            user_id = int(get_user_id(row['check_out_to']))

            url = BASE_URL + 'hardware/' + asset_id + '/checkout'
            payload = {
                'checkout_to_type': 'user',
                'assigned_user': user_id,
            }
            response = requests.post(url, json=payload, headers=headers)
            print(response.json())
            
def check_out_to_location(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            asset_id = str(get_asset_id(row['asset_to_check_out']))
            locaiton_id = int(get_location_id(row['check_out_to']))

            url = BASE_URL + 'hardware/' + asset_id + '/checkout'
            payload = {
                'checkout_to_type': 'location',
                'assigned_location': locaiton_id,
            }
            response = requests.post(url, json=payload, headers=headers)
            print(response.json())

def App():

    # get arguments from command line only if there are 2 arguments
    if (len(sys.argv) < 3):
        print('not enough arguments')
        return
    elif(len(sys.argv) > 3):
        print('too many arguments')
        return
    
    file_path = sys.argv[1]
    action = sys.argv[2]

    # make switch case to corresponding action
    match action:
        case 'check_in':
            check_in(file_path)    
        case 'check_out_to_user':
            check_out_to_user(file_path)
        case 'check_out_to_asset':
            check_out_to_asset(file_path)
        case 'check_out_to_location':
            check_out_to_location(file_path)
        case _:
            print('\'%s\' is not a recignized action' % action)    

if (__name__ == '__main__'):
    App()


