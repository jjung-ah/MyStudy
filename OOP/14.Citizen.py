class Citizen:
    """주민 클래스"""
    drinking_age = 19  # 음주 가능 나이
    
    def __init__(self, name, age, residint_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.age = age
        self.resident_id = resident_id
        
    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self.resident_id == id_field
        
    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.age >= Citizen.drinking_age
    
    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self.age) + "살입니다!"
       
        
kyusik = Citizen("최규식", 25, "12345678")
young = Citizen("younghoon", 5, "87654321")  # 어린이

print(kyusik.resident_id)  # 출력값 : 12345678
kyusik.age = -12
print(kyusik)  # 출력값 :  최규식씨는 -12살입니다. 
