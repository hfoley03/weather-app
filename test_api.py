import requests
import pytest

def test_get_check_status_code_equals_200():
     response = requests.get("https://weather-app-323116.appspot.com")
     assert response.status_code == 200

def test_get_location_galway_check_status_code_equals_200():
     response = requests.get("https://weather-app-323116.appspot.com/?location=galway%2C+ireland")
     assert response.status_code == 200

def test_get__random_endpoint_check_status_code_equals_404():
     response = requests.get("https://weather-app-323116.appspot.com/asdf")
     assert response.status_code == 404

def test_destructive_bad_characters_check_status_code_200():
     response = requests.get("https://weather-app-323116.appspot.com/?location=%21%22%C2%A3%24%25%5E%26*%28%29%28%C2%AC%60%60%3F%3E%3C")
     assert response.status_code == 200

def test_try_to_post_json_check_status_code_405():
     myobj = {'somekey': 'somevalue'}
     response = requests.post("https://weather-app-323116.appspot.com",myobj)
     assert response.status_code == 405

def test_try_delete_check_status_code_405():
     response = requests.delete("https://weather-app-323116.appspot.com")
     assert response.status_code == 405

def test_header_check_content_type():
     response = requests.get("https://weather-app-323116.appspot.com")
     content_type=response.headers.get('content-type')
     assert content_type == "text/html; charset=utf-8"


if __name__ == '__main__':
    pytest.main() 