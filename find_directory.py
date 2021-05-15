from os import listdir as ls, path as p

def find_directory(start):
    print(p.abspath(start))
    while True:
        print(ls(start))
        move = input("Input how to move: [.. or filename or stay]")
        if move == "..":
            start = ("\\").join(p.abspath(start).split("\\")[:-1])
        elif move == "stay":
            return start
        elif (p.isdir(start + "\\" + move)):
            start += "\\" + move
        else:
            print("Not valid")
        print(p.abspath(start))

#find_directory(".")
