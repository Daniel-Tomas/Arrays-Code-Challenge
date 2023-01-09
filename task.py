#!/bin/python
# -*- coding: utf-8 -*-

import math
import os
import random
import re
import sys

from collections import deque, namedtuple
from collections.abc import Callable, Iterable

from functools import reduce


#  Finish function ind_sum
def ind_sum(p):
    return find_idx_two_subarrays_same_sum_op_res(p)


# O(n) space complexity and O(n) time complexity
# The logic is to, while iterating over the array, create all possible pairs of subarrays and
# check when the condition is satisfied
def find_idx_two_subarrays_same_sum_op_res(array_iter: Iterable[int]) -> int:
    error_case = -1

    array_list = list(array_iter)  # O(n) space complexity

    if len(array_list) < 3:
        return error_case

    first_accum = 0
    second_accum = sum(array_list[1:])  # O(n) time complexity
    first_subarray = deque()
    second_subarray = deque(array_list[1:])  # O(n) space complexity

    res_idx = error_case
    for idx, value in enumerate(array_list[:-1]):  # O(n) time complexity
        if first_accum == second_accum:
            res_idx = idx
            break

        first_subarray.append(value)
        first_accum += value

        second_accum -= second_subarray.popleft()

    return res_idx


# # Second, more general and complex, solution. Valid with accumulative operations
# def ind_sum(p):
#     sum_func = lambda x, y: x + y
#     sum_accum_initializer = 0
#     sum_op = namedtuple('Operation', 'func accum_initializer')(sum_func, sum_accum_initializer)
#
#     return find_idx_two_subarrays_same_op_res(p, sum_op)
#
#
# # O(n) space complexity and O(n^2) time complexity
# def find_idx_two_subarrays_same_op_res(array_iter: Iterable[int], op: tuple[Callable[[int, int], int], int]) -> int:
#     error_case = -1
#
#     array_list = list(array_iter)  # O(n) space complexity
#
#     if len(array_list) < 3:
#         return error_case
#
#     first_accum = op.accum_initializer
#     second_accum = ...  # Not needed
#     first_subarray = deque()
#     second_subarray = deque(array_list[1:])  # O(n) space complexity
#
#     res_idx = error_case
#     for idx, value in enumerate(array_list[:-1]):  # O(n) time complexity
#         if first_accum == second_accum:
#             res_idx = idx
#             break
#
#         if idx == len(array_list) - 2:
#             # Penultimate value already checked, i.e. no idx found, no need to update subarrays
#             # Otherwise reduce method with empty iterable raise exception
#             break
#
#         first_subarray.append(value)
#         first_accum = op.func(first_accum, value)
#
#         second_subarray.popleft()
#         second_accum = reduce(op.func, second_subarray)  # O(n^2) time complexity
#
#     return res_idx

if __name__ == '__main__':
    fout = open('output.txt', 'w')
    fin = open('input.txt', 'r')

    n = int(fin.readline())
    p = map(int, fin.readline().rstrip().split())

    x = ind_sum(p)

    fout.write(str(x) + '\n')
    fout.close()
    fin.close()
