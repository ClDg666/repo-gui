import requests
import json
from pprint import pprint

def nick_name_list_repo():
    nickname = input('Nickname: ')
    url = f'https://api.github.com/users/{nickname}/repos'
    repo = requests.get(url)
    if repo.status_code == 200:
        repo_json = repo.json()
        pprint(repo_json)
        return  repo_json
    else:
        print('Namename not find!')

nick_name_list_repo()
