import numpy

class Solution(object):
    """ Solution for Leetcode problem 49: Group Anagrams. """

    def groupAnagrams(self, words):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        groups = {}

        for word in words:
            freq = {}

            for let in word:
                freq[let] = freq.get(let,0) + 1

            freq_tuple = tuple(freq.get(let,0) for let in alphabet)
            groups.setdefault(freq_tuple, []).append(word)

        return list(groups.values())

    def groupAnagrams_alter(self, words):
        groups = {}

        for word in words:
            freq = numpy.zeros(26)
            for let in word:
                freq[ord(let) - 97] += 1
            groups.setdefault(tuple(freq), []).append(word)

        return list(groups.values())

        
import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 49: Group Anagrams. """
    
    def test(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expect = [
            ["ate", "eat","tea"],
            ["nat","tan"],
            ["bat"] 
        ]

        answer = Solution().groupAnagrams(words)

        sorted_answer = sorted([sorted(x) for x in answer])
        sorted_expect = sorted([sorted(x) for x in expect])

        self.assertEqual(sorted_expect, sorted_answer)

if __name__ == '__main__':
    unittest.main()