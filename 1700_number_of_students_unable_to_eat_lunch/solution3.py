# Approach: Using Counter

# Intuition:
# Count students' preference of food to a variable students_count
# Now we iterate the food one by one,
# and see if any one in the left students queue will take it.

# We stop at sandwiches[k] if no one wants it,
# then n - k students are unable to eat.


import collections
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_count = collections.Counter(students)

        n, k = len(students), 0
        while k < n and students_count[sandwiches[k]]:
            students_count[sandwiches[k]] -= 1
            k += 1

        return n - k
        

# OR
# Intuition:
# We can distribute sandwich, if there is any student who wants that sandwich.
# So, we create a counter of students.
# And, iterate sandwiches, one by one, and check if there is any student left who wants that sandwich.
# If there is a student who wants that sandwich, we decrease counter by 1, 
# else we return count of students who want other kind of sandwich.


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_count = collections.Counter(students)
        for sandwich in sandwiches:
            if student_count[sandwich] > 0:
                student_count[sandwich] -= 1
            else:
                return student_count[not sandwich]
        return 0
    

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
obj = Solution()
print(obj.countStudents(students, sandwiches))


# Complexity Analysis:
# Let N be the length of students and sandwiches.
# Time Complexity: O(N).
# Space complexity : O(2).