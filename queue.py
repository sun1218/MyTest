queue = []


def enQ():
    queue.append(input('Enter new string: ').strip())


def deQ():
    if len(queue) == 0:
        print('Cannot pop from an empty queue!')

    else:
        print('Removed [', repr(queue.pop(0)), ']')


def viewQ():
    print(queue)


CMDs = {'e': enQ, 'd': deQ, 'v': viewQ}


def showmenu():
    global pr
    pr = """
 (E)nqueue
 (D)equeue
 (V)iew
 (Q)uit

Enter choice: """


if __name__ == '__main__':
    showmenu()

while True:
    try:
        choice = input(pr).strip()[0].lower()

        print('\nYou picked: [%s]' % choice)

        if choice not in 'devq':
            print('Invalid option, try again')

        else:
            CMDs[choice]()

    except (EOFError, KeyboardInterrupt, IndexError, KeyError):
        break
