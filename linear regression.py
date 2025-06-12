#linear regression.py

import parameters
import solvinglinearequations
class LinearRegression:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def xy(self):
        return self.x*self.y
    def xsqr(self):
        return self.x**2
    def __str__(self):
        return f"({self.x}, {self.y})"

p1=LinearRegression(2,8)
p2=LinearRegression(3,12)
p3=LinearRegression(4,15)
p4=LinearRegression(5,20)
points=[p1,p2,p3,p4]
n,sumx,sumxsqr,sumy,sumxy=parameters.calculate_regression_params(points)
print("for this linear regression we have: ")
for i in points:
    print(i)
print(f"sum of x: {sumx}")
print(f"sum of y: {sumy}")
print(f"sum of xy: {sumxy}")
print(f"sum of xsqr: {sumxsqr}")
a,b=solvinglinearequations.lrg(n,sumx,sumxsqr,sumy,sumxy)
print(f"a: {round(a,2)}")
print(f"b: {round(b,2)}")
x=int(input("enter the value of x : "))
y=a+b*x
print(f"for this value of x, as per linear regression the value of y is {round(y,2)}")