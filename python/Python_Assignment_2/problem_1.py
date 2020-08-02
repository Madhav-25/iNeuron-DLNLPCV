"""
Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

if __name__ == "__main__":
    symbol = "*"
    count_of_rows = 10
    count = 0
    for i in range(1, count_of_rows + 1):
        if (i <= int(count_of_rows/2)):
            count = i
        else:
            count = count_of_rows - i
        for j in range(count):
            print(symbol, end=" ")
        print(" ")
