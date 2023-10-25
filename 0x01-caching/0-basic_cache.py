#!/usr/bin/python3
""" Basic Cache Module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ 
        BasicCache defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
        Methods:
            put: add an item in the cache
            get: get and item by key from the cache
    """
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
            self.cache_data[key] = item

    def get(self, key):
        """ 
            get - Get an item by key
            Arguments:
                key: item key
            Return:
                value of the item
        """
        return self.cache_data.get(key) if key else None