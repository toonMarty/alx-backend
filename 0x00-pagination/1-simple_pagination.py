#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This method takes a page number and page_size
        as inputs, asserts their types and domain of discourse
        where the domain of discourse is a positive number
        greater than 0 and uses index_range to find correct indexes
        to paginate the dataset correctly
        Args:
            page: the page number
            page_size: items that will be displayed in a page
        Return:
            list: an appropriate page of a dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # indexes is a tuple with start and end indexes
        indexes = index_range(page, page_size)
        start = indexes[0]
        end = indexes[1]

        return self.dataset()[start: end]
