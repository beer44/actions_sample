#! /usr/bin/env python3

import requests


def check_alive():
    url = 'https://httpbin.org/get'
    response = requests.get(url)
    return response.status_code
