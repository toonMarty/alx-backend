#!/usr/bin/env python3
"""
This module contains the implementation
of the index_range function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    This function calculates the index_range
    given page and page_size as inputs
    and returns a tuple as output
    Args:
        page (int): the page number
        page_size (int): the items that will be displayed in a page
    Return:
        Tuple: a tuple of size two containing a start index and
            an end index corresponding to the range of indexes to
            return in a list for those particular pagination
            parameters.
    """
    start_index = (page - 1) * page_size    # offset
    end_index = start_index + page_size
    return start_index, end_index
