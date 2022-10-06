#! /usr/bin/env python3

import requests
import json


def test_post(payload):

    try:
        # httpbin.org > テスト用のサービス
        url = 'https://httpbin.org/post'
        # headers = {'Content-Type': 'application/json'} json文字列をpostする場合
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        res = requests.post(url, data=payload, headers=headers)
        jsonData = res.json()
        return jsonData
    except requests.exceptions.RequestException as e:
        print('HTTPError: ', e)
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)
