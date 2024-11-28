#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Problem 1
"""
Maximizing Profit for a Factory
A factory produces two types of products, A and B. Each unit of product A requires 2 
hours of machine time and 1 unit of raw material, while each unit of product B requires 
3 hours of machine time and 2 units of raw material. The factory has a total of 12 hours 
of machine time and 8 units of raw material available each day.
The profit from each unit of product A is N3, and the profit from each unit of product B
is N4. Maximize the total profit.
"""



# Define the constraints
x = np.linspace(0, 10, 200)  # x-axis values
y1 = (12 - 2 * x) / 3  # From 2x + 3y <= 12
y2 = (8 - x) / 2       # From x + 2y <= 8

# Non-negativity constraint
y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)

# Plot the constraints and feasible region
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r"$2x + 3y \leq 12$", color="blue")
plt.plot(x, y2, label=r"$x + 2y \leq 8$", color="green")
plt.fill_between(x, 0, np.minimum(y1, y2), color="gray", alpha=0.3, label="Feasible Region")

# Highlight the optimal solution
plt.scatter(6, 0, color='red', zorder=5, label="Optimal Solution (6, 0)")
plt.text(6, 0.2, "(6, 0)", color='red')

# Labels and title
plt.xlim(0, 6.5)
plt.ylim(0, 5)
plt.xlabel("Units of Product A (x)")
plt.ylabel("Units of Product B (y)")
plt.title("Feasible Region with Optimal Solution")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.grid()

# Show the plot
plt.show()


# In[5]:


# Problem 2
# Define the constraints for the given problem
"""
Minimizing Cost for a Manufacturer
A company manufactures two types of products, X and Y, using two resources: labor 
and materials. Each unit of product X requires 1 hour of labor and 2 units of material, 
while each unit of product Y requires 2 hours of labor and 1 unit of material. The 
company has a total of 6 hours of labor and 5 units of material available.
The cost of producing each unit of product X is N2, and the cost of producing each unit 
of product Y is N5. Minimize the total production cost.
"""

x = np.linspace(0, 10, 200)  # x-axis values

# Constraints
y1 = (6 - x) / 2  # From x + 2y <= 6
y2 = (5 - 2 * x)  # From 2x + y <= 5

# Non-negativity constraint
y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r"$x + 2y \leq 6$", color="blue")
plt.plot(x, y2, label=r"$2x + y \leq 5$", color="green")
plt.fill_between(x, 0, np.minimum(y1, y2), color="gray", alpha=0.3, label="Feasible Region")

# Labels and title
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.xlabel("Units of Product X (x)")
plt.ylabel("Units of Product Y (y)")
plt.title("Feasible Region for Minimizing Cost")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.grid()

plt.show()



# In[ ]:


# Problem 3
"""
Maximizing Production with Multiple Resources
A factory produces two types of products, A and B, using three resources: labor, material, 
and machine time. Each unit of product A requires 2 hours of labor, 3 units of material, 
and 1 hour of machine time. Each unit of product B requires 1 hour of labor, 2 units of 
material, and 2 hours of machine time. The company has 20 hours of labor, 30 units of 
material, and 18 hours of machine time available. The profit for each unit of product A is 
N5, and the profit for each unit of product B is N4. Maximize the total profit.
"""

# Define the constraints
x = np.linspace(0, 15, 200)  # x-axis values

# Constraints
y1 = (20 - 2 * x)  # From 2x + y <= 20
y2 = (30 - 3 * x) / 2  # From 3x + 2y <= 30
y3 = (18 - x) / 2  # From x + 2y <= 18

# Non-negativity constraint
y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)
y3 = np.maximum(0, y3)

# Plot the constraints and feasible region
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r"$2x + y \leq 20$", color="blue")
plt.plot(x, y2, label=r"$3x + 2y \leq 30$", color="green")
plt.plot(x, y3, label=r"$x + 2y \leq 18$", color="red")
plt.fill_between(x, 0, np.minimum(np.minimum(y1, y2), y3), color="gray", alpha=0.3, label="Feasible Region")

# Labels and title
plt.xlim(0, 10)
plt.ylim(0, 12)
plt.xlabel("Units of Product A (x)")
plt.ylabel("Units of Product B (y)")
plt.title("Maximizing Production with Multiple Resources")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.grid()

# Show the plot
plt.show()


# In[7]:


