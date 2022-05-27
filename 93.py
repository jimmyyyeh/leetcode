class Solution:

    @staticmethod
    def validate(s):
        if not s:
            return False
        elif s == '0':
            return True
        elif not s.startswith('0') and 0 <= int(s) <= 255:
            return True
        else:
            return False

    def dfs(self, s, result, results):
        for i in range(1, 4):
            if len(result) == 4:
                if not s:
                    ip = '.'.join(result.copy())
                    results.append(ip) if ip not in results else None
                result.pop()
                return
            if self.validate(s[:i]):
                result.append(s[:i])
                self.dfs(s=s[i:], result=result, results=results)
        if result:
            result.pop()

    def restoreIpAddresses(self, s: str) -> list[str]:
        results = list()
        self.dfs(s=s, result=list(), results=results)
        return results
