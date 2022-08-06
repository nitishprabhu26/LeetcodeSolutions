# Approach 2: Hashtable / Dictionary

# Intuition:
# One could combine the queue and set data structure into a hashtable or dictionary, which gives us the capacity of 
# keeping all unique messages as of queue as well as the capacity to quickly evaluate the duplication of messages 
# as of set.
# The idea is that we keep a hashtable/dictionary with the message as key, and its timestamp as the value. 
# The hashtable keeps all the unique messages along with the latest timestamp that the message was printed.

# Algorithm:
# 1.We initialize a hashtable/dictionary to keep the messages along with the timestamp.
# 2.At the arrival of a new message, the message is eligible to be printed with either of the two conditions as 
#   follows:
#   case 1). we have never seen the message before.
#   case 2). we have seen the message before, and it was printed more than 10 seconds ago.
# 3.In both of the above cases, we would then update the entry that is associated with the message in the hashtable, 
#   with the latest timestamp.


class Logger:
    def __init__(self):
        self._msg_dict = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self._msg_dict:
            # case 1). add the message to print
            self._msg_dict[message] = timestamp
            return True

        if timestamp - self._msg_dict[message] >= 10:
            # case 2). update the timestamp of the message
            self._msg_dict[message] = timestamp
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


# The main difference between this approach with hashtable and the previous approach with queue is that in previous 
# approach we do proactive cleaning, i.e. at each invocation of function, we first remove those expired messages.
# While in this approach, we keep all the messages even when they are expired. This characteristics might become 
# problematic, since the usage of memory would keep on growing over the time. Sometimes it might be more desirable 
# to have the garbage collection property of the previous approach.


# Complexity Analysis:
# Time Complexity: O(1). The lookup and update of the hashtable takes a constant time.
# Space Complexity: O(M) where M is the size of all incoming messages. Over the time, the hashtable would have an 
# entry for each unique message that has appeared.