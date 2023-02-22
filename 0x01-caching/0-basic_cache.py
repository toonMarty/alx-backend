#!/usr/bin/env python3
"""
This module contains a class BasicCache that
inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    The class definition of BasicCache
    """
    def put(self, key, item):
        """
        This method adds a key-value element
        to the cache_data dictionary
        Args:
            key: the key of the item to add
            item: the value of the item
        Return:
            none
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        This method returns the value in self.cache_data
        linked to key
        Args:
            key: the key to get
        Return:
            the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
