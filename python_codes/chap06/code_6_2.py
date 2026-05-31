def p(x: int) -> bool:
    """x が条件を満たすかどうかを判定する関数。"""
    raise NotImplementedError


def binary_search(left: int, right: int) -> int:
    """p(x) が True となる最小の整数 x を返す。"""
    while right - left > 1:
        mid = left + (right - left) // 2
        if p(mid):
            right = mid
        else:
            left = mid
    return right
