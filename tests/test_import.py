from types import ModuleType


import dgjax  # pytype: disable=import-error


def test_import():
    assert isinstance(dgjax, ModuleType)
