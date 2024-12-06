import sys
sys.path.append('../geometric_lib')
import pytest
import math
import calculate as c
#Test triangle
@pytest.mark.parametrize('size, expected, correct',[
                         ([3,4,5],12,True),
                         ([3,5,5],13,True),
                         ([-3,5,7],None,True),
                         (["asda", "asdad", "asdad"],None, True)
                         ])
def test_perimetr_triangle(size, expected, correct):
    if(correct):
        assert expected == c.calc('triangle', 'perimeter', size)
    else:
        assert expected != c.calc('triangle', 'perimeter', size)


@pytest.mark.parametrize('size, expected, correct',[
                         ([6,8,10],24,True),
                         ([5,12,13],30,True),
                         ([3,-5,7],None,True),
                         (["asda", "asdad", "asdad"],None, True)
                         ])
def test_area_triangle(size, expected, correct):
    if(correct):
        assert expected == c.calc('triangle', 'area', size)
    else:
        assert expected != c.calc('triangle', 'area', size)
#Test square
@pytest.mark.parametrize('size, expected, correct',[
                         ([6],24,True),
                         ([8],32,True),
                         ([-3],None,True),
                         (["str"],None, True)
                         ])
def test_perimetr_square(size, expected, correct):
    if(correct):
        assert expected == c.calc('square', 'perimeter', size)
    else:
        assert expected != c.calc('square', 'perimeter', size)


@pytest.mark.parametrize('size, expected, correct',[
                         ([8],64,True),
                         ([13],169,True),
                         ([-3,],None,True),
                         (["asda"],None, True)
                         ])
def test_area_square(size, expected, correct):
    if(correct):
        assert expected == c.calc('square', 'area', size)
    else:
        assert expected != c.calc('square', 'area', size)

#Test rectangle
@pytest.mark.parametrize('size, expected, correct',[
                         ([3,4],14,True),
                         ([3,5],16,True),
                         ([-3,5],None,True),
                         (["asda", "asdad"],None, True)
                         ])
def test_perimetr_rectangle(size, expected, correct):
    if(correct):
        assert expected == c.calc('rectangle', 'perimeter', size)
    else:
        assert expected != c.calc('rectangle', 'perimeter', size)


@pytest.mark.parametrize('size, expected, correct',[
                         ([6,5],30,True),
                         ([50,12],600,True),
                         ([3,-5],None,True),
                         ([-3,-5],None,True),
                         (["asda", "asdad"],None, True)
                         ])
def test_area_rectangle(size, expected, correct):
    if(correct):
        assert expected == c.calc('rectangle', 'area', size)
    else:
        assert expected != c.calc('rectangle', 'area', size)


#Test circle
@pytest.mark.parametrize('size, expected, correct',[
                         ([2],4*math.pi,True),
                         ([10],20*math.pi,True),
                         ([-9],None,True),
                         (["str"],None, True)
                         ])
def test_perimetr_circle(size, expected, correct):
    if(correct):
        assert expected == c.calc('circle', 'perimeter', size)
    else:
        assert expected != c.calc('circle', 'perimeter', size)


@pytest.mark.parametrize('size, expected, correct',[
                         ([6],36*math.pi,True),
                         ([8],64*math.pi,True),
                         ([-9],None,True),
                         (["str"],None, True)
                         ])
def test_area_circle(size, expected, correct):
    if(correct):
        assert expected == c.calc('circle', 'area', size)
    else:
        assert expected != c.calc('circle', 'area', size)


