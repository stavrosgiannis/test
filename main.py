import json
import locale
import re

import requests
from flask import Flask, render_template, typing

import io
from base64 import b64encode

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', apiStatus=apiStatus(), bTest=runBacktest(), apiPairHistory=apiWhitelist(),
                           title="TestTitle")


def apiStatus():
    _session = requests.Session()
    _session.auth = ("newbiee12", "anubis12")
    token = json.loads(_session.request("POST", "http://192.168.178.49:8080/api/v1/token/login").text)
    print(token["access_token"])

    # GET - -header
    # "Authorization: Bearer ${access_token}"
    # http: // localhost: 8080 / api / v1 / count
    hd = f"Authorization: Bearer {token['access_token']}"
    print(hd)
    r = _session.request("GET", "http://192.168.178.49:8080/api/v1/status", data=hd).text

    characters_to_remove = '{}[]"'
    for i in characters_to_remove:
        r = r.replace(i, '')
    r = r.split(',')

    r_dict = dict()
    for item in r:
        r_dict[item.split(':', 1)[0]] = item.split(':', 1)[1]

    # print(f"{type(r_dict)} + {len(r_dict)}")
    print(r_dict)

    return r_dict


def apiWhitelist():
    _session = requests.Session()
    _session.auth = ("newbiee12", "anubis12")
    token = json.loads(_session.request("POST", "http://192.168.178.49:8080/api/v1/token/login").text)
    print(token["access_token"])

    # GET - -header
    # "Authorization: Bearer ${access_token}"
    # http: // localhost: 8080 / api / v1 / count
    hd = f"Authorization: Bearer {token['access_token']}"
    print(hd)
    r = _session.request("GET", "http://192.168.178.49:8080/api/v1/whitelist", data=hd).text
    characters_to_remove = '{}[]"'
    for i in characters_to_remove:
        r = r.replace(i, '')
    r = r.split(',')

    r_dict = dict()
    print(r)
    for item in r:
        print(item)
        r_dict[item.split(':')[0]] = item.split(':')[1]

    print(f"{type(r_dict)} + {len(r_dict)}")
    print(r_dict)

    return r_dict



def runBacktest():
    import subprocess
    result = subprocess.run(['ipconfig'], stdout=subprocess.PIPE).stdout.decode("unicode-escape")
    print(f"{type(result)} + {(result)}")
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runBacktest()
    app.run(host="0.0.0.0")
