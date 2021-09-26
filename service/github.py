import requests
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
)

class GitHub:
    def __init__(self, org, token):
        self.token = token
        self.org = org
        self.host = 'https://api.github.com/'
        self.headers = {
            'Authorization': f'Bearer {self.token}'
        }

    def get_members(self):
        method = f'orgs/{self.org}/members'
        members = self.request(self.host + method, self.headers)
        for m in members:
            yield m['login']

    def get_pulls(self, repo, username):
        method = f'repos/{self.org}/{repo}/pulls?state=all'
        pulls = self.request(self.host + method, self.headers)
        for p in pulls:
            if p['user']['login'] == username:
                yield {
                    'merged_at': p['merged_at'],
                    'closed_at': p['closed_at']
                }

    def get_repos(self):
        method = f'orgs/{self.org}/repos'
        repos = self.request(self.host + method, self.headers)
        for r in repos:
            yield r['name']

    def request(self, url, headers):
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            logging.error(url)
            logging.error(response.status_code)
            logging.error(response.content.decode())
            return []
        return response.json()

