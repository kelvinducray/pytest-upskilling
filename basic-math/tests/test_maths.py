import pytest
from basic_math.maths import add, divide, multiply, subtract


@pytest.mark.parametrize(
    "input,expected",
    [
        ((5, 5), 10),
        ((6, 0), 6),
        ((-8, 4), -4),
        ((0.1, 0.4), 0.5),
    ],
)
def test_add(input, expected):
    assert add(*input) == expected


@pytest.mark.parametrize(
    "input",
    [
        ([5, 6, 7], [8, 9]),  # lists
        ("6", "0"),  # strings
        (-8, (3, 4, 5)),  # mixture
        (True, True),  # bools
    ],
)
def test_add_different_types(input):
    with pytest.raises(ValueError):
        add(*input)


# @pytest.mark.parametrize(
#     "input,expected",
#     [
#         ((5, 5), 0),
#         ((6, 0), 6),
#         ((-8, 4), -12),
#         ((0.4, 0.1), 0.3),
#     ],
# )
# def test_subtract(input, expected):
#     assert subtract(*input) == expected


# @pytest.mark.parametrize(
#     "input,expected",
#     [
#         ((5, 5), 0),
#         ((6, 0), 6),
#         ((-8, 4), -12),
#         ((0.4, 0.1), 0.3),
#     ],
# )
# def test_multiply(input, expected):
#     assert multiply(*input) == expected


# @pytest.mark.parametrize(
#     "input,expected",
#     [
#         ((5, 5), 0),
#         ((6, 1), 6),
#         ((-8, 4), -12),
#         ((0.4, 0.1), 0.3),
#     ],
# )
# def test_divide(input, expected):
#     assert divide(*input) == expected


# @pytest.mark.parametrize(
#     "input",
#     [1, 2.3, 0, -5, -6.3],
# )
# def test_divide_by_zero(input):
#     with pytest.raises(ZeroDivisionError):
#         divide(input, 0)