#Problem 4
"""
Maximizing Revenue from Sales
A company sells two products, A and B, and has a limited amount of advertising budget 
and production capacity. Each unit of product A brings in N4, and each unit of product 
B brings in N5. The company has a total advertising budget of N20 and a production 
capacity of 15 units. The advertisement cost for each unit of product A is N1, and the 
advertisement cost for each unit of product B is N2. Each unit of product A requires 1 
unit of production capacity, while each unit of product B requires 2 units of production 
capacity. Maximize the total revenue
"""

import numpy as np
import matplotlib.pyplot as plt

# Define constraints
x = np.linspace(0, 20, 400)  # Range for x values
y1 = 15 - x  # From x + y <= 15
y2 = (20 - x) / 2  # From x + 2y <= 20

# Feasible region
y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r"$x + y \leq 15$", color="blue")
plt.plot(x, y2, label=r"$x + 2y \leq 20$", color="green")
plt.fill_between(x, 0, np.minimum(y1, y2), color="gray", alpha=0.3, label="Feasible Region")

# Highlight vertices
vertices = [(0, 10), (10, 5), (15, 0)]
for vx, vy in vertices:
    plt.scatter(vx, vy, color='red', zorder=5)
    plt.text(vx, vy, f"({vx}, {vy})", color='red', fontsize=10)

# Optimal point
plt.scatter(10, 5, color="purple", label="Optimal Solution (10, 5)", zorder=6)

# Labels and formatting
plt.title("Maximizing Revenue for Products A and B")
plt.xlabel("Units of Product A (x)")
plt.ylabel("Units of Product B (y)")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.legend()
plt.grid()

# Show plot
plt.show()


# In[5]:


#Problem 5
"""
Resource Allocation for Two Projects
A company is considering two projects, P1 and P2. Each project requires both labor 
hours and capital investment. Project P1 requires 3 labor hours and 2 units of capital, 
while project P2 requires 4 labor hours and 1 unit of capital. The company has a total of 
12 labor hours and 6 units of capital available.
The profit from project P1 is N8 per unit, and the profit from project P2 is N7 per unit.
Maximize the total profit
"""

import numpy as np
import matplotlib.pyplot as plt

# Define constraints
x = np.linspace(0, 4, 400)  # Range for x values
y1 = (12 - 3 * x) / 4  # From 3x + 4y <= 12
y2 = 6 - 2 * x  # From 2x + y <= 6

# Feasible region
y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r"$3x + 4y \leq 12$", color="blue")
plt.plot(x, y2, label=r"$2x + y \leq 6$", color="green")
plt.fill_between(x, 0, np.minimum(y1, y2), color="gray", alpha=0.3, label="Feasible Region")

# Highlight vertices
vertices = [(0, 3), (2.4, 1.2), (3, 0)]
for vx, vy in vertices:
    plt.scatter(vx, vy, color='red', zorder=5)
    plt.text(vx, vy, f"({vx:.1f}, {vy:.1f})", color='red', fontsize=10)

# Optimal point
plt.scatter(2.4, 1.2, color="purple", label="Optimal Solution (2.4, 1.2)", zorder=6)

# Labels and formatting
plt.title("Resource Allocation for Two Projects")
plt.xlabel("Units of Project P1 (x)")
plt.ylabel("Units of Project P2 (y)")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.legend()
plt.grid()

# Show plot
plt.show()


# In[9]:


#Problem 6
"""
Production Planning for a Bakery
A bakery produces two types of cakes, chocolate cakes and vanilla cakes. Each 
chocolate cake requires 1 hour of baking time and 3 units of flour, while each vanilla 
cake requires 2 hours of baking time and 2 units of flour. The bakery has a total of 8 
hours of baking time and 12 units of flour available. The bakery earns a profit of N5 for 
each chocolate cake and N3 for each vanilla cake. Maximize the total profit.

"""

import numpy as np
import matplotlib.pyplot as plt

# Define constraints
x = np.linspace(0, 8, 400)  # Range for x values
y1 = (8 - x) / 2  # From x + 2y <= 8
y2 = (12 - 3 * x) / 2  # From 3x + 2y <= 12

# Feasible region
y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r"$x + 2y \leq 8$", color="blue")
plt.plot(x, y2, label=r"$3x + 2y \leq 12$", color="green")
plt.fill_between(x, 0, np.minimum(y1, y2), color="gray", alpha=0.3, label="Feasible Region")

