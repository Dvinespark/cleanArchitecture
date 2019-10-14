from Controller.Calc import Calc
# print(__name__) -- folder_name.file_name


def test_add_two_numbers():
    """

    :return:
    """
    result = Calc.add(4, 5)
    assert result == 9
