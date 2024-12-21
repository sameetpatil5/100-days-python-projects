from math import ceil

def paint_cal(height, width, cover):
    print("You'll need" + str(ceil((height*width)/cover)) + "cans of paint")

test_h = int(input("Height of the wall:"))
test_w = int(input("Width of the wall:"))
coverage = 5
paint_cal(height=test_h, width=test_w, cover=coverage)