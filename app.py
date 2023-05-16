import os
import csv
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
headers = {
        'Authorization': 'Bearer ' + key,
        "accept": "application/json",
        "content-type": "application/json"
    }

def get_asset_id(assetTag):
    url = base_url + 'hardware/bytag/' + assetTag
    response = requests.get(url, headers=headers)
    return response.json()['id']

def get_user_id(username):
    url = base_url + 'users?username=' + username
    response = requests.get(url, headers=headers)
    return response.json()['rows'][0]['id']

def check_in(id, status_id):
    url = base_url + 'hardware/' + str(id) + '/checkin'
    payload = {
        'status_id': status_id,
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def check_out_to_cart(asset_id, cart_id):
    url = base_url + 'hardware/' + str(asset_id) + '/checkout'
    payload = {
        'checkout_to_type': 'asset',
        'assigned_asset': cart_id,
    }
    response = requests.post(url, json=payload, headers=headers)

    return response.json()

# Needs implementation
def check_out_to_user(asset_id, user_id):
    url = base_url + 'users/' + str(asset_id) + '/checkout'
    payload = {
        'checkout_to_type': 'asset',
        'assigned_asset': user_id,
    }
    response = requests.post(url, json=payload, headers=headers)

    return response.json()

def print_CSV_rows(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['first_name'], row['last_name'])
        
def App():
    return

if (__name__ == '__main__'):
    App()


