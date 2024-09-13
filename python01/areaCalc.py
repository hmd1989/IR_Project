import math



print("Here we are goint to calculate Area of shapes ...");

class calculation:

        def circle_area(self,r):
                area = math.pi * math.pow(r,2)
                print("Circle area is : ", area)

        def rectangle_area(self,width,height):
                  area = width * height
                  print("Rectangle area is : ", area)

        def squars_area(self, width, height):
                  area= math.pow(width)
                  print("Squars area is : ", area)

