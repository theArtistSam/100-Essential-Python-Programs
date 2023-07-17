# Python program to check if a triangle is valid

# Receive inputs for the lengths of the triangle's edges
edge1 = eval(input("Enter the value of edge 1 of the triangle"))
edge2 = eval(input("Enter the value of edge 2 of the triangle"))
edge3 = eval(input("Enter the value of edge 3 of the triangle"))

# Calculate the sum of edge1 and edge2, edge1 and edge3, and edge2 and edge3
sum1 = edge1 + edge2
sum2 = edge1 + edge3
sum3 = edge2 + edge3

# Calculate the perimeter of the triangle
perimeter = edge1 + edge2 + edge3

# Check if the sums of the two shorter edges are greater than the longest edge
# and if all sums are greater than zero to ensure a valid triangle
if sum1 > edge1 and sum1 > edge2 and sum1 > edge3 and \
   sum2 > edge1 and sum2 > edge2 and sum2 > edge3 and \
   sum3 > edge1 and sum3 > edge2 and sum3 > edge3:
    print("The triangle is valid and its perimeter is", perimeter)
else:
    print("The triangle is not valid")
