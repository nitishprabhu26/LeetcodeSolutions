# Approach 2: HashTable

class TwoSum(object):

    def __init__(self):
        self.num_counts = {}


    def add(self, number):
        if number in self.num_counts:
            self.num_counts[number] += 1
        else:
            self.num_counts[number] = 1

    def find(self, value):
        for num in self.num_counts.keys():
            comple = value - num
            if num != comple:
                if comple in self.num_counts:
                    return True
            elif self.num_counts[num] > 1:
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

# Complexity Analysis:

# Time Complexity:
# For the add(number) function: O(1), since it takes a constant time to update an entry in hashtable.
# For the find(value) function: O(N), where N is the total number of unique numbers. In the worst case, we would iterate through the 
# entire table.
# Space Complexity: O(N), where N is the total number of unique numbers that we will see during the usage of the data structure.