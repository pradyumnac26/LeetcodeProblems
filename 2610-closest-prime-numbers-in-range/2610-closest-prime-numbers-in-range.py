class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        rangePrime = []
        primes = [True]*(right+1)
        primes[0] = False
        primes[1] = False
        for i in range(2, int(right**0.5) + 1) : 
            if primes[i] : 
                for j in range(i*i, right+1, i) : 
                    primes[j] = False
        for i in range(left, right +1 ) :
            if primes[i] == True : 
                rangePrime.append(i)
        print(rangePrime)
        
        if len(primes) < 2 : 
            return [-1, -1]
        closest_pair = [-1, -1]
        mini = float('inf')
        for i in range(len(rangePrime)-1) : 
            diff = rangePrime[i+1] - rangePrime[i] 
            if diff < mini : 
                mini = diff
                closest_pair = [rangePrime[i], rangePrime[i+1]]
        return closest_pair




        