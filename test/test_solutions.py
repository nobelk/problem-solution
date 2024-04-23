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
from solution.pair_with_target_sum import find_pair
from solution.array_sign import array_sign
from solution.plus_one import plus_one
from solution.DFS_graph import Node
from solution.asteroid import asteroidCollision
from solution.balance_parenthesis import is_balanced
from solution.two_number_sum import twoNumberSum
from solution.binary_search import binarySearch
from solution.run_length_encoding import get_run_length_encoding
from solution.max_length_of_pair_chain import find_longest_chain
from solution.semordnilap import find_semordnilap
from solution.generate_document import can_generate_document
from solution.binary_tree import BinaryTree
from solution.transpose_matrix import transposeMatrix
from solution.class_photos import classPhotos
from solution.product_sum_of_special_array import productSum
from solution.min_waiting_time import minimumWaitingTime
from solution.sum_of_node_depths import sum_node_depths
from solution.common_characters import commonCharacters
from solution.breadh_first_traversal_pattern import TreeNode, traverse, reverse_traverse, zigzag_traverse, \
    level_average, min_tree_depth, find_level_order_successor
import sure


def test_transpose_matrix():
    transposeMatrix([[1, 2], [3, 4]]).should.equal([[1, 3], [2, 4]])
    transposeMatrix([[1, 2], [3, 4], [5, 6]]).should.equal([[1, 3, 5], [2, 4, 6]])


def test_common_characters():
    commonCharacters(["abc", "bcd", "cbaccd"]).should.equal(["b", "c"])


def test_product_sum():
    productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]).should.equal(12)


def test_class_photos():
    classPhotos([19, 19, 21, 1, 1, 1, 1, 1], [20, 5, 4, 4, 4, 4, 4, 4]).should.equal(False)
    classPhotos([126], [125]).should.equal(True)
    classPhotos([125], [125]).should.equal(False)


def test_min_waiting_time():
    minimumWaitingTime([3, 2, 1, 2, 6]).should.equal(17)


def test_dfs_graph():
    n = Node("a")
    arr = []
    Node.depthFirstSearch(n, arr)
    arr.should.equal(["a"])


def test_sum_of_node_depths():
    t = BinaryTree(1)
    t.left = BinaryTree(2)
    t.right = BinaryTree(3)
    t.left.left = BinaryTree(4)
    t.left.right = BinaryTree(5)
    t.left.left.left = BinaryTree(8)
    t.left.left.right = BinaryTree(9)
    t.right.left = BinaryTree(6)
    t.right.right = BinaryTree(7)
    sum_node_depths(t).should.equal(16)


def test_run_length_encoding():
    get_run_length_encoding("AB").should.equal("1A1B")
    get_run_length_encoding("AAAAAAAAAAAAABBCCCC").should.equal("9A4A2B4C")


def test_can_generate_document():
    can_generate_document("n e w s o f f ice", "news office").should.equal(True)
    can_generate_document("asdf asd;fasdf ", "").should.equal(True)


def test_find_semordnilap():
    find_semordnilap(["ox", "racecar", "diaper", "box", "repaid", "racecar"]).should.equal(
        [["diaper", "repaid"], ["racecar", "racecar"]])


def test_binary_search():
    binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33).should.equal(3)


def test_twoNumberSum():
    twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10).should.equal([-1, 11])


def test_find_longest_chain():
    example1 = [[1, 2], [3, 4], [2, 3]]
    example2 = [[5, 6], [1, 2], [8, 9], [2, 3]]
    example3 = [[7, 8], [5, 6], [1, 2], [3, 5], [4, 5], [2, 3]]
    find_longest_chain(example1).should.equal(2)
    find_longest_chain(example2).should.equal(3)
    find_longest_chain(example3).should.equal(3)


def test_is_balanced():
    is_balanced("{[()]}").should.equal(True)
    is_balanced("{[}]").should.equal(False)
    is_balanced("(]").should.equal(False)


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


def test_find_pair():
    find_pair([1, 2, 3, 4, 5, 6], 6).should.equal([0, 4])
    find_pair([2, 5, 9, 11], 11).should.equal([0, 2])


def test_arraySign():
    array_sign([-1, 2, -5, 3, 4]).should.equal(1)
    array_sign([1, 2, 4, 42323, 0, -1]).should.equal(0)


def test_plus_one():
    plus_one([1, 2, 9]).should.equal([1, 3, 0])


def test_asteroid_solution():
    asteroidCollision([5, 10, -5]).should.equal([5, 10])
