"""
Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.
"""
if __name__ == "__main__":
    print("Please enter your firstname and lastname:")
    name = input().split(" ")
    print("Reverse of your name is:", end=" ")
    for index in range(len(name)-1, -1, -1):
        print(name[index], end=" ")
