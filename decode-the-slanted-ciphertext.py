import pytest

class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        cols = int(len(encodedText)/rows)
        decodedText = []

        for i in range(cols):
            for j in range(rows):
                if i+j >= cols: break
                decodedText.append(encodedText[j * cols + (i + j)])

        return "".join(decodedText).rstrip()

def test():
    s = Solution()
    assert s.decodeCiphertext("ch   ie   pr", 3) == "cipher"
    assert s.decodeCiphertext("iveo    eed   l te   olc", 4) == "i love leetcode"
    assert s.decodeCiphertext("coding", 1) == "coding"
