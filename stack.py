stack = []


def pushit():
    stack.append(str(input('Enter new string: ')).strip())


def popit():
    if len(stack) == 0:
        print('Cannot pop from an empty stack!')
    else:

        print('Remove [', repr(stack.pop(-1)), ']')


def viewstack():
    print(stack)


def showmenu():
    global pr
    pr = """
    p(u)sh 
    p(o)P
    (v)iew
    (q)uit

Enter choice:
    """


if __name__ == '__main__':
    showmenu()

CMDs = {'u': pushit, "o": popit, "v": viewstack}

while True:
    while True:
        try:
            choice = str(input(pr).strip()[0].lower())
        except(EOFError, KeyboardInterrupt, IndexError):
            choice = 'q'

        print('You picker: [%s]' % choice)
        if choice not in 'uovq':
            print('Invalid option, try again')
        else:
            break

    if choice == "q":
        break
    CMDs[choice]()
