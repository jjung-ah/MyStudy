class Citizen:
    """주민 클래스"""
    drinking_age = 19  # 음주 가능 나이
    
    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.__age = age  # __age변수에 접근할 수 없기 때문에 주민의 나이를 알 수 없고, 수정할 수도 없다!
        self.__resident_id = resident_id
        
    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self.__resident_id == id_field
        
    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.__age >= Citizen.drinking_age
    
    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self.age) + "살입니다!"
    
    def get_age(self):   # Citizen 클래스 밖에서도 이제 이 get_age 메소드를 이용해서 __age값을 읽을 수 있다. 
        return self.__age
    
    def set_age(self, value):   # __age의 값을 설정할 수 있다. 
        self.__age = value
        

young = Citizen("younghoon kang", 18, "12345678")
 
print(young.get_age())   # 18
 
young.set_age(25)
print(young.get_age())   # 25
        
        
#kyusik = Citizen("최규식", 25, "12345678")

#print(kyusik.__resident_id)  # 에러 발생 # 외부에서 숨김 
#print(kyusik.__age)  # 에러 발생
## NameError: name 'resident_id' is not defined
