# 6.GameCharacter

class GameCharacter:
    # 게임 캐릭터 클래스
    def __init__(self, name, hp, power):
        # 게임 캐릭터는 속성으로 이름, hp, 공격력을 갖는다
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        # 게임 캐릭터가 살아있는지(체력이 0이 넘는지) 확인하는 메소드
        if self.hp > 0:
            return True
        else:
            return False

    def get_attacked(self, damage):
        """
        게임 캐릭터가 살아있으면 공격한 캐릭터의 공격력만큼 체력을 깎는 메소드
        조건:    
            1. 이미 캐릭터가 죽었으면 죽었다는 메시지를 출력한다
            2. 남은 체력보다 공격력이 더 크면 체력은 0이 된다.
        """
        if self.is_alive:
            if self.hp >= damage:
                self.hp -= damage
                #print(self.hp)
            else:
                self.hp = 0
                #print(self.hp)
                print("{}님은 이미 죽었습니다.".format(self.name))
        else:
            print("{}님은 이미 죽었습니다.".format(self.name))

    def attack(self, other_character):
        # 게임 캐릭터가 살아있으면 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다.
        if self.is_alive:
            return other_character.get_attacked(self.power)

    def __str__(self):
        # 게임 캐릭터의 의미있는 정보를 포함한 문자열을 리턴한다.
        return "{}님의 hp는 {}만큼 남았습니다.".format(self.name, self.hp)

# 게임 캐릭터 인스턴스 생성                        
character_1 = GameCharacter("Ww영훈전사wW", 200, 30)
character_2 = GameCharacter("Xx지웅최고xX", 100, 50)

# 게임 캐릭터 인스턴스들 서로 공격
character_1.attack(character_2)  # 200 70
character_2.attack(character_1)  # 150 70
character_2.attack(character_1)  # 100 70
character_2.attack(character_1)  # 50 70
character_2.attack(character_1)  # 0 70
character_2.attack(character_1)  

# 게임 캐릭터 인스턴스 출력
print(character_1)
print(character_2)