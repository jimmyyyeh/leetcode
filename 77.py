class Solution:
    def dfs(self, elements, k, result, results):
        for index, element in enumerate(elements):
            result.append(element)
            if len(result) == k:
                results.append(result.copy())
                result.pop()
            else:
                self.dfs(elements=elements[index + 1:], k=k, result=result, results=results)
        if result:
            result.pop()

    def combine(self, n: int, k: int) -> list[list[int]]:
        elements = list(range(1, n + 1))
        results = list()
        self.dfs(elements=elements, k=k, result=list(), results=results)
        return results
