def call_target():
    f = open("data/target.txt", "r")
    target = f.read()
    return target

def call_credentials():
    f2 = open("data/credentials.txt", "r")
    credentials = f2.read()
    username, password = credentials.split(':')
    return username, password