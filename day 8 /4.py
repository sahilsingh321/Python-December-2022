import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height,width,cover):
    surface_area = height*width;
    no_of_cans = surface_area / cover;
    print(f"So the total no of cans you need to purchase is   >   {math.floor(no_of_cans)} cans ");
paint_calc(height=test_h, width=test_w, cover=coverage)