import requests
from pytest_bdd import scenario, given, when, then
import setup as S  # I use setup.py to hide vk service tocken. It looks like "access_token='23ab7b1...c0203ebc'"

user_id = '210700286'


@scenario('features/incorrect_login.feature', 'incorrect_login', encoding='utf-8')
def incorrect_login():
    query = 'https://api.vk.com/method/users.get?user_ids=' + user_id + '&access_token=' + S.wrong_access_token + '&v=5.130'
    response = requests.get(query)
    assert response == 200


@scenario('features/getWallMessagesWithWrongUserId.feature', 'getWallMessagesWithWrongUserId', encoding='utf-8')
def getWallMessages():
    user_id = 'q'
    query = 'https://api.vk.com/method/wall.get?owner_id=' + user_id + '&count=10&access_token=' + S.correct_access_token + '&v=5.130'
    response = requests.get(query)
    assert response.json().get('count') >= 0


@scenario('features/postMessageToWallWithEmptyMessage.feature', 'postMessageToWallWithEmptyMessage', encoding='utf-8')
def postMessageToWall():
    message = ''
    query = 'https://api.vk.com/method/wall.post?owner_id=' + user_id + '&message=' + message + '&access_token=' + S.correct_access_token + '&v=5.130'
    response = requests.get(query)
    assert response.json().get('response')[0].isdigit() == True
