class Solution:
    def check_palindrome(self,s:str)->bool:
        length = len(s)
        n, m  = 0, length - 1
        i = 0
        while n < m:
            if s[n] == s[m]:
                n+=1
                m-=1
            else:
                return False
        return True


    def check_odd_even(self,number:int) -> str:
        if number % 2 == 0: return "Even" 
        else: return "Odd"


if __name__ == "__main__":
    s = Solution()
    string_vlu = input("Enter the string to check palindrome:")
    number_vlu = input("Enter the number to check odd/even:")

    print(f"{string_vlu} is palindrome: {s.check_palindrome(string_vlu)} ")
    print(f"{number_vlu} is odd/even: {s.check_odd_even(int(number_vlu))}")