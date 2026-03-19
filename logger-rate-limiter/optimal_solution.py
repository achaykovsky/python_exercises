from collections import deque


# https://gongybable.medium.com/google-microsoft-interview-question-leetcode-359-eb4d6106c2a2

# We have here 4 cases:
# 1. New message, time inside [t,t+10] - True
# 2. New message, time after [t,t+10] - True
# 3. Old message, time inside [t,t+10] - False
# 4. Old message, time after [t,t+10] - True


# Time Complexity: O(1) Space: O(n)
class Logger:
    def __init__(self):
        self.message_set = set()  # to check if a message exists in O(1)
        self.message_queue = deque()  # to keep track of the order of messages and their timestamps

    def should_print_message(self, timestamp: int, message: str) -> bool:
        # checking old messages:
        while self.message_queue:
            msg, ts = self.message_queue[0]  # the oldest message in the queue
            if timestamp - ts >= 10:  # if the question is older than 10, it can be removed,
                # because we won't need to validate it again, so we remove it both from the set and the queue
                self.message_queue.popleft()
                self.message_set.remove(msg)
            else:
                # the arrived messaged is in the [t,t+10] Interval, and should be validated for the message content
                break

        if message not in self.message_set:
            # a new message arrived
            self.message_set.add(message)
            self.message_queue.append((message, timestamp))
            return True
        else:
            # an old message arrived with the new time, but inside the Interval
            return False


if __name__ == '__main__':
    obj = Logger()
    print(obj.should_print_message(1, "foo"))
    print(obj.should_print_message(2, "bar"))
    print(obj.should_print_message(3, "foo"))
    print(obj.should_print_message(8, "bar"))
    print(obj.should_print_message(10, "foo"))
    print(obj.should_print_message(11, "foo"))
