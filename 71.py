class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.rstrip('/')
        path_list = path.split('/')

        result_path = list()
        for path_ in path_list:
            if not path_ or path_ == '.':
                continue
            if path_ == '..':
                result_path = result_path[:-1]
            else:
                result_path.append(path_)
        return '/' + '/'.join(result_path)
