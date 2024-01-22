from typing import List


class ListComparer:
    def __init__(self, list1: List[int], list2: List[int]):
        self.list1 = list1
        self.list2 = list2

    @staticmethod
    def find_average(lst: List[int]) -> float:
        if not lst:
            return 0
        return sum(lst) / len(lst)

    def compare_lists(self) -> str:
        average1 = self.find_average(self.list1)
        average2 = self.find_average(self.list2)

        if average1 > average2:
            return "Первый список имеет большее среднее значение"
        elif average2 > average1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
