import numpy

class Solution(object):
    """ Solution for Leetcode problem 49: Group Anagrams. """

    def group_anagrams(self, words):
        """Group anagrams in a given list of strings.

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

    def group_anagrams_alter(self, words):
        """ Group anagrams (alternative solution). """
        
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

        answer = Solution().group_anagrams(words)
        sorted_answer = sorted([sorted(x) for x in answer])
        sorted_expect = sorted([sorted(x) for x in expect])

        self.assertEqual(sorted_expect, sorted_answer)

if __name__ == '__main__':
    unittest.main()