class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        elif x >= 0 and x < 10:
            return True

        # 121
        # 3 digits
        # digits = 2

        else:
            
            digits = int(math.log10(x))
            exponent = digits
            y = x
            
            digit_array = []
            while exponent >= 0:
                print(exponent)
                print(10 ** exponent)
                value = y // 10 ** exponent
                y = y - (value * 10 ** exponent)
                digit_array.append(value)
                exponent -= 1
            print(digit_array)
            
            length = len(digit_array)

            # 0...2 if len is 5
            # 0...4
            # 1...3
            # 2...2
            for n in range(length//2):
                if digit_array[n] != digit_array[length-1-n]:
                    return False
            return True
            

