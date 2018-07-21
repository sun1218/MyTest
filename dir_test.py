class temp_class(object):

    str1 = "str"

    def __init__(self):
        self.a = "A"
        self.b = "B"

    def print_a(self):
        print(self.a)

    def print_b(self):
        print(self.b)


temp = temp_class
print(dir(temp))
