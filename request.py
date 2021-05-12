# -*- coding: utf-8 -*-
"""
Created on Wed May 12 19:59:40 2021

@author: Pragi
"""


import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())