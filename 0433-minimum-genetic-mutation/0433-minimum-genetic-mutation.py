class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([(startGene, 0)])
        bank_set = set(bank) 
        vis = set()


        while q : 
            gene, dist = q.popleft()
            if gene == endGene : 
                return dist 
            for i in range(len(startGene)) : 
                for ch in "ACGT" :
                    newWord = gene[:i] + ch + gene[i+1:] 
                    if newWord in bank_set and newWord not in vis : 
                        q.append((newWord, dist+1)) 
                        vis.add(newWord) 
        return -1





        