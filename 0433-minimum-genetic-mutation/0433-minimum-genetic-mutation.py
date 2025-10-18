class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        s = set(bank) 
        q = deque([(startGene, 0)])
        s.discard(startGene)
        if endGene not in s : 
            return -1 

        while q : 
            gene, step = q.popleft() 
            if gene == endGene : 
                return step 
            for i in range(len(gene)): 
                tochange = gene[i]  
                for ch in "ACGT" : 
                    new_gene = gene[:i] + ch + gene[i+1:] 
                    if new_gene in s : 
                        s.remove(new_gene) 
                        q.append((new_gene, step+1)) 
        return -1

        

