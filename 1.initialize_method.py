# 1.initialize_method

class User:
    # initialize 메소드를 여기 쓰세요
    def initialize(self):
        self.name = name
        self.email = email
        self.password = password
        
        return self.name, self.email, self.password

user1 = User()
user1.name = "Young"
user1.email = "young@codeit.kr"
user1.password = "123456"
    
user2 = User()
user2.name = "Yoonsoo"
user2.email = "yoonsoo@codeit.kr"
user2.password = "abcdef"
    
user3 = User()
user3.name = "Taeho"
user3.email = "taeho@codeit.kr"
user3.password = "123abc"
    
user4 = User()
user4.name = "Lisa"
user4.email = "lisa@codeit.kr"
user4.password = "abc123"


print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)
