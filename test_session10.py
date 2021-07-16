import math
from classPolygon import Polygon
from sequencePolygon import SequencePolygon
import pytest
import random

# print(help(Polygon))
# print(len(Polygon.__doc__))

def test_docstrings_Polygon():
    if Polygon.__doc__ == None:
        return print(f'Documentation on class description missing')
    else:
        if len(Polygon.__doc__) > 50:
            return print(f'class is described')

test_docstrings_Polygon()

def test_docstrings_SequencePolygon():
    if SequencePolygon.__doc__ == None:
        return print(f'Documentation on class description missing')
    else:
        if len(SequencePolygon.__doc__) > 50:
            return print(f'class is described')

test_docstrings_SequencePolygon()

def test_compare_instances():
    p1 = Polygon(7, 5)
    p2 = Polygon(3, 3)
    print(f'p1 is {p1}, and p2 is {p2}')
    print(f'greater_than inequality depends on vertices / num_edges alone')
    assert p1 > p2

test_compare_instances()

def test_compare_type_instances():
    p1 = Polygon(7, 5)
    p2 = tuple((1, 2, 3))
    print(f'p1 is {p1}, and p2 is {type(p2)} {p2}')
    return p1 > p2

test_compare_type_instances()

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







