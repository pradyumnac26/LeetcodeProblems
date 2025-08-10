class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # 32 = 23 -> so yes they are the power of 2.
        # 128 , 182, 281, 218, 812, 821 -> all are power of 2 , have to return true if possible or false
        # so given an n -> fid all permutations or numbers or digits that can be formed thriugh those nubers and check if they are th epower of 2
        # or smart way is find all powers of 2 store it somewhere and see if the n can be done that wa y
        patterns = set()
        for i in range(32): 
            power = 1 << i
            patterns.add("".join(sorted(str(power))))
        return "".join(sorted(str(n))) in patterns
        

        