import sure

from solution.code_template import build_string

def test_string_building():
    arr = ['s', 't', 'r', 'i', 'n', 'g']
    build_string(arr).should.equal('string')