import requests
from pytest_bdd import scenario, given, when, then
import  setup as S

user_id = '210700286'

@scenario('features/login.feature', 'login', encoding='utf-8')
def test_logging_in_backend():

    query = 'https://api.vk.com/method/users.get?user_ids=' + user_id + '&access_token=' + S.access_token + '&v=5.130'
    response = requests.get(query)
    #print(response.json().get('response')[0].get('first_name'))
    assert response == 200

@scenario('features/getWallMessages.feature', 'getWallMessages', encoding='utf-8')
def getWallMessages():
    query = 'https://api.vk.com/method/wall.get?owner_id=' + user_id + '&count=10&access_token=' + S.access_token + '&v=5.130'
    response = requests.get(query)
    assert response.json().get('count') >= 0

@scenario('features/postMessageToWall.feature', 'postMessageToWall', encoding='utf-8')
def postMessageToWall():
    query = 'https://api.vk.com/method/wall.post?owner_id=' + user_id + '&message="test"&access_token=' + S.access_token + '&v=5.130'
    response = requests.get(query)
    assert response.json().get('response')[0].isdigit() == True