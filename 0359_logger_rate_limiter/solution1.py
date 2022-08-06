# Approach 1: Queue + Set

# We keep the incoming messages in a queue. In addition, to accelerate the check of duplicates, we use a set data 
# structure to index the messages.

# Algorithm:
# 1.First of all, we use a queue as a sort of sliding window to keep all the printable messages in certain time 
#   frame (10 seconds).
# 2.At the arrival of each incoming message, it comes with a timestamp. This timestamp implies the evolution of 
#   the sliding windows. Therefore, we should first invalidate those expired messages in our queue.
# 3.Since the queue and set data structures should be in sync with each other, we would also remove those expired 
#   messages from our message set.
# 4.After the updates of our message queue and set, we then simply check if there is any duplicate for the new 
#   incoming message. If not, we add the message to the queue as well as the set.


from collections import deque

class Logger:
    def __init__(self):
        self._msg_set = set()
        self._msg_queue = deque()
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self._msg_queue:
            msg, ts = self._msg_queue[0]
            if timestamp - ts >= 10:
                self._msg_queue.popleft()
                self._msg_set.remove(msg)
            else:
                break
        
        if message not in self._msg_set:
            self._msg_set.add(message)
            self._msg_queue.append((message, timestamp))
            return True
        else:
            return False
        

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

# Input:
# ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", 
# "shouldPrintMessage", "shouldPrintMessage"]
# [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]


# As one can see, the usage of set data structure is not absolutely necessary. One could simply iterate the message 
# queue to check if there is any duplicate.
# Another important note is that if the messages are not chronologically ordered then we would have to iterate 
# through the entire queue to remove the expired messages, rather than having early stopping. Or one could use 
# some sorted queue such as Priority Queue to keep the messages.


# Complexity Analysis:
# Time Complexity: O(N) where N is the size of the queue. In the worst case, all the messages in the queue become 
# obsolete. As a result, we need clean them up.
# Space Complexity: O(N) where N is the size of the queue. We keep the incoming messages in both the queue and 
# set. The upper bound of the required space would be 2N, if we have no duplicate at all.