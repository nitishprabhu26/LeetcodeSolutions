# Approach 1: Sorted List

class TwoSum:
    def __init__(self):
        self.nums = []
        self.is_sorted = False

    def add(self, number: int) -> None:
        # Inserting while maintaining the ascending order.
        # for index, num in enumerate(self.nums):
        #     if number <= num:
        #         self.nums.insert(index, number)
        #         return
        ## larger than any number
        #self.nums.append(number)

        self.nums.append(number)
        self.is_sorted = False

    def find(self, value: int) -> bool:
        if not self.is_sorted:
            self.nums.sort()
            self.is_sorted = True
            
        low, high = 0, len(self.nums)-1
        while low < high:
            currSum = self.nums[low] + self.nums[high]
            if currSum < value:
                low += 1
            elif currSum > value:
                high -= 1
            else: # currSum == value
                return True
        
        return False


# Your TwoSum object will be instantiated and called as such:
number = [1, 3, 5]
target_1 = 4
target_2 = 7
obj = TwoSum()
for i in number:
    obj.add(i)
    
print(obj.find(target_1))
print(obj.find(target_2))


# The usage pattern implies that we should try to minimize the cost of add(number) function. As a result, we sort the list within the 
# find(value) function instead of the add(number) function.
# So to the above questions about where to place the sort operation, actually both options are valid and correct. Due to the usage 
# pattern of the two functions though, it is less optimal to sort the list at each add operation.

# Complexity analysis:

# Time Complexity: 
# For the add(number) function: O(1), since we simply append the element into the list.
# For the find(value) function: O(N⋅log(N)). In the worst case, we would need to sort the list first, which is of O(N⋅log(N)) time 
# complexity normally. And later, again in the worst case we need to iterate through the entire list, which is of O(N) time complexity. 
# As a result, the overall time complexity of the function lies on O(N⋅log(N)) of the sorting operation, which dominates over the 
# later iteration part.

# Space Complexity: 
# the overall space complexity of the data structure is O(N) where N is the total number of numbers that have been added.
