import deal
from typing import List
import pydash


@deal.example(lambda: __repeat_each_item([1, 3], 2) == [1, 1, 3, 3])
def __repeat_each_item(original: List[int], numtimes: int) -> List[int]:
    """Example:
    ```
    original = [1, 0]  
    numtimes = 3  
    result = [1, 1, 1, 0, 0, 0]
    ```
    """
    def repeat(item):
        return [item] * numtimes
    return pydash.flat_map(original, repeat)


def __is_binary(x: int) -> bool:
    return x in [1, 0]


@deal.pre(lambda _: all(map(__is_binary, _.data)))
def ook_modulate(data: List[int], bit_length: int) -> List[int]:
    return __repeat_each_item(data, bit_length)