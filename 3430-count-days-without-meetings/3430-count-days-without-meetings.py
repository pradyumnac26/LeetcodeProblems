class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # sort - [1,3], [5,7], [9,10]
        # iterate through days from 1 -> 10 
        # so day 1 is there , day 2 is there and then day 3 is there and then .
        # so when we re checking lie this , we can say convert that 2-D arra to a 1-D array and then compare then itll be easy 
        # so say, [1,3] -> 1, 2, 3, ; [5,7] -> 5, 6, 7 ; [9, 10] - 9, 10 
        # so when we compare above with the days iteration we find that 2 are missing , so we return 2.lets try this approach out. 
        # Below is the brute force approach. 
        # x = [] 
        # meetings.sort()
        # for i in range(len(meetings)) : 
        #     start = meetings[i][0]
        #     end = meetings [i][1] 
        #     for j in range(start, end+1) : 
        #         x.append(j)
        # cnt = 0 
        # for i in range(1, days+1) : 
        #     if i not in x : 
        #         cnt +=1 
        # return cnt

        # Optimal approach 

        if not meetings:
            return days

    # Step 1: Sort meetings by start day
        meetings.sort()

    # Step 2: Merge overlapping or adjacent intervals
        merged = [meetings[0]]
        for start, end in meetings[1:]:
            last_start, last_end = merged[-1]
            if start <= last_end:
            # Overlap or touch: merge
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

    # Step 3: Count total busy days
        busy_days = sum(end - start + 1 for start, end in merged)

    # Step 4: Return available days
        return days - busy_days





