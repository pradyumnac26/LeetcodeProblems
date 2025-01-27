class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        # Initialize a 2D array to track prerequisites
        is_prerequisite = [[False] * numCourses for _ in range(numCourses)]

        # Mark direct prerequisites
        for pre, course in prerequisites:
            is_prerequisite[pre][course] = True

        # Apply Floyd-Warshall to compute indirect prerequisites
        for k in range(numCourses):  # Intermediate course
            for i in range(numCourses):  # Start course
                for j in range(numCourses):  # End course
                    if is_prerequisite[i][k] and is_prerequisite[k][j]:
                        is_prerequisite[i][j] = True

        # Answer each query
        answer = []
        for u, v in queries:
            answer.append(is_prerequisite[u][v])

        return answer



