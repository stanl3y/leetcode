from operator import mul 
from functools import reduce
import re

class Solution(object):
    """ Solution for Leetcode problem 91: Decode Ways. """

    def num_decodings(self, string):
        """Find no. of ways to convert a sequence of nums to letters."""
        
        if not string: return 0

        symbols = self.extract_symbols_efficient(string)

        # alternatively EITHER
        # segments = self.extract_segments(string)
        # symbols = self.segments_to_symbols(segments)

        # alternatively OR  
        # segments = self.extract_segments_regex(string)
        # symbols = self.segments_to_symbols(segments)

        num_decodings = self.calc_decodings(symbols)
        return num_decodings

    def calc_decodings(self, symbols):
        """Given symbols, count the ways to decode them. """

        if not symbols: return 0

        # process symbols
        symbols = "".join(symbols)
        segm_lens = [len(x) for x in symbols.split("x")]

        # calculate the required no. of Fibonacci terms
        fib = [1,1]
        for _ in range(max(segm_lens)):
            fib.append(fib[-1] + fib[-2])

        # if (F_1, F_2, F_3 ...) = (1, 1, 2)
        # then n dashes ~ F_(n+2) options ~ fib[n+1]
        segm_ways = [fib[n+1] for n in segm_lens]

        return reduce(mul, segm_ways)

    def extract_segments_regex(self, string):
        """Split the input into independent blocks using RE. """

        # zeros always need a digit in front (1 or 2)
        if re.search('^0', string) or re.search('00', string): return []

        zeros_occur = re.findall('[1-9]0', string)
        if zeros_occur and not set(zeros_occur) < set(['10', '20']): return []

        # split into independent segments
        return re.split('[1-9]0', string)


    def extract_segments(self, string):
        """Split the input into independent blocks. """

        segments, symbols = [], []
        slow = 0

        # note that zeros split string into independent segments
        # (zero must have a digit in front, cannot have 0 or 01)
        for i in range(len(string)):
            if string[i] == "0":
                if i-1 >= 0 and int(string[i-1:i+1]) in [10,20]:
                    segments.append(string[slow:i-1])
                    slow = i+1
                else: return [] 
            if i == len(string) - 1:
                segments.append(string[slow : len(string)])

        return segments



    def segments_to_symbols(self, segments):
        """Convert segments to symbols '-' and 'x'. 

        Translate segments as 
            "-" if two consecutive digits can be joined 
            "x" otherwise
        """
        symbols = []

        for segment in segments:
            for i in range(1, len(segment)):
                symbols.append( "-" if 11 <= int(segment[i-1:i+1]) <= 26 else "x")
            symbols.append("x") # segments are independent
        
        return symbols




    def extract_symbols_efficient(self, string):
        """Convert input to symbols (efficient method). 

        Translate segments as 
            "-" if two consecutive digits can be joined 
            "x" otherwise
        """

        symbols = []
        i = len(string) - 1

        # going backwards, check all pairs
        while i > 0:
            current_pair = int(string[i-1:i+1])

            if not string[i] == "0":
                symbols.append("-" if 11 <= current_pair <= 26 else "x")
                i -= 1
            else:
                if current_pair in [10,20]:
                    symbols.append("xx")
                    i -= 2
                else:
                    return 0

        # and check also the first element
        if string[0] == "0": return []
        else: symbols.append("x")

        return symbols



import unittest

class ProblemTest(unittest.TestCase):
    """ Tests for Leetcode problem 91: Decode Ways. """
    
    def test(self):
        self.assertEqual(0, Solution().num_decodings(""))
        self.assertEqual(5, Solution().num_decodings("1111"))
        self.assertEqual(15, Solution().num_decodings("1119111"))
        self.assertEqual(5, Solution().num_decodings("11234"))
        
        self.assertEqual(0, Solution().num_decodings("0"))
        self.assertEqual(0, Solution().num_decodings("11130"))
        self.assertEqual(2, Solution().num_decodings("11201"))
        self.assertEqual(1, Solution().num_decodings("1"))


if __name__ == '__main__':
    unittest.main()