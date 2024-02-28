class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common_string = ''

        min_word = min(strs, key=len)
        print(min_word)
        min_word_length = len(min_word)

        for letter_index in range(min_word_length):
            all_is_equal = True
            for string in strs:
                if min_word[letter_index] == string[letter_index]:
                    continue
                else:
                    all_is_equal = False
            if all_is_equal:
                common_string = f'{common_string}{min_word[letter_index]}'
            else:
                break

        return common_string
