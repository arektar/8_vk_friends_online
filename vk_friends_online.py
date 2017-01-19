import vk
import getpass

APP_ID = 5827034


def get_user_login():
    login = getpass.getpass("Write your VK.com login: ")
    assert login, 'No login'
    return login


def get_user_password():
    password = getpass.getpass("Write your VK.com password: ")
    assert password, 'No password'
    return password


def make_vk_session(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    return api


def get_online_friends(api):
    online_friends = api.friends.getOnline()
    return online_friends['response']


def output_friends_to_console(api,friends_online):
    print("Друзья онлайн: \n")
    for friend in friends_online:
        api.users.get(friend)
        print("%s %s" % (friend['first_name'], friend['last_name']))

if __name__ == '__main__':
    my_login = get_user_login()
    my_password = get_user_password()
    my_session_api = make_vk_session(my_login, my_password)
    my_friends_online = get_online_friends(my_session_api)
    output_friends_to_console(my_session_api, my_friends_online)
