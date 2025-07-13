class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        #[4, 7, 9] and [2, 5, 8, 8]
        i, j = 0, 0 
        n, m = len(players), len(trainers)
        total = 0 
        while i < n and j < m : 
            if players[i] <= trainers[j] : 
                i = i + 1 
                j = j + 1 
                total +=1 
            else : 
                j = j + 1 
        return total 
        