
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        paris = { ")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in paris.values():
                st.append(c)
            elif not st or st.pop() != paris[c]:
                return False
        return not st