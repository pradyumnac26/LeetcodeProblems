class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        result = [['.' for _ in range(rows)] for _ in range(cols)]  # Initialize result matrix
        
        # Process each row of the box
        for i in range(rows):
            empty_position = cols - 1  # Track the lowest position for stones
            for j in range(cols - 1, -1, -1):
                if box[i][j] == '*':
                    # Obstacle: place it in the result and reset the empty position
                    result[j][rows - i - 1] = '*'
                    empty_position = j - 1
                elif box[i][j] == '#':
                    # Stone: move it to the lowest available position
                    result[empty_position][rows - i - 1] = '#'
                    empty_position -= 1

        return result