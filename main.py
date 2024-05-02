# Copyright (c) 2023-2024 Westfall Inc.
#
# This file is part of Windwatcher.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, and can be found in the file NOTICE inside this
# git repository.
#
# This program is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests
import json

def auth(host):
    url = host+"/authentication"
    payload = json.dumps({
      "username": "test",
      "password": "test"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return response.json()['token']

def auth_header(token):
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer '+token
    }
    return headers

def createOrg(host, token):

    url = host+"/orgs"

    payload = json.dumps({
      "orgs": [
        {
          "id": "westfall",
          "name": "Westfall"
        }
      ]
    })

    response = requests.request("POST", url, headers=auth_header(token), data=payload)

    print(response.text)

def createProject(host, token):
    url = host+ "/projects"

    payload = json.dumps({
      "projects": [
        {
          "id": "rocket",
          "name": "Rocket",
          "orgId": "westfall",
          "projectType": "default"
        }
      ]
    })

    response = requests.request("POST", url, headers=auth_header(token), data=payload)
    print(response.text)

def getOrgs(host, token):
    url = host+ "/orgs"

    response = requests.request("GET", url, headers=auth_header(token))
    print(response.text)

if __name__ == '__main__':
    host = 'http://localhost/mms'
    token = auth(host)
    createOrg(host, token)
    createProject(host, token)
    #getOrgs(host, token)
