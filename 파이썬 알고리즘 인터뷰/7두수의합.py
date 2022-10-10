from typing import List


def twoSum(self, nums : List[int], target :int)-> List[int]:
    nums_map = {}
    #키와 값을 바꿔서 딕셔너리로 저장 
    for i,num in enumerate(nums):
        nums_map[num] = i
        
    #타겟에서 첫 번째 수를 뺀 결과를 키로 조회 
    #for 로 하나씩 찾는것 보다는 in , in 으로 리스트에서 찾는 것 보다 딕셔너리에서 찾기
    for i,num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target -num]:
            return [i,nums_map[target -num]]
        