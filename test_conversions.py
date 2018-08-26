"""Unit tests for the module."""

from pathlib import Path
import pytest
from chol_dictionary import *


def test_chol_conversion():
    cases = get_chol_test_cases()
    converter = CholConverter(rules='conversion_rules.txt')
    for original, converted in cases.items():
        assert converter.convert(original) == converted


def get_chol_test_cases():
    """Parse the file test_cases.txt for unit tests of converting Ch'ol into
    the new ortography.
    """
    cases_file = Path('test_cases.txt')
    cases = dict()
    reading = []
    with open(cases_file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            if len(reading) < 2 and line.strip() != '': # reading test case
                reading.append(line.strip())
            elif len(reading) == 2: # record test case
                cases[reading[0]] = reading[1]
                reading = []
    return cases


def test_full_conversion():
    case = "\\oi t'an\n"
    converter = SourceConverter(latex=False,
                              rules='conversion_rules.txt')
    result = converter._convert_line(case)
    assert result == "\\oi ty'añ"
    latex = SourceConverter(latex=True,
                          rules='conversion_rules.txt')
    result = latex._convert_line(case)
    assert result[0] == '\\'
    assert result[-1] == '}'
