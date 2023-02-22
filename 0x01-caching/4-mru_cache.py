#!/usr/bin/env python3
"""
This module contains a class MRUCache
that inherits from BaseCaching. The class
contains a method that implements the MRU
caching algorithm that discards the Most Recently
Used item put in the cache
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    The class definition of MRUCache
    """
    def __init__(self):
        """
        This method is the constructor for MRUCache
        that inherits from the Parent class
        """
        self.usage = {}
        self.freq = 0
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
            self.usage[key] = self.freq
            self.freq += 1
            self.cache_data.update({key: item})

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            delete_key = None
            newer = self.freq - 2

            for key, value in self.usage.items():
                if newer == value:
                    delete_key = key

            del self.cache_data[delete_key]
            del self.usage[delete_key]
            print(f'DISCARD: {delete_key}')

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

        self.usage[key] = self.freq
        self.freq += 1
        return self.cache_data.get(key)
