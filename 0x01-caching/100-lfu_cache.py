#!/usr/bin/env python3
"""
    lfu cache module
"""

from base_caching import BaseCaching


def lfu(obj):
    """ get the least frequently used item """
    # get the ranks of the items based on usage
    ranks = [obj[key] for key in obj.keys()]
    # determine the minimum rank in the list
    least_rank = min(ranks)
    # get the least frequently used items or item
    lfu_items = [key for key in obj.keys() if obj[key] == least_rank]
    # return an item or notify the amount of lfu item
    return lfu_items if len(lfu_items) == 1 else lfu_items[0]


class LFUCache(BaseCaching):
    """
        LFUCache defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
        - using the lfu caching policy
        Methods:
            put: add an item in the cache
            get: get and item by key from the cache
    """
    _lru_stack = []
    _lfu_stack = {}

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
                    # increase the number of accessed time
                    self._lfu_stack[key] += 1
                else:
                    # remove the least frequently used item
                    lfu_item = lfu(self._lfu_stack)
                    # if the lfu item is more than one use lru
                    if len(lfu_item) == 1:
                        self._lru_stack.remove(lfu_item[0])
                        discard_item = str(lfu_item[0])
                    else:
                        discard_item = lfu_item
                        self._lru_stack.remove(discard_item)
                    # remove the discarded item from the cache data
                    del self.cache_data[discard_item]
                    del self._lfu_stack[discard_item]
                    # add the new item to the cache, lru, and lru stack
                    self.cache_data[key] = item
                    self._lru_stack.append(key)
                    self._lfu_stack[key] = 1
                    # print the discarded item
                    print('DISCARD: {}'.format(discard_item))
            else:
                self.cache_data[key] = item
                self._lru_stack.append(key)
                self._lfu_stack[key] = 1

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
            self._lfu_stack[key] += 1
            return self.cache_data.get(key)
        return None
