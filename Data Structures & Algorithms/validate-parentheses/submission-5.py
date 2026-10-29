class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if c == "(":
                st.append(c)
            elif c == ")":
                if not st:
                    return False
                if st[-1] == "(":
                    st.pop()
                else:
                    return False
            elif c == "{":
                st.append(c)
            elif c == "}":
                if not st:
                    return False
                if st[-1] == "{":
                    st.pop()
                else:
                    return False             
            elif c == "[":
                st.append(c)
            elif c == "]":
                if not st:
                    return False
                if st[-1] == "[":
                    st.pop()
                else:
                    return False
        if not st:
            return True
        else :
            return False
            