# Highlight vertices
vertices = [(0, 4), (2, 3), (4, 0)]
for vx, vy in vertices:
    plt.scatter(vx, vy, color='red', zorder=5)
    plt.text(vx, vy, f"({vx}, {vy})", color='red', fontsize=10)

# Optimal point
plt.scatter(4, 0, color="purple", label="Optimal Solution (4, 0)", zorder=6)

# Labels and formatting
plt.title("Maximizing Profit for Bakery Cakes")
plt.xlabel("Chocolate Cakes (x)")
plt.ylabel("Vanilla Cakes (y)")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.legend()
plt.grid()

# Show plot
plt.show()


# In[10]:


#Problem 7
"""
Minimizing Cost for a Transport Company
A transport company operates two types of vehicles, X and Y, to transport goods. 
Vehicle X requires 3 hours of fuel and 2 hours of driver time for each trip, while vehicle
Y requires 4 hours of fuel and 1 hour of driver time for each trip. The company has a 
budget that allows for 18 hours of fuel and 10 hours of driver time. The cost of using 
vehicle X is $6 per trip, and the cost of using vehicle Y is $7 per trip. Minimize the total 
cost.
"""

import numpy as np
import matplotlib.pyplot as plt

# Define constraints
x = np.linspace(0, 6, 400)  # Range for x values
y1 = (18 - 3 * x) / 4  # From 3x + 4y <= 18
y2 = 10 - 2 * x  # From 2x + y <= 10

# Feasible region
y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r"$3x + 4y \leq 18$", color="blue")
plt.plot(x, y2, label=r"$2x + y \leq 10$", color="green")
plt.fill_between(x, 0, np.minimum(y1, y2), color="gray", alpha=0.3, label="Feasible Region")

# Highlight vertices
vertices = [(0, 4.5), (4.4, 1.2), (5, 0)]
for vx, vy in vertices:
    plt.scatter(vx, vy, color='red', zorder=5)
    plt.text(vx, vy, f"({vx:.1f}, {vy:.1f})", color='red', fontsize=10)

# Optimal point
plt.scatter(5, 0, color="purple", label="Optimal Solution (5, 0)", zorder=6)

# Labels and formatting
plt.title("Minimizing Cost for Transport")
plt.xlabel("Trips by Vehicle X (x)")
plt.ylabel("Trips by Vehicle Y (y)")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.legend()
plt.grid()

# Show plot
plt.show()


# In[11]:


#Problem 8
"""
Maximizing Revenue from Two Products
A company manufactures two types of products, P1 and P2, and sells them at different 
prices. Product P1 requires 4 hours of labor, 1 unit of raw material, and 3 units of 
machine time to produce. Product P2 requires 3 hours of labor, 2 units of raw material, 
and 2 units of machine time. The company has 30 hours of labor, 18 units of raw 
material, and 24 units of machine time available. The revenue from selling each unit of
P1 is $10, and the revenue from selling each unit of P2 is $12.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Coefficients for the objective function (maximize revenue Z = 10x + 12y)
c = [-10, -12]  # Negatives because linprog minimizes

# Coefficients for the constraints
A = [[4, 3],   # 4x + 3y <= 30 (labor)
     [1, 2],   # x + 2y <= 18 (raw material)
     [3, 2]]   # 3x + 2y <= 24 (machine time)]
b = [30, 18, 24]

# Solve the linear program
result = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

# Extract solution
x_opt, y_opt = result.x
z_opt = -result.fun  # Negate the minimized result to get the maximized value

# Print results
print(f"Optimal solution: x = {x_opt:.2f}, y = {y_opt:.2f}, Revenue = {z_opt:.2f}")

# Plot constraints
x = np.linspace(0, 10, 400)
y1 = (30 - 4*x) / 3
y2 = (18 - x) / 2
y3 = (24 - 3*x) / 2

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r'$4x + 3y \leq 30$')
plt.plot(x, y2, label=r'$x + 2y \leq 18$')
plt.plot(x, y3, label=r'$3x + 2y \leq 24$')

# Feasible region
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), color='lightgrey', label='Feasible Region', alpha=0.5)

# Optimal solution point
plt.plot(x_opt, y_opt, 'ro', label=f'Optimal Solution: ({x_opt:.2f}, {y_opt:.2f})')

# Labels and legends
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('x (Units of P1)')
plt.ylabel('y (Units of P2)')
plt.title('Maximizing Revenue for Products P1 and P2')
plt.legend()
plt.grid()
plt.show()


# In[12]:


# Problem 9
"""
Advertising Campaign Budget Allocation
A company runs two advertising campaigns, A and B, using a budget allocated for 
television, print media, and social media. The company has a total of $10,000 to allocate 
across these campaigns, with the following constraints: Campaign A requires $4,000 for 
television, $2,000 for print media, and $1,000 for social media. Campaign B requires $3,000 
for television, $2,500 for print media, and $1,500 for social media. The company can spend 
no more than $5,000 on television, $4,500 on print media, and $3,000 on social media.
The company wants to maximize the reach of the campaigns, where: The reach of 
campaign A is 500,000 people. The reach of campaign BBB is 400,000 people. Maximize 
the total reach
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Coefficients for the objective function (maximize reach Z = 500x + 400y)
c = [-500, -400]  # Negatives because linprog minimizes

