#Write a function to implement F = (a+b-c)*(d-e+K) where all of the numbers are passed as parameters.
#However your function should not work unless the names of parameters are passed.
#That is if I call F(1,2,3,4,5,6) it should throw an error, rather it should work only when F(a=1,b=2,c=3…) is called.

def funcF(*,a,b,c,d,e,k):
    return (a+b-c)*(d-e+k)

print(funcF(a=2,b=3,c=4,d=3,e=5,k=6))
