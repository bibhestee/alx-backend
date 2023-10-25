#!/usr/bin/env python3
"""
    FiFo cache module
"""

from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """
        FIFOCache defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
        - using the fifo caching policy
        Methods:
            put: add an item in the cache
            get: get and item by key from the cache
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.queue = deque([key for key in self.cache_data.keys()])

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
                if key in self.queue:
                    self.cache_data[key] = item
                else:
                    first_in = self.queue.popleft()
                    del self.cache_data[first_in]
                    self.cache_data[key] = item
                    self.queue.append(key)
                    print('DISCARD: {}'.format(first_in))
            else:
                self.cache_data[key] = item
                self.queue.append(key)

    def get(self, key):
        """
            get - Get an item by key
            Arguments:
                key: item key
            Return:
                value of the item
        """
        return self.cache_data.get(key) if key else None
