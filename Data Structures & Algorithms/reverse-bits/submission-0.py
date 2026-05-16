class Solution:
    def reverseBits(self, n: int) -> int:
        # n = len(reverse)
        n = bin(n)[2:].zfill(32)
        print(n)
        reverse = n[::-1]
        print(reverse)
        return int(reverse, 2)
        # n = str(n)
        # print(n)
        # total = 0
        # i = 1
        # print(len(n))

        # for num in reversed(n):
        #     if num == "1":
        #         total += 2 ** (len(n)-i)
        #         print(total)
        #     i += 1
            
        # return total
        # # for i, num in enumerate(reverse, -1):
        # #     if 