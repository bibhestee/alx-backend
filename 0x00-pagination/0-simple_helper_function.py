#!/usr/bin/env python3
""" Simple helper function """
from typing import Tuple

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
