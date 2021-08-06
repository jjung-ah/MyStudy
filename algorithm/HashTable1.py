class Hashtable:

    def __init__(self):
        self.table = [None for _ in range(139)]

    '''
    def simple_hash(self, name):
        ord_sum = 0
        for letter in name:
            ord_sum += ord(letter)
        return ord_sum % len(self.table)
        # return sum(map(ord, name)) % len(self.table)
    '''

    def put(self, name, num):
        #self.table[self.simple_hash(name)] = num
        self.table[self.better_hash(name)] = num

    def show(self):
        for idx, value in enumerate(self.table):
            if value:   # is not None
                print(idx, value)
    
    def find(self, name):
        #return self.table[self.simple_hash(name)]
        return self.table[self.better_hash(name)]

    def better_hash(self, name):
        honer = 37
        ord_sum = 0
        for letter in name:
            ord_sum += ord_sum * honer + ord(letter)
        return ord_sum % len(self.table)

    
##### 결과 확인 #####
boo = Hashtable()
boo.put('Kim', 7458)
boo.put('John', 8569)
boo.put('Smith', 1452)
boo.put('Michael', 2563)
boo.put('Raymond', 1598)
boo.put('Clayton', 7432)
boo.show()


''' 결과
42 1598
54 2563
81 1452
87 7458
100 7432
108 8569
'''
