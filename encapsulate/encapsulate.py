class User():
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_attr(self, attr):
        if attr == 'name':
            return self.__name
        elif attr == 'email':
            return self.__email
        elif attr == 'password':
            return self.__password
        else:
            return f'Entered attr is None'


    def set_attr(self, attr, entr):
        if attr == 'name':
            self.__name = entr
        elif attr == 'email':
            self.__email = entr
        elif attr == 'password':
            self.__password = entr
        else:
            return print('Attr is None, please check if you correct set new attr')


user = User('Kirill Hutsenko', 'kirillhutsenko@gmail.com', 'hfAHf3423ujdD')
user.set_attr('name', 'Oleksiy Sosunok')
print(user.get_attr('name'))

