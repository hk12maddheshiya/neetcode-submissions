from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for string in strs:
            encoded.append(str(len(string)))
            encoded.append("#")
            encoded.append(string)

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            # Find the delimiter separating the length from the string.
            delimiter = s.find("#", i)

            # Convert the length portion to an integer.
            length = int(s[i:delimiter])

            # Move past the delimiter.
            start = delimiter + 1
            end = start + length

            # Extract exactly `length` characters.
            decoded.append(s[start:end])

            # Continue decoding after the current string.
            i = end

        return decoded