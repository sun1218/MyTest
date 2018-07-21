db = {}
prompt = '''
(N)ew User Login
(E)xit User Login 
(Q)uit

    Enter choice: '''


def newuser():
    prompt = 'login desired:'
    while True:
        name = str(input(prompt))
        if name in db:
            prompt = "name taken, try another: "
        else:
            break
    pwd = str(input('passwd:'))
    db[name] = pwd


def olduser():
    name = str(input('login: '))
    pwd = str(input('passwd: '))
    passwd = db.get(name)
    if passwd == pwd:
        print('welcome back %s' % name)
    else:
        print('login incorrect!')


while True:
    try:
        choice = str(input(prompt))
    except(EOFError, KeyboardInterrupt):
        choice = 'q'

    print('\nYou picked: [%s]' % str(choice))

    if choice not in 'neq':
        print('invalid option, try again')
    else:
        if choice == 'q': break
        if choice == 'n': newuser()
        if choice == 'e': olduser()

