# 숫자 문자열과 영단어   # 다시하기

num_dict = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
string = ''
num = 0
answer = ''
s = "one4seveneight"

for i in s:
    if i.isdigit() == False:
        string += i
    else:
        string 