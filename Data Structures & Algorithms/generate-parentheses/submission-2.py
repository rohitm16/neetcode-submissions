
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = ""

        def backtrack(open_count, close_count,s):
            if len(s) == 2 * n:
                res.append("".join(s))
                # s = ''
                return

            if open_count < n:
                s = s + "("
                backtrack(open_count+1,close_count,s)
                s = s[:-1]

            if close_count < open_count:
                s = s+ ")"
                backtrack(open_count, close_count+1,s)
                s = s[:-1]


        backtrack(0,0,s)
        return res
