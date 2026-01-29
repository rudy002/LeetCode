class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        
        res = [[0]*c for _ in range(r)]
        plat = []
        for i in range(len(mat)):
            for j in mat[i]:
                plat.append(j)
        index = 0
        for i in range(len(res)):
            for j in range(len(res[i])):
                res[i][j] = plat[index]
                index+=1
        
        return res