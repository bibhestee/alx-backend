#!/usr/bin/env python3
"""
    mru cache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
        MRUCache defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
        - using the mru caching policy
        Methods:
            put: add an item in the cache
            get: get and item by key from the cache
    """
    _mru_stack = []

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
                if key in self._mru_stack:
                    # move the updated item to the front
                    self.cache_data[key] = item
                    self._mru_stack.remove(key)
                    self._mru_stack.append(key)
                else:
                    # remove the most recently used item
                    mru_key = self._mru_stack.pop()
                    del self.cache_data[mru_key]
                    # add the new item to the cache and mru stack
                    self.cache_data[key] = item
                    self._mru_stack.append(key)
                    # print the discarded item
                    print('DISCARD: {}'.format(mru_key))
            else:
                self.cache_data[key] = item
                self._mru_stack.append(key)

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
            self._mru_stack.remove(key)
            self._mru_stack.append(key)
            return self.cache_data.get(key)
        return None