# Coefficients for the constraints
A = [[4000, 3000],  # Budget constraint
     [2000, 2500],  # Print media constraint
     [1000, 1500]]  # Social media constraint
b = [10_000, 4_500, 3_000]

# Solve the linear program
result = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

# Extract solution
x_opt, y_opt = result.x
z_opt = -result.fun  # Negate the minimized result to get the maximized value

# Print results
print(f"Optimal solution: x = {x_opt:.2f}, y = {y_opt:.2f}, Reach = {z_opt:.2f}")

# Plot constraints
x = np.linspace(0, 5, 400)
y1 = (10_000 - 4000 * x) / 3000
y2 = (4_500 - 2000 * x) / 2500
y3 = (3_000 - 1000 * x) / 1500

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r'$4000x + 3000y \leq 10,000$')
plt.plot(x, y2, label=r'$2000x + 2500y \leq 4,500$')
plt.plot(x, y3, label=r'$1000x + 1500y \leq 3,000$')

# Feasible region
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), color='lightgrey', label='Feasible Region', alpha=0.5)

# Optimal solution point
plt.plot(x_opt, y_opt, 'ro', label=f'Optimal Solution: ({x_opt:.2f}, {y_opt:.2f})')

# Labels and legends
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel('x (Campaign A Units)')
plt.ylabel('y (Campaign B Units)')
plt.title('Maximizing Advertising Campaign Reach')
plt.legend()
plt.grid()
plt.show()


# In[13]:


# Problem 10
"""
Meal Planning for a School Cafeteria
A school cafeteria wants to plan a meal schedule for the week, offering two types of meals, 
A and B. Each type of meal requires certain ingredients, and the cafeteria has limited 
resources. Meal A requires 2 units of meat, 3 units of vegetables, and 1 unit of rice. Meal B
requires 4 units of meat, 2 units of vegetables, and 2 units of rice. The cafeteria has a total 
of 30 units of meat, 24 units of vegetables, and 20 units of rice available for the week. The 
cafeteria earns $6 from each meal A and $5 from each meal B. Maximize the total revenue
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Coefficients for the objective function (maximize revenue Z = 6x + 5y)
c = [-6, -5]  # Negatives because linprog minimizes

# Coefficients for the constraints
A = [[2, 4],   # Meat constraint
     [3, 2],   # Vegetables constraint
     [1, 2]]   # Rice constraint
b = [30, 24, 20]

# Solve the linear program
result = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

# Extract solution
x_opt, y_opt = result.x
z_opt = -result.fun  # Negate the minimized result to get the maximized value

# Print results
print(f"Optimal solution: x = {x_opt:.2f}, y = {y_opt:.2f}, Revenue = {z_opt:.2f}")

# Plot constraints
x = np.linspace(0, 12, 400)
y1 = (30 - 2*x) / 4
y2 = (24 - 3*x) / 2
y3 = (20 - x) / 2

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r'$2x + 4y \leq 30$')
plt.plot(x, y2, label=r'$3x + 2y \leq 24$')
plt.plot(x, y3, label=r'$x + 2y \leq 20$')

# Feasible region
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), color='lightgrey', label='Feasible Region', alpha=0.5)

# Optimal solution point
plt.plot(x_opt, y_opt, 'ro', label=f'Optimal Solution: ({x_opt:.2f}, {y_opt:.2f})')

# Labels and legends
plt.xlim(0, 12)
plt.ylim(0, 10)
plt.xlabel('x (Meal A)')
plt.ylabel('y (Meal B)')
plt.title('Maximizing Cafeteria Revenue')
plt.legend()
plt.grid()
plt.show()


# In[ ]:




