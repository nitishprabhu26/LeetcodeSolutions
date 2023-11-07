# Approach Brutefore: Using lists
# Using lists works due to small input size, may not work for large array inputs.


from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        for sandwich in sandwiches:
            if sandwich in students:
                while sandwich != students[0]:
                    x = students.pop(0)
                    students.append(x)
                students.pop(0)
            else:
                break
        return len(students)
        

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
obj = Solution()
print(obj.countStudents(students, sandwiches))


# Complexity Analysis:
# Let N be the length of students and sandwiches.
# Time Complexity: O(N^2), in the worst case, because of iterating n * n.
# Space complexity : O(1), No extra space used.