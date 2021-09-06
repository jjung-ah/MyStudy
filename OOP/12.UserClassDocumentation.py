# User 클래스 문서화하기  # 수정 필요

class User:
    """SNS의 유저를 나타내는 클래스"""
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    @classmethod
    def number_of_users(cls):
        print("총 유저 수는: {}입니다".format(cls.count))

        
# 실행 결과




help(User)

'''
Help on class User in module __main__:

class User(builtins.object)
 |  User(name, email, pw)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, name, email, pw)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __str__(self)
 |      Return str(self).
 |  
 |  say_hello(self)
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  number_of_users() from builtins.type
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  count = 3
 '''
