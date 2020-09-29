from typing import List, Optional


def binary_search(search_term: int, arr: List[int]) -> Optional[int]:
    left = 0

    right = len(arr)

    while left <= right:
        medium = int((left + right) / 2)

        if arr[medium] > search_term:
            left = medium + 1

        elif arr[medium] < search_term:
            right = medium - 1

        else:
            return arr[medium]

    return None
