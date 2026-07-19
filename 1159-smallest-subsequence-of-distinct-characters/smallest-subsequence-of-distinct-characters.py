class Solution:
    def smallestSubsequence(self, strIn_: str) -> str:
        
        # Store the rightmost index for each character
        lastPosPerChr = {chr: idx for idx, chr in enumerate(strIn_)}

        # Track characters currently in the result to ensure uniqueness
        isPresentChr = set()
        # Output string acting as a conditionally monotonic stack
        strOut_ = []

        for idx, chr in enumerate(strIn_):
            if chr in isPresentChr:
                continue

            # Maintain lexicographical order by removing larger trailing
            # characters if they are guaranteed to appear again later
            while (strOut_ and strOut_[-1] > chr and
                   lastPosPerChr[strOut_[-1]] > idx
            ):
                isPresentChr.remove(strOut_.pop())

            strOut_.append(chr)
            isPresentChr.add(chr)

        return "".join(strOut_)