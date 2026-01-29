class Solution:
    def task(self,a):
        total = 0
        length = len(a)
        for  x in range(length):
            if type(a[x]) == int:
                if a[x] % 5 == 0:
                    total += a[x]
        return total

if __name__ == "__main__":
    s = Solution()
    y = [5,10,15, 18,25, 'python']
    print(f"ans={s.task(y)}")


    a = ["python", "", None, "java", 4,4]
    print(f"a's answer = {a[-1]+a[-2]}")

    b = [5,6,7,8,9,10,1,2,3,4]
    b.sort()
    print(f"b's answer = {b}")


    c = ["hello", "my", "name", "is"]
    name = input("enter your name").strip()
    c.append(name)
    string = ""
    for x in c:
        string += x[0]
    print(f"c's result={string}")

 