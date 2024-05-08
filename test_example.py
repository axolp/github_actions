import pytest
import utils


def test_add (a , b , expected ) :
    result = utils.add(a , b)
    assert result == expected