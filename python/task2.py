class solutions:
    pass

if __name__ == "__main__":
    # try:
    #     no_of_student = int(input("Enter the number of students:\t"))
    # except ValueError:
    #     print("Number of students should be an integer")
    #     exit()

    # marks_record = dict() 
    # for i in range(1,no_of_student+1):
    #     name = input(f"Enter the name of student {i}:\t").strip()
    #     marks = input(f"Enter marks for (Python, C#, c++) respectively for student number {i}: \t").strip()

    #     marks_list = marks.split()
    #     if len(marks_list) != 3:
    #         print("Enter  (Python, C#, c++) subjects marks!")
    #         exit()
        
    #     try:
    #         Python, C_sharp, C_plus  = int(marks_list[0]), int(marks_list[1]), int(marks_list[2])
    #     except ValueError:
    #         print("Marks should be integer.")
    #         exit()

    #     marks_record[f"{name}_{i}"] = {
    #         "Python":Python,
    #         "C#":C_sharp,
    #         "C++":C_plus
    #     }

    # print(marks_record)
    
    # for i in range(1,15):
    #     if  i < 15:
    #         if i == 5:
    #             continue
    #         print(i)

    # for i in range(5,55,5):
    #     print(i)

    # a = ["a","b","c","d","e",4,5,6,7,8,"python"]
    # for x in range(len(a)):
    #     print(f"{a[x]} is {type(a[x])}")

    # b = [1,2,3,4,'',6,7]
    # idx = 0
    # for r in b:
    #     if r == '':
    #         break
    #     idx+=1
    # print(b[0:idx])

    a = [4,5,6,7,8,9,30,35,40]
    for x in range(len(a)):
        if a[x] % 5 == 0:
            print(x)









