#!/usr/bin/env python3
"""
    LRU cache module
"""

from base_caching import BaseCaching
from datetime import datetime


class LRUCache(BaseCaching):
    """
        LRUCache defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
        - using the lru caching policy
        Methods:
            put: add an item in the cache
            get: get and item by key from the cache
    """
    _lru_stack = []

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """
            put - Add an item in the cache
            Arguments:
                key: item key
                item: item value
            Return:
                None
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self._lru_stack:
                    # move the updated item to the front
                    self.cache_data[key] = item
                    self._lru_stack.remove(key)
                    self._lru_stack.append(key)
                else:
                    # remove the least recently used item
                    lru_key = self._lru_stack.pop(0)
                    del self.cache_data[lru_key]
                    # add the new item to the cache and lru stack
                    self.cache_data[key] = item
                    self._lru_stack.append(key)
                    # print the discarded item
                    print('DISCARD: {}'.format(lru_key))
            else:
                self.cache_data[key] = item
                self._lru_stack.append(key)

    def get(self, key):
        """
            get - Get an item by key
            Arguments:
                key: item key
            Return:
                value of the item
        """
        if key and key in self.cache_data:
            # move the accessed item to the front
            self._lru_stack.remove(key)
            self._lru_stack.append(key)
            return self.cache_data.get(key)
        return None
