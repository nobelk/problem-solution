from solution.calculate_word_distance import calculate_distance
from solution.check_anagram import is_valid_anagram
from solution.check_palindrome import is_valid_palindrome
from solution.check_pangram import check_pangram
from solution.count_good_pairs import count_good_pairs
from solution.detect_duplicates import contains_duplicates
from solution.reverse_vowels import reverse_vowels
from solution.sqrt_inaccurate import get_inaccurate_sqrt_value
from solution.two_pointers_pattern_problems import find_pair_with_target_sum
import sure

def test_duplicates():
    assert contains_duplicates([-1, 2, -3, 4, 5, 6, 7, 8, 9]) is False
    assert contains_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 4]) is True
    assert contains_duplicates([0, 0, 0, 0, 0, 0, 0, 0, 0]) is True


def test_check_pangram():
    assert check_pangram("abcd") is False


def test_get_inaccurate_sqrt():
    assert get_inaccurate_sqrt_value(4) == 2
    assert get_inaccurate_sqrt_value(8) == 2
    assert get_inaccurate_sqrt_value(15) == 3
    assert get_inaccurate_sqrt_value(15) == 3


def test_reverse_vowels():
    assert reverse_vowels("aei") == "iea"
    assert reverse_vowels("DesignGUrus") == "DusUgnGires"
    assert reverse_vowels("AEIOU") == "UOIEA"


def test_is_valid_palindrome():
    assert is_valid_palindrome("Was it a car or a cat I saw?") is True
    assert is_valid_palindrome("Was a car or a cat I saw?") is False
    assert is_valid_palindrome("Was aw?") is True


def test_valid_anagram():
    assert is_valid_anagram("listen", "Silent") is True
    assert is_valid_anagram("rat", "car") is False
    assert is_valid_anagram("Hello", "World") is False


def test_calculate_distance():
    assert calculate_distance(["a", "b", "c", "d", "e"], "a", "e") == 4
    assert calculate_distance(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], "brown", "fox") == 1


def test_count_good_pairs():
    assert count_good_pairs([1, 1, 1, 1]) == 6
    assert count_good_pairs([1, 2, 3, 1, 1, 3]) == 4
    assert count_good_pairs([1, 2, 3, 4]) == 0


def test_find_pair_with_target_sum():
    find_pair_with_target_sum([1, 2, 3, 4, 5], 6).should.equal([1, 3])
    find_pair_with_target_sum([2, 5, 9, 10, 11, 12], 11).should.equal([0, 2])



