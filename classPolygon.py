import math

# Regular Convex Polygon Object

class Polygon:
    '''
    This Polygon takes 2 parameters -- number of edges (N) and circum-radius (R), and the related parameters
    such as vertices, interior angle, edge length, apothem, area and perimeter are obtained using get methods.
    Access to modify by name operator is available only for num_edges and circum_rad, and any such 
    modifications will reflect accordingly in the dependent parameters accessed by get_{attribute} methods.
    '''
    
    def __init__(self, num_edges=3, circum_rad=6):
        self.num_edges = num_edges
        self.circum_rad = circum_rad

    @property
    def get_num_edges(self):
        return self.num_edges

    @property
    def get_circum_rad(self):
        return self.circum_rad

    @property
    def get_vertices(self):
        return self.get_num_edges

    @property
    def get_int_angle(self):
        return (self.get_num_edges - 2) * 180 / self.get_num_edges

    @property
    def get_edge_length(self):
        return 2*self.get_circum_rad * math.sin(math.pi / self.get_num_edges)

    @property
    def get_apothem(self):
        return self.get_circum_rad * math.cos(math.pi / self.get_num_edges)

    @property
    def get_area(self):
        return self.get_num_edges * self.get_edge_length * self.get_apothem / 2

    @property
    def get_perimeter(self):
        return self.get_num_edges * self.get_edge_length

    def __repr__(self):
        return f'Polygon(edges={self.get_num_edges}, rad={self.get_circum_rad})'

    def __eq__(self, other):
        if isinstance(other, Polygon):
            if self.get_vertices == other.get_vertices and self.get_circum_rad == other.get_circum_rad:
                return True
            else:
                return False
        else:
            return print(f'Compare instances of same class: Right-side instance not a Polygon')

    def __gt__(self, other):
        if isinstance(other, Polygon):
            if self.get_vertices > other.get_vertices:
                return True
            else:
                return False
        else:
            return print(f'Compare instances of same class: Right-side instance not a Polygon')
