from Controller.Calc import Calc
from Controller.MockImplementation import MeteoriteStats
from unittest import mock
# print(__name__) -- folder_name.file_name


def test_add_two_numbers():
    """

    :return:
    """
    result = Calc.add(4, 5)
    assert result == 9


def test_average_mass():
    """

    :return:
    """
    m = MeteoriteStats()

    #   create mock object
    m.get_data = mock.Mock()
    m.get_data.return_value = [1, 2, 3]
    data = m.get_data()
    assert m.add_mass(data) == 6

'''
    from unitest.mock import patch
    'with patch' changes the behaviour of execution
    with patch('os.path.abspath') as abspath_mock:
        test_abspath = 'some/abs/path'
        abspath_mock.return_value = test_abspath
        fi = FileInfo(original_path)
        assert fi.get_info() == (filename, original_path, test_abspath)
        
        
        ----------------- with decorator
        @patch('os.path.abspath')
        def test_get_info(abspath_mock):
            test_abspath = 'some/abs/path'
            abspath_mock.return_value = test_abspath
            filename = 'somefile.ext'
            original_path = '../{}'.format(filename)
            fi = FileInfo(original_path)
            assert fi.get_info() == (filename, original_path, test_abspath)
            
        @patch('os.path.getsize')
        @patch('os.path.abspath') -- parameter 1 for below function
        def test_get_info(abspath_mock -- for first patch nearest one, getsize_mock):
            filename = 'somefile.ext'
            original_path = '../{}'.format(filename)
            test_abspath = 'some/abs/path'
            abspath_mock.return_value = test_abspath
            test_size = 1234
            getsize_mock.return_value = test_size
'''