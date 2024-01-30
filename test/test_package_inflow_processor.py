import pytest

from src.utils.invalid_input_error import InvalidInputError
from src.handler.package_inflow_processor import PackageInflowProcessor


@pytest.fixture
def package_processor():
    return PackageInflowProcessor


def test_valid_flow(package_processor):
    processor = package_processor()

    # empty string 
    assert [] == processor.process_input('')

    # package of zero size
    assert [None] == processor.process_input('_')

    # single package
    assert [4] == processor.process_input('bac')

    # inflow as two character encoding 'z_'
    assert [None, 26] == processor.process_input('_az_')

    # multiple packages
    assert [None, 56, None, 3] == processor.process_input('_bzzac_ac')
    assert [28, 53, 1] == processor.process_input('dz_a_aazzaaa')

    # package-size as two character encoding 'z_' 
    assert [26]== processor.process_input('z_aaaaaaaaaaaaaaaaaaaaaaaaaa')


def test_invalid_flow(package_processor):
    processor = package_processor()

    # flow contains number
    with pytest.raises(InvalidInputError) as e:
        processor.process_input('b1')
        assert "contains an invalid character" == e.message

    # flow contains whitespace
    with pytest.raises(InvalidInputError) as e:
        processor.process_input('ba ')
        assert "contains an invalid character" == e.message

    # flow contains fewer characters than specified
    with pytest.raises(InvalidInputError) as e:
        processor.process_input('abcc')
        assert "contains fewer characters than specified by package-size" == e.message


    with pytest.raises(InvalidInputError) as e:
        processor.process_input('abbazz')
        assert "contains fewer characters than specified by package-size" == e.message


    with pytest.raises(InvalidInputError) as e:
        processor.process_input('_a')
        assert "contains fewer characters than specified by package-size" == e.message

