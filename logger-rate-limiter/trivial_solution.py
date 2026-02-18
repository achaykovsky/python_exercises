from collections import defaultdict

# https://gongybable.medium.com/google-microsoft-interview-question-leetcode-359-eb4d6106c2a2

# Time Complexity: O(1)
# Space: O(n)
class Logger:
    def __init__(self):
        self.message_dict = defaultdict()

    def should_print_message(self, timestamp: int, message: str) -> bool:
        if message not in self.message_dict:
            self.message_dict[message] = timestamp
            return True
        if timestamp - self.message_dict[message] >= 10:
            self.message_dict[message] = timestamp
        else:
            return False
        return True


# To make it thread-safe:
# 1. add self.lock = threading.Lock() in the init
# 2. add with self.lock inside the function

# class Logger:
#     def __init__(self):
#         self.message_dict = defaultdict()
#         self.lock = threading.Lock()
#
#     def should_print_message(self, timestamp: int, message: str) -> bool:
#       with self.lock:
#         if message not in self.message_dict:
#             self.message_dict[message] = timestamp
#             return True
#         if timestamp - self.message_dict[message] >= 10:
#             self.message_dict[message] = timestamp
#         else:
#             return False


if __name__ == '__main__':
    obj = Logger()
    print(obj.should_print_message(1, "foo"))
    print(obj.should_print_message(2, "bar"))
    print(obj.should_print_message(3, "foo"))
    print(obj.should_print_message(8, "bar"))
    print(obj.should_print_message(10, "foo"))
    print(obj.should_print_message(11, "foo"))
