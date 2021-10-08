import numpy as np
import pytest

from lab2.box_window import BoxWindow, UnitBoxWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), "BoxWindow: [2.5, 2.5]"),
        (np.array([[0, 5], [0, 5]]), "BoxWindow: [0, 5] x [0, 5]"),
        (
            np.array([[0, 5], [-1.45, 3.14], [-10, 10]]),
            "BoxWindow: [0, 5] x [-1.45, 3.14] x [-10, 10]",
        ),
    ],
)
def test_box_string_representation(bounds, expected):
    assert str(BoxWindow(bounds)) == expected


@pytest.fixture
def box_2d_05():
    return BoxWindow(np.array([[0, 5], [0, 5]]))


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0]), True),
        (np.array([2.5, 2.5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
def test_indicator_function_box_2d(box_2d_05, point, expected):
    is_in = box_2d_05.indicator_function(point)
    assert is_in == expected


# ================================
# ==== WRITE YOUR TESTS BELOW ====
# ================================


<<<<<<< HEAD
def test_init():
    c = BoxWindow(np.array([[0, 5], [-1.45, 3.14], [-10, 10]]))
    assert c.bounds.shape == (3, 2)


=======
# checks if the dimension of the window box is correct (d,2).
>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [-1.45, 3.14], [-10, 10]]), (3, 2)),
        (np.array([[2.5, 2.5]]), (1, 2)),
    ],
)
<<<<<<< HEAD
def test_init2(bounds, expected):
=======
def test_init(bounds, expected):
>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
    c = BoxWindow(bounds)
    assert c.bounds.shape == expected


<<<<<<< HEAD
def test_len():
    c = BoxWindow(np.array([[0, 5], [-1.45, 3.14], [-10, 10]]))
    assert c.__len__() == [5.0, 4.59, 20.0]


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), [5, 5]),
        (np.array([[2.5, 2.5]]), [0]),
    ],
)
def test_len2(bounds, expected):
=======
# checks the evaluation of the length of each bound is correct.
@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), np.array([5, 5])),
        (np.array([[2.5, 2.5]]), np.array([0])),
        (np.array([[0, 5], [-1.45, 3.14], [-10, 10]]), np.array([5.0, 4.59, 20.0])),
    ],
)
def test_length(bounds, expected):
    c = BoxWindow(bounds)
    assert np.all(c.length() == expected)


# checks if the len of the box window is correct.
@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), 10),
        (np.array([[2.5, 2.5]]), 0),
        (np.array([[0, 5], [-1.45, 3.14], [-10, 10]]), 29.59),
    ],
)
def test_len(bounds, expected):
>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
    c = BoxWindow(bounds)
    assert c.__len__() == expected


<<<<<<< HEAD
def test_contains():
    c = BoxWindow(np.array([[0, 5], [-1.45, 3.14], [-10, 10]]))
    point1 = np.array([1, 0, 0])
    assert (c.__contains__(point1)) == True


=======
# checks if for the box_2d, the points are in the box window
>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
@pytest.fixture
def box_2d_05():
    return BoxWindow(np.array([[0, 5], [0, 5]]))


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([1, 1]), True),
        (np.array([2.5, 2.5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
<<<<<<< HEAD
def test_contains2(box_2d_05, point, expected):
=======
def test_contains(box_2d_05, point, expected):
>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
    is_in = box_2d_05.__contains__(point)
    assert is_in == expected


<<<<<<< HEAD
def test_dimension():
    c = BoxWindow(np.array([[0, 5], [-1.45, 3.14], [-10, 10]]))
    assert c.dimension() == 3


=======
# checks if the dimension of the box window is correct
>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), 2),
        (np.array([[2.5, 2.5]]), 1),
<<<<<<< HEAD
    ],
)
def test_dimension2(bounds, expected):
=======
        (np.array([[0, 5], [-1.45, 3.14], [-10, 10]]), 3),
    ],
)
def test_dimension(bounds, expected):
>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
    c = BoxWindow(bounds)
    assert c.dimension() == expected


<<<<<<< HEAD
def test_volume():
    c = BoxWindow(np.array([[0, 5], [-1.45, 3.14], [-10, 10]]))
    assert (c.volume()) == 459


=======
# checks if the evaluation of the volume of the box is correct
>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), 25),
        (np.array([[2.5, 2.5]]), 0),
<<<<<<< HEAD
    ],
)
def test_volume2(bounds, expected):
=======
        (np.array([[0, 5], [-1.45, 3.14], [-10, 10]]), 459),
    ],
)
def test_volume(bounds, expected):
>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
    c = BoxWindow(bounds)
    assert c.volume() == expected


<<<<<<< HEAD




def test_indicator_function():
    c = BoxWindow(np.array([[0, 5], [-1.45, 3.14], [-10, 10]]))
    point1 = np.array([1, 0, 0])
    assert (c.indicator_function(point1)) == 1


=======
# checks if the indicator function returns 1 if the point is in the box, 0 otherwise
>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
@pytest.fixture
def box_2d_05():
    return BoxWindow(np.array([[0, 5], [0, 5]]))


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([1, 1]), 1),
        (np.array([2.5, 2.5]), 1),
        (np.array([-1, 5]), 0),
        (np.array([10, 3]), 0),
    ],
)
<<<<<<< HEAD
def test_indicator_function2(box_2d_05, point, expected):
=======
def test_indicator_function(box_2d_05, point, expected):
>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
    is_in = box_2d_05.indicator_function(point)
    assert is_in == expected


<<<<<<< HEAD


def test_rand():
    c = BoxWindow(np.array([[0, 5], [-1.45, 3.14], [-10, 10]]))
    assert c.__contains__(c.rand(1)[0]) == True


=======
# checks if the point taken randomly is in the box
>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), True),
        (np.array([[2.5, 2.5]]), True),
<<<<<<< HEAD
    ],
)
def test_rand2(bounds, expected):
=======
        (np.array([[0, 5], [-1.45, 3.14], [-10, 10]]), True),
    ],
)
def test_rand(bounds, expected):
>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
    c = BoxWindow(bounds)
    assert c.__contains__(c.rand(1)[0]) == expected


<<<<<<< HEAD
def test_UnitBoxWindow_init():
    d=UnitBoxWindow(np.array([2,3]),2)
    assert d.__len__() == [1.0,1.0]
=======
# checks if the box window created is unitary (the length of each segment = 1)
@pytest.mark.parametrize(
    "center, dimension, expected",
    [
        (np.array([2, 3]), 2, [1.0, 1.0]),
        (np.array([1, 1, 1]), 3, [1.0, 1.0, 1.0]),
        (np.array([0]), 1, [1.0]),
    ],
)
def test_UnitBoxWindow_init(center, dimension, expected):
    d = UnitBoxWindow(center, dimension)
    assert np.all(d.length() == expected)
>>>>>>> 5fb105a7f479758cfd95109b31811c2f02d2e41b
