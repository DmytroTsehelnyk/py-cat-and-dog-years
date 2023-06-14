import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_human_age",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "human age should be 0 if cat/dog age is 0",
            "human age should be 0 if cat/dog age is 14",
            "human age should be 1 if cat/dog age is 15",
            "human age should be 1 if cat/dog age is 23",
            "human age should be 2 if cat/dog age is 24",
            "human age should be 2 if cat/dog age is 24-27",
            "human age should be [3, 2] if cat age is 28 and dog age is 24-28",
            "human age should be [21, 17] if cat/dog age is 100",
        ]
    )
    def test_proper_conversion_to_human_age(
        self,
        cat_age: int,
        dog_age: int,
        expected_human_age: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_human_age
