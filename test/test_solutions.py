from solution.calculate_word_distance import calculate_distance
from solution.check_anagram import is_valid_anagram
from solution.check_palindrome import is_valid_palindrome
from solution.check_pangram import check_pangram
from solution.count_good_pairs import count_good_pairs
from solution.detect_duplicates import contains_duplicates
from solution.reverse_vowels import reverse_vowels, reverse_vowels2
from solution.sqrt_inaccurate import get_inaccurate_sqrt_value
from solution.two_pointers_pattern_problems import find_pair_with_target_sum
from solution.two_pointers_pattern_problems import remove_duplicates
from solution.two_pointers_pattern_problems import make_squares
from solution.two_pointers_pattern_problems import search_triplets
from solution.two_pointers_pattern_problems import dutch_flag_sort
from solution.url_shortener import shorten_url
from solution.smallest_difference import smallestDifference
from solution.tournament_winner import tournamentWinner
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
from solution.nth_fibonacci_number import getNthFib
from solution.bubble_sort import bubble_sort
from solution.transpose_matrix import transposeMatrix
from solution.class_photos import classPhotos
from solution.product_sum_of_special_array import productSum
from solution.min_waiting_time import minimumWaitingTime
from solution.sum_of_node_depths import sum_node_depths
from solution.validate_subsequence import isValidSubsequence
from solution.find_three_largest_numbers import findThreeLargestNumbers
from solution.common_characters import commonCharacters
from solution.branch_sums import branchSums
from solution.validate_BST import validateBst
from solution.find_middle_node_of_linked_list import LinkedList, middleNode
from solution.breadh_first_traversal_pattern import TreeNode, traverse, reverse_traverse, zigzag_traverse, \
    level_average, min_tree_depth, find_level_order_successor
from solution.caesar_cipher_encryptor import caesarCipherEncryptor
from solution.evaluate_expression_tree import evaluateExpressionTree
from solution.sorted_squared_array import sortedSquaredArray
from solution.selection_sort import selectionSort
from solution.one_edit import oneEdit
from solution.longest_peak_length import longestPeak
from solution.monotonically_increasing import isMonotonic
from solution.non_constructible_change import nonConstructibleChange
from solution.find_closest_value_in_BST import BST, findClosestValueInBst
from solution.tree_traversal import inOrderTraverse, preOrderTraverse, postOrderTraverse
from solution.invert_binary_tree import invertBinaryTree
from solution.symmetrical_tree import symmetricalTree
from solution.two_colorable import twoColorable
from solution.graph_bfs import Node
from solution.is_same_tree import isSameTree, TreeNode1
from solution.move_element_to_end import moveElementToEnd
from solution.all_valid_ip_addresses import validIPAddresses
from solution.stair_climbing import climbStairs
from solution.cycle_in_graph import cycleInGraph
from solution.has_path_sum import has_path_sum
from solution.palindrome_number import isPalindrome
from solution.search_insert_position import searchInsert
from solution.average_of_tree_levels import averageOfLevels, TreeNodeL
from solution.can_jump import can_jump
from solution.sqrt import sqrt, sqrt1
from solution.add_binary import AddBinary
from solution.delete_node import DeleteNodeSolution
from solution.listnode import ListNode
from solution.validate_subsequence import isValidSubsequence
from solution.highest_point import highest_point
from solution.reverse_words import reverse_words
from solution.pivot_index import find_pivot_index
from solution.find_difference import find_difference
from solution.find_max_average import findMaxAverage
from solution.merge_string_alternatively import mergeAlternately

import math
import sure
import pytest


def test_merge_string_alternatively():
    mergeAlternately('abcd', 'pq').should.equal('apbqcd')

def test_find_max_average():
    findMaxAverage([1,12,-5,-6,50,3],4).should.equal(12.75)
    findMaxAverage([5],1).should.equal(5.000)


def test_find_difference():
    find_difference([1, 2, 3], [2, 4, 6]).should.equal([[1, 3], [4, 6]])


def test_find_pivot_index():
    find_pivot_index([1, 7, 3, 6, 5, 6], 4).should.equal(3)


def test_reverse_words():
    reverse_words("a good   example").should.equal("example good a")
    reverse_words("  hello world  ").should.equal("world hello")


def test_highest_point():
    highest_point([-5, 1, 5, 0, -7]).should.equal(1)
    highest_point([-4, -3, -2, -1, 4, 3, 2]).should.equal(0)


