# -*- coding: Utf-8 -*-

from __future__ import annotations

import pytest

from example_package_FrankySnow9.example import add_one


@pytest.mark.parametrize(
    ["number", "result"],
    [
        (0, 1),
        (5, 6),
        (-10, -9),
    ],
)
def test_add_one(number: int, result: int) -> None:
    assert add_one(number) == result
