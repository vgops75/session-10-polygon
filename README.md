# Class definitions for Regular Convex Polygons
This example project is written in Python, and tested with pytest.

### The assignment
Objective 1: Build python class for defining regular convex polygons. Class takes two parameters as input -- number of edges of a polygon (N), and the circum-radius R.

Rest of the variables are dependent on the above N and R. These are: -

    N edges (=N vertices)
    R circumradius
    interiorAngle=(N−2)⋅180/N
    edgeLength,s=2⋅R⋅sin(pi/n)
    apothem,a=R⋅cos(pi/n)
    area=12⋅n⋅s⋅a
    perimeter=n⋅s
Supplementary tasks include the below: - 
a) Implement a proper __repr__ function
b) Implement equality (==) based on vertices and circum_radius
c) Implement greater than inequality (__gt__) based on number of vertices only.

Objective 2: Build a class that takes in number of vertices for largest polygon in the sequence, and
output the maximum efficiency polygon i.e., polygon with the highest area to perimeter ratio.

Supplementary tasks include: 
a) functionality of sequence type (__getitem__)
b) support len() functionality
c) proper __repr__ representation

Results:
Implementing these two classes -- one for single instance of polygon, and another for sequence instances of polygon, as separate modules.

Then import these two into notebook and perform calls and tests showing functionalities are correctly
implemented.

Also from the SequencePolygon module, show which polygon is efficient for n = 25.

