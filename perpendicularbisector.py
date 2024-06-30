def calculate_perpendicular_bisector(point1, point2):
    # Calculate midpoint of the line segment AB
    midpoint = ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)
    
    # Calculate the slope of AB
    if point1[0] != point2[0]:
        slope_AB = -1 / ((point2[1] - point1[1]) / (point2[0] - point1[0]))
    else:
        slope_AB = None  # Vertical line case
    
    # Calculate y-intercept of the perpendicular bisector passing through the midpoint
    if slope_AB is not None:
        intercept = midpoint[1] - slope_AB * midpoint[0]
        return f"Perpendicular bisector equation of ({point1},{point2}): y = {slope_AB:.2f}x + {intercept:.2f}"
    else:
        return f"Perpendicular bisector equation of ({point1},{point2}): x = {midpoint[0]:.2f}"

if __name__ == "__main__":
    # Input number of points
    n = int(input("Enter number of points: "))
    
    # Input points
    points = []
    for i in range(n):
        point_str = input(f"Enter point {i + 1} (format: x,y): ")
        x, y = map(float, point_str.split(','))
        points.append((x, y))
    
    # Calculate perpendicular bisectors
    for i in range(n):
        for j in range(i + 1, n):
            point1 = points[i]
            point2 = points[j]
            bisector_equation = calculate_perpendicular_bisector(point1, point2)
            print(bisector_equation)
