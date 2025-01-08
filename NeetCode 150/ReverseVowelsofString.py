class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        # sv = []
        # for i in s:
        #     if i in vowels:
        #         sv.append(i)
        # sv=sv[::-1]
        # pointer = 0
        # result = ""
        # for i in s:
        #     if i in vowels:
        #         result = result+sv[pointer]
        #         pointer +=1
        #     else:
        #         result = result+i
        
        # return result

        s = list(s)

        left = 0
        right = len(s)-1

        while left < right:
            while left < right and s[left] not in vowels:
                left +=1
            while left < right and s[right] not in vowels:
                right -=1

            s[left],s[right] = s[right],s[left]
            

            left +=1
            right -=1

        return "".join(s)        