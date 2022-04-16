class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        needle = list(needle)
        haystack = list(haystack)
        index = 0
        while haystack:
            if haystack[:needle_len] == needle:
                break
            haystack = haystack[1:]
            index += 1
            if not haystack:
                index = -1
        return index
