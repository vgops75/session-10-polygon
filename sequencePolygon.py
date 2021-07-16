import math

class SequencePolygon:
  '''
  This class takes in number of vertices for the largest polygon in the sequence. Currently the sequence type is chosen as list,
  but it can be changed later, if required. The SequencePolygon class also takes in a circum_radius and it is assumed to be common
  for all of the polygons in the sequence.
  '''

  def __init__(self, num_vertices=4, circum_rad=5):
    self._num_vertices = num_vertices
    self._circum_rad = circum_rad
    # self.seq_list = [item for item in range(3, self.num_vertices + 1)]

  @property
  def get_seq_list(self):
    return [item for item in range(3, self._num_vertices + 1)]

  @property
  def get_num_edges(self):
    return self.get_seq_list

  @property
  def get_circum_rad(self):
    return self._circum_rad

  @property
  def __setitem__(self, index, value):
    self._num_vertices[index] = value
  
  @property
  def __getitem__(self, index):
    return self._num_vertices[index]

  @property
  def get_vertices(self):
    return self.get_seq_list

  @property
  def get_int_angle(self):
    int_angle = [(num_edges - 2) * 180 / num_edges for num_edges in self.get_num_edges]
    return int_angle

  @property
  def get_edge_length(self):
    edge_length = [2 * self._circum_rad * math.sin(math.pi / num_edges) for num_edges in self.get_num_edges]
    return edge_length
  
  @property
  def get_apothem(self):
    apothem = [self._circum_rad * math.cos(math.pi / num_edges) for num_edges in self.get_num_edges]
    return apothem

  @property
  def get_area(self):
    area = [(num_edges * edge_length * apothem / 2) for num_edges, edge_length, apothem in zip(self.get_num_edges, self.get_edge_length, self.get_apothem)]
    return area

  @property
  def get_perimeter(self):
    perimeter = [num_edges * edge_length for num_edges, edge_length in zip(self.get_num_edges, self.get_edge_length)]
    return perimeter

  def __len__(self):
    return len(self.get_seq_list) 

  @property
  def max_efficiency_polygon(self):
    ratio = [area / perimeter for area, perimeter in zip(self.get_area, self.get_perimeter)]
    max_index = ratio.index(max(ratio))
    # print(f'Polygon with max efficiency is Polygon(num_edges={max_index+3}, circum_rad={self._circum_rad})')
    return f'Polygon(num_edges={max_index+3}, circum_rad={self._circum_rad}) is max efficient with area to perimeter ratio of {round(max(ratio), 3)}'

  def __repr__(self):
    return f'SequencePolygon(seq_num_edges=range(3, {self._num_vertices+1}), circum_rad={self._circum_rad})'
    

