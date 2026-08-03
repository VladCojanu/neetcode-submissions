class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        # print("decoding:", s)
        while s != "":
            len_str, remainder = s.split("#", 1)
            # print("splits: ", len_str, " remainder: ", remainder)
            len_str = int(len_str)
            # print('appending result: ', remainder[:len_str])
            result.append(remainder[:len_str])
            s = remainder[len_str:]

        return result