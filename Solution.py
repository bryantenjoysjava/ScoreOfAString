class Solution(object):
    def scoreOfString(self, s):
        string_orders = []
        for character in s:
            string_orders.append(ord(character))
        sum = 0
        for i in range(len(string_orders) - 1):
            sum += abs(string_orders[i] - string_orders[i + 1])
        return sum


