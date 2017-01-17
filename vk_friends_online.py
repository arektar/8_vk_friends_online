import vk


APP_ID = 5827034


def get_user_login():
    login = str(input("Write your VK.com login: "))
    assert login, 'No login'
    return login


def get_user_password():
    password = str(input("Write your VK.com password: "))
    assert password, 'No password'
    return


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)  # например, api.friends.get()
    friends = api.friends.get(fields='online')
    online_friends = []
    for friend in friends:
        if friend['online'] == 1:
            online_friends.append(friend)
    return online_friends


def output_friends_to_console(friends_online):
    print("Друзья онлайн: \n")
    for friend in friends_online:
        print("%s %s" % (friend['first_name'], friend['last_name']))

    pass

if __name__ == '__main__':
    my_login = get_user_login()
    my_password = get_user_password()
    my_friends_online = get_online_friends(my_login, my_password)
    output_friends_to_console(my_friends_online)
