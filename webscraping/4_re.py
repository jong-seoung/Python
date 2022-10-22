import re
p = re.compile("ca.e") 
# . (ca.e): 하나의 문자를 의미 > cafe, care, case (0) | caffe(x)
# ^ (^de) : 문자열의 시작 > desk, destination (0) | fade (x)
# $ (se$) : 문자열의 끝을 의미 > case, base (0) |face (x)

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지않음")

# 매칭하는법 - 매치되지않으면 에러 발생
m = p.match("careless") # match 주어진 문자열의 처음부터 일치하는지 확인
print_match(m) 

