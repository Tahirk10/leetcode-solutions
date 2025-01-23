class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums1 = list(set(nums))
        if len(nums1) == 1:
            if nums1[0] * 4 == target and len(nums) >= 4:
                return [[nums1[0], nums1[0], nums1[0], nums1[0]]]
            return []
        
        nums.sort()
        res = []
        x = 0

        while x < len(nums) - 1:
            y = x + 1
            while y < len(nums):
                nums2 = nums[:] 
                row = [nums[x], nums[y]]
                nums2.remove(row[0])
                nums2.remove(row[1])
                
                a = 0
                b = len(nums2) - 1
                while a < b:
                    new_row = row[:]
                    new_row.append(nums2[a])
                    new_row.append(nums2[b])
                    
                    if sum(new_row) == target:
                        res.append(new_row)
                        a += 1
                        b -= 1
                    elif sum(new_row) < target:
                        a += 1
                    else:
                        b -= 1

                y += 1
            x += 1

        res2 = [sorted(x) for x in res]
        return list(map(list, set(map(tuple, res2))))
