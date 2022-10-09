import collections
import re
def isPalindrome(self,s:str)-> bool :
    s = s.lower()
    #정규식으로 불필요한 문자 필터링
    #문자열의 경우 슬라이싱을 자주 사용하자 
    s = re.sub('[^a-z0-9]','',s)
    return s == s[::-1]