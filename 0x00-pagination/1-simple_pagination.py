#!/usr/bin/env python3
""" Simple pagination """


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
        index_range - the function return a tuple of size two
            containing a start index and an end index
            corresponding to the range of indexes to return
            in a list for a particular pagination parameters.
        Arguments:
            page (int): page number
            page_size (int): page size
        Return:
            tuple of size two containing start and end index
    """
    start = 0 if page == 1 else (page - 1)*page_size
    end = page * page_size
    return (start, end)


class Server:
    """
        Server - Server class to paginate a database of popular baby names.
        Methods:
            dataset: return a cached dataset
            get_page: get the page passed as argument from the data set
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
            get_page - get page from cached dataset from page
                        with size of page_size
            Arguments:
                page(int): page number
                page_size(int): page size
            Return:
                page row from dataset
        """
        assert type(page) == int, 'page should be an int'
        assert type(page_size) == int, 'page size should be an int'
        assert page > 0, 'page should be greater than 0'
        assert page_size > 0, 'page size should be greater than 0'
        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end]
