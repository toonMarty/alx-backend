#!/usr/bin/env python3
"""
This module contains a class LIFOCache
that inherits from BaseCaching. The class
contains a method that implements the FIFO
caching algorithm that discards the last item
put in the cache
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    The class definition of FIFOCache
    """
    def __init__(self):
        """
        This method is the constructor for FIFOCache
        that inherits from the Parent class
        """
        self.delete = None
        super().__init__()

    def put(self, key, item):
        """
        This method adds a key-value element
        to the cache_data dictionary
        Args
            key: the key of the item to add
            item: the value of the item
        Return:
            none
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.delete)
            print(f'DISCARD: {self.delete}')

        if key is not None:
            self.delete = key

    def get(self, key):
        """
        This method returns the value in self.cache_data
        linked to key
        Args:
            key: the key to get
        Return
            the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
