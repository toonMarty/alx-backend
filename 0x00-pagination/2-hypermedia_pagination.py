#!/usr/bin/env python3

"""This module contains a class server
and the method get_hyper_index
"""

import csv
from math import ceil
from typing import List, Dict

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
        indices = index_range(page, page_size)
        start = indices[0]
        end = indices[1]

        try:
            return self.dataset()[start: end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        This method returns a dictionary containing hypermedia pagination
        data
        Args:
            page: the current page number
            page_size: the length of returned dataset page
        Return:
             dictionary containing hypermedia pagination data
        """
        data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = ceil(total_data / page_size)

        return {'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': page + 1 if page < total_pages else None,
                'prev_page': page - 1 if page != 1 else None,
                'total_pages': total_pages
                }
