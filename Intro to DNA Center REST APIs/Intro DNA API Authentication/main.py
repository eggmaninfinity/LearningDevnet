
import requests
from requests.auth import HTTPBasicAuth
import env_lab

requests.packages.urllib3.disable_warnings()

def get_auth_token():
    # Endpoint URL
    endpoint = '/dna/system/api/v1/auth/token'
    url = 'https://' + env_lab.DNA_CENTER['host'] + endpoint
    # Make the POST Request
    resp = requests.post(url, auth=HTTPBasicAuth(env_lab.DNA_CENTER['username'], env_lab.DNA_CENTER['password']), verify=False)
    # Retrieve the Token from the returned JSON
    token = resp.json()['Token']
    # append token to tokens.txt file
    with open('tokens.txt', 'a') as file:
        file.write(f'{token}\n')
    # print confirmation
    print('Token Retrieved and stored in tokens.txt')

  
if __name__ == "__main__":
    get_auth_token()