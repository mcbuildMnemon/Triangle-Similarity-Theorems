def are_triangles_similar(side1_a, side1_b, side1_c, side2_a, side2_b, side2_c):
  """
  This function checks if two triangles are similar based on SSS, AA, or SAS criteria.

  Args:
      side1_a: Length of the first side of the first triangle.
      side1_b: Length of the second side of the first triangle.
      side1_c: Length of the third side of the first triangle.
      side2_a: Length of the first side of the second triangle.
      side2_b: Length of the second side of the second triangle.
      side2_c: Length of the third side of the second triangle.

  Returns:1    
      True if the triangles are similar, False otherwise.
  """

  # Check for SSS (Side-Side-Side) similarity
  if (side1_a / side2_a == side1_b / side2_b) and (side1_a / side2_a == side1_c / side2_c):
    return True

  # Check for AA (Angle-Angle) similarity (assuming angle measurement is available)
  # This requires modifying the function to accept angles as input

  # Check for SAS (Side-Angle-Side) similarity
  # This requires modifying the function to accept angle information 
  #  alongside side lengths

  # If none of the above conditions are met, triangles are not similar
  return False

# Example usage
triangle1_side1 = 21
triangle1_side2 = 15
triangle1_side3 = 10

triangle2_side1 = 25
triangle2_side2 = 35
triangle2_side3 = 20

if are_triangles_similar(triangle1_side1, triangle1_side2, triangle1_side3, triangle2_side1, triangle2_side2, triangle2_side3):
  print("Triangles are similar")
else:
  print("Triangles are not similar")
