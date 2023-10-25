#!/usr/bin/env python3
"""
    LRU cache module
"""

from base_caching import BaseCaching
from datetime import datetime


def lru(obj):
    """ get the least recently used item """
    # get the key of the least used items
    least_used = [key for key in obj.keys()]
    # initial least used key
    lru_key = least_used[0]
    lru_updated_at = obj[least_used[0]]
    # check for the least used item using the time
    for i in range(1, 4):
        key = least_used[i]
        updated_at = obj[key]
        # if the time the prev obj is accessed is
        # greater than when the next item is accessed
        # then the next item is the lru
        if lru_updated_at > updated_at:
            lru_key = key
            lru_updated_at = updated_at
    return lru_key


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
    _lru_stack = {}

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
                    self.cache_data[key] = item
                    self._lru_stack[key] = datetime.now()
                else:
                    lru_key = lru(self._lru_stack)
                    # delete the discarded item from cache
                    # and lru stack
                    del self.cache_data[lru_key]
                    del self._lru_stack[lru_key]
                    # update the cache and lru stack with the
                    # new item
                    self.cache_data[key] = item
                    self._lru_stack[key] = datetime.now()
                    # print the discarded item
                    print('DISCARD: {}'.format(lru_key))
            else:
                self.cache_data[key] = item
                self._lru_stack[key] = datetime.now()

    def get(self, key):
        """
            get - Get an item by key
            Arguments:
                key: item key
            Return:
                value of the item
        """
        if key and key in self.cache_data:
            self._lru_stack[key] = datetime.now()
            return self.cache_data.get(key)
        return None
