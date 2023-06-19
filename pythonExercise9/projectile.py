import math
pi = math.pi
angle = float(input (" enter angle:"))
theta = (angle) * (pi/180)
tan = float(math.tan(theta))
cos = float(math.cos(theta))
print ("pi=",pi)

y0= float(input ("enter gun barrel height:"))
x = float(input ("enter horizontal distance travelled:"))
v0 = float(input (" enter intial velocity:"))

print ("radons",theta)
print ("cos theta",cos)
print ("tan theta",tan)

y= y0 + x * tan - 9.81 * (x**2)/(2 *(v0 *cos))**2


print ("height of projectile=",y)