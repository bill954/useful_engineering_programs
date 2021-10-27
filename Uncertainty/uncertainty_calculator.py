import sympy as sym
import math

# declare variables for the function
x, y, z = sym.symbols('x y z')

# declare the function
f = 3.14 * x**2 * y

# declare x values (data points)
x1 = 10
x2 = 5
x3 = 0
# declare sigma values of each data point
sigma1 = 0.5
sigma2 = 0.1
sigma3 = 0

# find partial derivatives of the function
derivative_x = f.diff(x)
print('Derivative df/dx:', derivative_x)

derivative_y = f.diff(y)
print('Derivative df/dy:', derivative_y)

derivative_z = f.diff(z)
print('Derivative df/dz:', derivative_z)

# evaluate each derivative with the given x values
df_dx = derivative_x.evalf(subs={x: x1, y: x2, z: x3})
df_dy = derivative_y.evalf(subs={x: x1, y: x2, z: x3})
df_dz = derivative_z.evalf(subs={x: x1, y: x2, z: x3})
print('df/dx1:', df_dx)
print('df/dx2:', df_dy)
print('df/dx3:', df_dz)

# 
summ = df_dx**2 * sigma1**2 + df_dy**2 * sigma2**2 + df_dz**2 * sigma3**2

U_y = math.sqrt(summ)

print('U(y): ', round(U_y, 4))

Y = f.evalf(subs={x: x1, y: x2, z: x3})

print('Y(x1, x2, x3):', round(Y, 4))