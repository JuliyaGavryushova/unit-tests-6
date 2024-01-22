from ListComparer import ListComparer
import pytest

class TestListComparer:
    def test_compare_averages_first_greater(self):
        comporator = ListComparer([1, 2, 3, 4], [1, 2, 3])
        result = comporator.compare_lists()
        assert result == "Первый список имеет большее среднее значение"

    def test_compare_averages_second_greater(self):
        comporator = ListComparer([1, 2, 3], [1, 2, 3, 4])
        result = comporator.compare_lists()
        assert result == "Второй список имеет большее среднее значение"

    def test_compare_averages_second_equal(self):
        comporator = ListComparer([1, 2, 3], [1, 2, 3])
        result = comporator.compare_lists()
        assert result == "Средние значения равны"

    def test_compare_averages_one_number(self):
        comporator = ListComparer([1], [2])
        result = comporator.compare_lists()
        assert result == "Второй список имеет большее среднее значение"

    def test_compare_averages_two_empty(self):
        comporator = ListComparer([], [])
        result = comporator.compare_lists()
        assert result == "Средние значения равны"