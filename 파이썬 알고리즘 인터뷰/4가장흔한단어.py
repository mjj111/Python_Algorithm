import re
import collections
from typing import List
def mostCommonWord(self, paragraph : str, banned : List[str]) -> str:
    words = [word for word in re.sub(r'[^\w','',paragraph)
             .lower().split() if word not in banned]
    counts = collections.defaultdict(int)
    for word in words:
        counts[word]+=1
        
    return max(counts,key = counts.get)
    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫번쨰 인덱스 리턴 [('ball',2)]
    return counts.most_common(1)[0][0]