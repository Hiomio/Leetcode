class Solution:
    def mapWordWeights(self, words, weights):
        table = {chr(97 + i): w for i, w in enumerate(weights)}

        return "".join(
            chr(122 - (s % 26))
            for s in (
                sum(table[ch] for ch in word)
                for word in words
            )
        )