import math
def get_input():
    x1=input("x1: ")
    x2=input("x2: ")
    x3=input("x3: ")
    y1=input("y1: ")
    y2=input("y2: ")
    y33=find_y3(x1, x2, x3, y1, y2)

def find_y3 (x1, x2, x3, y1, y2):
    y3=((x3-x2)/(x2-x1)*(y2-y1)+y2)
    return y3


if __name__ == "__main__":
    get_input()
    