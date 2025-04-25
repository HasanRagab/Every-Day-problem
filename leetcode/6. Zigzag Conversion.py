class Solution(object):
    def wave_value(self, num: int, index: int) -> int:
        wave_length = 2 * num

        position = index % wave_length

        if position <= num:
            return position
        else:
            return wave_length - position


    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        strings = ["" for _ in range(numRows)]
        for i in range(len(s)):
            level = self.wave_value(numRows - 1, i)
            strings[level] += s[i]
        return "".join(strings)


print(Solution().convert("A", 1))


# def wave_value(num, index):
#     # Calculate the position in the pattern
#     pos = index % (2 * num)  # Find the position in the 0 to 2 * num range
#     return num - abs(num - pos)  # Adjust the position to return the correct value
