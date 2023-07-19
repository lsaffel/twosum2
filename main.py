def twonumbersum(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

if __name__ == '__main__':
    print(twonumbersum( [3,2,4], 6))
    print(twonumbersum( [3,3], 6))
    print(twonumbersum( [2,7,11,15], 9))