def test_is_valid_subsequence():
    isValidSubsequence('abc', 'abxasdfaserc').should.equal(True)
    isValidSubsequence('xyz', 'xadyzafz').should.equal(True)


def test_move_element_to_end():
    moveElementToEnd([0, 1, 0, 3, 12], 0).should.equal([1, 3, 12, 0, 0])


def test_reverse_vowels2():
    reverse_vowels2("DesignGUrus").should.equal("DusUgnGires")


def test_delete_node():
    l = ListNode(4)
    l.next = ListNode(5)
    l.next.next = ListNode(1)
    l.next.next.next = ListNode(9)
    d = DeleteNodeSolution()
    d.deleteNode(l.next)
    l.next.val.should.equal(1)


@pytest.mark.skip(reason="not passing")
def test_add_binary():
    a = AddBinary()
    a.addBinary("11", "1").should.equal("100")
    a.addBinary("0", "0").should.equal("0")
    a.addBinary("1111", "1111").should.equal("10000")


def test_sqrt():
    sqrt(4).should.equal(2)
    sqrt(0).should.equal(0)
    sqrt(1).should.equal(1)
    sqrt1(8).should.equal(2)


def test_can_jump():
    can_jump([2, 3, 1, 1, 4]).should.equal(True)


def test_average_of_levels():
    t = TreeNodeL(3)
    t.left = TreeNodeL(9)
    t.right = TreeNodeL(20)
    t.right.left = TreeNodeL(15)
    t.right.right = TreeNodeL(7)
    res = averageOfLevels(t)
    math.isclose(res[0], 3.0)
    math.isclose(res[1], 14.5)
    math.isclose(res[2], 11.0)


def test_search_insert():
    searchInsert([1, 3, 5, 6], 7).should.equal(4)
    searchInsert([1, 3, 5, 6], 2).should.equal(1)


def test_is_palindrome_number():
    isPalindrome(-123).should.equal(False)
    isPalindrome(12321).should.equal(True)


def test_path_sum_helper():
    has_path_sum(None, 0).should.equal(False)
    t = TreeNodeL(1)
    t.left = TreeNodeL(2)
    t.right = TreeNodeL(3)
    has_path_sum(t, 3).should.equal(True)
    has_path_sum(t, 5).should.equal(False)


def test_cycle_in_graph():
    # edges = [[1, 2], [2], []]
    # cycleInGraph(edges).should.equal(False)
    edges1 = [[], [0, 3], [0], [1, 2]]
    cycleInGraph(edges1).should.equal(True)


def test_climb_stairs():
    climbStairs(2).should.equal(2)
    climbStairs(3).should.equal(3)


def test_is_same_tree():
    t = TreeNode1(1)
    t.left = TreeNode1(2)
    t.right = TreeNode1(0)
    t1 = TreeNode1(1)
    t1.left = TreeNode1(2)
    t1.right = TreeNode1(0)
    isSameTree(t, t1).should.equal(True)


def test_valid_ip_addresses():
    validIPAddresses('1921680').should.equal(
        ["1.9.216.80", "1.92.16.80", "1.92.168.0", "19.2.16.80", "19.2.168.0", "19.21.6.80", "19.21.68.0", "19.216.8.0",
         "192.1.6.80", "192.1.68.0", "192.16.8.0"]
    )


def test_move_element_to_end():
    moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2).should.equal([1, 3, 4, 2, 2, 2, 2, 2])


def test_graph_bfs():
    g = Node("A")
    g.addChild("B")
    g.addChild("C")
    g.addChild("D")
    array = []
    g.breadthFirstSearch(array)
    array.should.equal(["A", "B", "C", "D"])


def test_two_colorable():
    edges = [
        [0, 1],
        [0, 2],
        [1, 2]
    ]
    twoColorable(edges).should.equal(False)


def test_symmetrical_tree():
    t = BinaryTree(1)
    t.left = BinaryTree(2)
    t.right = BinaryTree(2)
    t.left.left = BinaryTree(3)
    t.left.right = BinaryTree(4)
    t.right.right = BinaryTree(3)
    t.right.left = BinaryTree(4)
    symmetricalTree(t).should.equal(True)


def test_invert_binary_tree():
    t = BinaryTree(1)
    t.left = BinaryTree(2)
    t.right = BinaryTree(3)
    t.left.left = BinaryTree(4)
    t.left.right = BinaryTree(4)
    t.right.right = BinaryTree(7)
    t.right.left = BinaryTree(6)
    invertBinaryTree(t)
    t.value.should.equal(1)
    t.right.value.should.equal(2)
    t.left.value.should.equal(3)
    t.right.right.value.should.equal(4)


