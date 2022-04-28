class Solution:
    """

    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()
        for str_ in strs:
            sorted_str = ''.join(sorted(str_))
            if sorted_str not in anagram_dict:
                anagram_dict[sorted_str] = list()
            anagram_dict[sorted_str].append(str_)

        return [v for k, v in anagram_dict.items()]
