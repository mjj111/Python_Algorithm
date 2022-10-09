from typing import List
import collections

def groupAnagrams(self, strs : List[str])->List[List[str]]:
    anagrams = collections.defualtdict(int)
    for word in strs:
        #정렬하여 추가 
        # sorted() 를 사용하게될 경우, word 문자열을 하나씩 빼서 정렬 후 리스트로 전달한다. 
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())