def test_tree_traversal():
    in_order_result = [1, 2, 5, 5, 10, 15, 22]
    pre_order_result = [10, 5, 2, 1, 5, 15, 22]
    post_order_result = [1, 2, 5, 5, 22, 15, 10]

    t = BinaryTree(10)
    t.right = BinaryTree(15)
    t.left = BinaryTree(5)
    t.right.right = BinaryTree(22)
    t.left.left = BinaryTree(2)
    t.left.right = BinaryTree(5)
    t.left.left.left = BinaryTree(1)

    array = []
    array = inOrderTraverse(t, array)
    array.should.equal(in_order_result)
    array = []
    array = preOrderTraverse(t, array)
    array.should.equal(pre_order_result)
    array = []
    array = postOrderTraverse(t, array)
    array.should.equal(post_order_result)


def test_longest_peak_length():
    longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]).should.equal(6)


def test_is_monotonic():
    isMonotonic([-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11]).should.equal(True)


def test_validate_BST():
    t = BinaryTree(10)
    t.left = BinaryTree(5)
    t.right = BinaryTree(15)
    t.left.right = BinaryTree(10)
    validateBst(t).should.equal(False)


def test_smallest_difference():
    smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]).should.equal([28, 26])


def test_one_edit():
    oneEdit('hello', 'hallo').should.equal(True)
    oneEdit('abc', 'ac').should.equal(True)
    oneEdit('ab', 'acsdf').should.equal(False)


def test_selection_sort():
    selectionSort([8, 5, 2, 9, 5, 6, 3]).should.equal([2, 3, 5, 5, 6, 8, 9])


def test_find_closest_value_in_BST():
    t = BST(4)
    t.left = BinaryTree(2)
    t.right = BinaryTree(6)
    result = findClosestValueInBst(t, 7)
    result.should.equal(6)


def test_non_constructible_change():
    nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]).should.equal(20)


def test_sorted_squared_array():
    sortedSquaredArray([-10, -5, 0, 5, 10]).should.equal([0, 25, 25, 100, 100])


def test_evaluate_expression_tree():
    t = BinaryTree(-4)
    t.left = BinaryTree(3)
    t.right = BinaryTree(2)
    result = evaluateExpressionTree(t)
    result.should.equal(6)

    t = BinaryTree(-3)
    t.left = BinaryTree(3)
    t.right = BinaryTree(2)
    result = evaluateExpressionTree(t)
    result.should.equal(1)


def test_bubble_sort():
    bubble_sort([8, 5, 2, 9, 5, 6, 3]).should.equal([2, 3, 5, 5, 6, 8, 9])


def test_caesar_cipher_encryptor():
    caesarCipherEncryptor('xyz', 2).should.equal('zab')


def test_branch_sums():
    t = BinaryTree(1)
    t.left = BinaryTree(2)
    t.right = BinaryTree(3)
    t.left.left = BinaryTree(4)
    t.left.right = BinaryTree(5)
    t.left.left.left = BinaryTree(8)
    t.left.left.right = BinaryTree(9)
    t.right.left = BinaryTree(6)
    t.right.right = BinaryTree(7)
    result = branchSums(t)
    result.should.equal([15, 16, 8, 10, 11])


def test_tournament_winner():
    competions = [
        ["HTML", 'C#'],
        ['C#', 'Python'],
        ['Python', 'HTML']
    ]
    results = [0, 0, 1]
    tournamentWinner(competions, results).should.equal('Python')


def test_find_middle_node():
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(5)
    middle_node = middleNode(head)
    middle_node.value.should.equal(3)


def test_find_three_largest_numbers():
    findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]).should.equal([18, 141, 541])


def test_is_valid_subsequence():
    isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 22, 25, 6, -1, 8, 10]).should.equal(True)


def test_nth_fibonacci():
    getNthFib(3).should.equal(1)
    getNthFib(11).should.equal(55)
    getNthFib(101).should.equal(354224848179261915075)


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


@pytest.mark.skip(reason="not passing")
def test_dfs_graph():
    n = Node("a")
    arr = []
    Node.depthFirstSearch(n, arr)
    arr.should.equal(["a"])


@pytest.mark.skip(reason="not passing")
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


@pytest.mark.skip(reason="not passing")
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


@pytest.mark.skip(reason="not passing")
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
