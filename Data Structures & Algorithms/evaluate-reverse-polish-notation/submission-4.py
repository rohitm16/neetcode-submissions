class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        res = 0
        for token in tokens:
            if token not in ["+","-","*","/"]:
                st.append(int(token))
            else:
                b = st.pop()
                a = st.pop()

                if token == "+":
                    st.append(a+b)
                if token == "-":
                    st.append(a-b)
                if token == "*":
                    st.append(a*b)
                if token == "/":
                    st.append(int(a/b))
        return st[-1]