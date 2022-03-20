# Test if one can add data to the database
from unittest import TestCase
import requests
import json
def test_get_one_people_route():
        res = requests.get("http://127.0.0.1:5000/people/1")
        assert res.headers["Content-Type"] == "application/json"
        assert res.status_code == 200

def test_get_all_people_route():
        res = requests.get("http://127.0.0.1:5000/people")
        assert res.headers["Content-Type"] == "application/json"
        assert res.status_code == 200

def test_homepage_route():
        res = requests.get("http://127.0.0.1:5000/")
        assert res.status_code == 200

def test_update_page_route():
        res = requests.get("http://127.0.0.1:5000/update/1")
        assert res.status_code == 200

def test_delete_page_route():
        res = requests.get("http://127.0.0.1:5000/delete/16")
        assert res.status_code == 200


def test_post_add_people_route():
    my_data = {
                "pid": '28',
                "name": 'sai',
                "ptype": 'male',
                "age": '28',
                "desc": 'good',
                "check": 'True',
            }
    get_data = requests.post("http://127.0.0.1:5000/add", data=my_data, timeout=30)
    assert get_data.status_code == 200

def test_POST_people_route():
        res = requests.get("http://127.0.0.1:5000/ui/#/People/people.create")
        assert res.status_code == 200

def test_Csv_route():
        res = requests.get("http://127.0.0.1:5000/report/pdf")
        assert res.status_code == 200