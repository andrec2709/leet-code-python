"""
https://leetcode.com/problems/weighted-word-mapping/
"""


from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        final_word = ""
        
        for word in words:
            word_weight = 0
            
            for letter in word:
                letter_index = ord(letter[0]) - 97
                letter_weight = weights[letter_index]
                word_weight += letter_weight
                
            modulo_26 = word_weight % 26
            
            final_word += chr(122 - modulo_26)
        
        return final_word