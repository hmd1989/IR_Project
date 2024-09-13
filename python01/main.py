import math

import module
import areaCalc
import calculator

object1=module.GFG()
object2=calculator.my_calculator()
object=areaCalc.calculation()

# Calling and printing class methods
print(object1.add(15, 5))
print(object1.sub(15, 5))
print("--------------------------------------------------------")
print(object.circle_area(9))

print(object2.subtract(20,30))
print(object2.add(20,30))
print(object2.divide(20,0))


