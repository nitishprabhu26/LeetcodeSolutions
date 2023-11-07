# Approach: Converting input lists to deque
# This approach is more efficient than lists
# https://youtu.be/yOfZ80BcUXE?si=VAVWj5ZlO3uMwGDN

import collections
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_deque = collections.deque(students)

        for sandwich in sandwiches:
            if sandwich in student_deque:
                while sandwich != student_deque[0]:
                    x = student_deque.popleft()
                    student_deque.append(x)
                student_deque.popleft()
            else:
                break
        return len(student_deque)
    
# OR

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_deque = collections.deque(students)
        sandwiches_deque = collections.deque(sandwiches)

        while sandwiches_deque:
            student = students_deque[0]
            if student == sandwiches_deque[0]:
                students_deque.popleft()
                sandwiches_deque.popleft()
            else:
                if sandwiches_deque[0] not in students_deque:
                    break

                students_deque.popleft()
                students_deque.append(student)

        return len(students_deque)

        

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
obj = Solution()
print(obj.countStudents(students, sandwiches))


# Complexity Analysis:
# Let N be the length of students and sandwiches.
# Time Complexity: O(N^2), in the worst case, because of iterating n * n.
# Space complexity : O(n) because of converting lists into deques.