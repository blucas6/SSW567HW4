'''
Author: Benjamin Lucas
Description: Grabs a users repository data
'''

import requests
import json

def grabUserRepos(userid, token=''):
    website = "https://api.github.com/"
    if userid and website and isinstance(userid, str) and isinstance(website, str):
        # get list of repos
        url = website + "users/" + userid + "/repos"
        if token:
            res = requests.get(url, auth=(userid, token))
        else:
            res = requests.get(url)
        d = {}
        if res.status_code == 200:
            repos = res.json()
            for repo in repos:
                url = website + "repos/" + userid + "/" + repo['name'] + "/commits"
                if token:
                    nres = requests.get(url, auth=(userid, token))
                else:
                    nres = requests.get(url)
                if nres.status_code == 200:
                    commits = nres.json()
                    d[repo['name']] = len(commits)
                else:
                    return nres.status_code
        else:
            return res.status_code
        return d
    else:
        return -1

if __name__ == "__main__":
    token = ""
    data = grabUserRepos(input("Enter your Github user ID: "), token)
    ml = max(len(repo) for repo in data)
    for repo in data:
        print(f"Repo: {repo}{' '*(ml-len(repo))}\tNumber of commits: {data[repo]}")
