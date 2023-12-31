from solution.calculate_word_distance import calculate_distance
from solution.check_anagram import is_valid_anagram
from solution.check_palindrome import is_valid_palindrome
from solution.check_pangram import check_pangram
from solution.count_good_pairs import count_good_pairs
from solution.detect_duplicates import contains_duplicates
from solution.reverse_vowels import reverse_vowels
from solution.sqrt_inaccurate import get_inaccurate_sqrt_value
from solution.two_pointers_pattern_problems import find_pair_with_target_sum
from solution.two_pointers_pattern_problems import remove_duplicates
from solution.two_pointers_pattern_problems import make_squares
from solution.two_pointers_pattern_problems import search_triplets
from solution.two_pointers_pattern_problems import dutch_flag_sort
from solution.url_shortener import shorten_url
from solution.breadh_first_traversal_pattern import TreeNode, traverse, reverse_traverse, zigzag_traverse, level_average,min_tree_depth,find_level_order_successor
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
    assert calculate_distance(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], "brown",
                              "fox") == 1


def test_count_good_pairs():
    assert count_good_pairs([1, 1, 1, 1]) == 6
    assert count_good_pairs([1, 2, 3, 1, 1, 3]) == 4
    assert count_good_pairs([1, 2, 3, 4]) == 0


def test_find_pair_with_target_sum():
    find_pair_with_target_sum([1, 2, 3, 4, 6], 6).should.equal([1, 3])
    find_pair_with_target_sum([2, 5, 9, 10, 11, 12], 11).should.equal([0, 2])


def test_remove_duplicates():
    remove_duplicates([2, 2, 2, 2, 2, 2, 2, 19]).should.equal(2)
    remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 10]).should.equal(5)


def test_make_squares():
    make_squares([-2, -1, 0, 3]).should.equal([0, 1, 4, 9])


def test_url_shortener():
    shorten_url("https://google.com").should.equal(b'BQRvJsg+jIiz3asuq2PQ0WIkrB5WRTX8dc3O7kegk40=')


def test_search_triplets():
    search_triplets([-3, 0, 1, 2, -1, 1, -2]).should.equal([[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]])
    search_triplets([-5, 2, -1, -2, 3]).should.equal([-5, 2, -1, -2, 3])


def test_dutch_flag_sort():
    dutch_flag_sort([1, 0, 2, 1, 0, 2]).should.equal([0, 0, 1, 1, 2, 2])
    dutch_flag_sort([1, 0, 0, 1, 0]).should.equal([0, 0, 0, 1, 1])


def test_bfs_level_traversal():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    traverse(root).should.equal([[12], [7, 1], [9, 10, 5]])


def test_bfs_reverse_level_traversal():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    reverse_traverse(root).should.equal([[9, 10, 5], [7, 1], [12]])


def test_bfs_zigzag_level_traversal():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    zigzag_traverse(root).should.equal([[12], [1, 7], [9, 10, 5], [17, 20]])


def test_bfs_zigzag_level_traversal():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    level_average(root).should.equal([12.0, 4.0, 6.5])


def test_min_tree_depth():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    min_tree_depth(root).should.equal(2)


def test_find_level_order_successor():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    find_level_order_successor(root, 3).should.equal(4)

