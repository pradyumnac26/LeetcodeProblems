class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i in ")}]":
                if not st:      # closing bracket but nothing to match
                    return False
                if i == ")" and st[-1] == "(":
                    st.pop()
                elif i == "}" and st[-1] == "{":
                    st.pop()
                elif i == "]" and st[-1] == "[":
                    st.pop()
                else:
                    return False  # mismatched pair
            else:
                st.append(i)
        return len(st) == 0
        