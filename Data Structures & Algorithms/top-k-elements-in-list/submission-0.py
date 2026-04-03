class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = [] # treat as a stack, keep size at max k
        temp = [] # a temp stack when adding new values

        store = defaultdict(int)

        for i in range(len(nums)):
            store[nums[i]] += 1
        
        # now we have a dictionary with the #s and their # of occurances

        for key, val in store.items():
            while len(ret) > 0 and val > store[ret[-1]]: # while val is bigger than current smallest in ret
                temp.append(ret.pop())
            ret.append(key)
            while len(ret) < k and len(temp) > 0:
                ret.append(temp.pop())

        return ret[:k]

                


