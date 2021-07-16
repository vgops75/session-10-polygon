import math
from classPolygon import Polygon
from sequencePolygon import SequencePolygon
import pytest
import random

print(help(Polygon))
print(len(Polygon.__doc__))

def test_docstrings_presence(cls):
    if cls.__doc__ == None:
        return print(f'Documentation on class description missing')
    else:
        if len(cls.__doc__) > 50:
            return print(f'class is described')

test_docstrings_presence(Polygon)
test_docstrings_presence(SequencePolygon)

def test_compare_instances(cls):
    p1 = cls(7, 5)
    p2 = cls(3, 3)
    print(f'p1 is {p1}, and p2 is {p2}')
    print(f'greater_than inequality depends on vertices / num_edges alone')
    assert p1 > p2

test_compare_instances(Polygon)

def test_compare_type_instances(cls):
    p1 = cls(7, 5)
    p2 = tuple((1, 2, 3))
    print(f'p1 is {p1}, and p2 is {type(p2)} {p2}')
    return p1 > p2

test_compare_type_instances(Polygon)

def test_SequencePolygon_is_sequence():
    import collections
    p1 = SequencePolygon(25, 5)
    return print(f'{isinstance(p1.get_seq_list, collections.Sequence)}')

test_SequencePolygon_is_sequence()

def test_SequencePolygon_max_efficiency_ratio():
    p1 = SequencePolygon(25, 5)
    ratio = p1.get_area[-1] / p1.get_perimeter[-1]
    check = p1.get_apothem[-1] / 2
    return print(f'{ratio == check}')

test_SequencePolygon_max_efficiency_ratio()







