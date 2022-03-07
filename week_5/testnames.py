from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name(): 
    assert make_full_name("Sally","Brown") == ("Brown; Sally")
    assert make_full_name("John", "South-Jones") == "South-Jones; John"
    assert make_full_name("Kirra", "LaRee") == "LaRee; Kirra"
    assert make_full_name("A", "Bp") == "Bp; A"
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    assert make_full_name("Sally","Brown") == ("Brown; Sally")
    assert make_full_name("John", "South-Jones") == "South-Jones; John"
    assert make_full_name("Kirra", "LaRee") == "LaRee; Kirra"
    assert make_full_name("A", "Bp") == "Bp; A"
    assert make_full_name("", "") == "; "

def test_extract_given_name():
    assert make_full_name("Sally","Brown") == ("Brown; Sally")
    assert make_full_name("John", "South-Jones") == "South-Jones; John"
    assert make_full_name("Kirra", "LaRee") == "LaRee; Kirra"
    assert make_full_name("A", "Bp") == "Bp; A"
    assert make_full_name("", "") == "; "   

pytest.main(["-v", "--tb=line", "-rN", __file__])