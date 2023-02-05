from common import yellow, cyan, log, green, verdict, getUsers

def get_users_test():
    users = getUsers() 
    expected = {'kermitt': 'Happy$100', 'Shabone': 'bonny', 'Eeboo': 'boo', 'Maggy': 'arrawarrru', 'Mr. C': 'meow'}

    for x in users:
        print(x + "   " + users[x])

    verdict(users, expected, "get_users_test")


if __name__ == "__main__":
    get_users_test()