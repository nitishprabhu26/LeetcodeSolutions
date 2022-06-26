# Approach 1: Heap
# In Python there is a method nlargest in heapq library which has the same O(N.logk) time complexity and reduces 
# the code to one line.

# In other languages, https://leetcode.com/problems/kth-largest-element-in-an-array/solution/
# The idea is to init a heap "the smallest element first", and add all elements from the array into this heap one 
# by one keeping the size of the heap always less or equal to k. That would results in a heap containing k largest 
# elements of the array.
# The head of this heap is the answer, i.e. the kth largest element of the array.
# The time complexity of adding an element in a heap of size k is O(logk), and we do it N times that means O(Nlogk) 
# time complexity for the algorithm.

# https://www.geeksforgeeks.org/priorityqueue-poll-method-in-java/#:~:text=poll()%20method%20in%20Java%20is%20used%20to%20retrieve%20or,if%20the%20queue%20is%20empty.
# The java.util.PriorityQueue.poll() method in Java is used to retrieve or fetch and remove the first element of 
# the Queue or the element present at the head of the Queue. The peek() method only retrieved the element at the 
# head, but the poll() also removes the element along with the retrieval. It returns NULL if the queue is empty.


""" class Solution {
    public int findKthLargest(int[] nums, int k) {
        // init heap to 'the smallest element first'- keeps the queue in ascending order.
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>((n1, n2) -> n1 - n2);

        // keep k largest elements in the heap
        for (int n: nums) {
          heap.add(n);
          if (heap.size() > k)
            heap.poll();
        }

        // output
        return heap.poll();        
  }
} """


import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


nums = [3,2,3,1,2,4,5,5,6]
k = 4
obj = Solution()
print(obj.findKthLargest(nums, k))


# Complexity Analysis:
# Time complexity : O(N.logk).
# Space complexity : (k) to store the heap elements.