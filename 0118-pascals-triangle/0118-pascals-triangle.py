class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [] ## je creer une nouvelle liste vide
        for _ in range(numRows):
            if not tri: ## ici je verifie si tri est vide. si cest le cas alors je raj. le premier element qui sera du coup 1
                tri.append([1])
                continue
            prev = tri[-1] ## je sauvegarde dans prev le dernier elemenr de tri. avec -1 cest une methode rapide davoir le dernier element d'une liste
            row = [1] ## cette variable correpond a la premiere valeur quon creer. une fois que a cette sub liste on la rentrera dans la liste principal tri

            for i in range(len(prev)-1):
                row.append(prev[i]+prev[i+1])
            
            row.append(1)
            tri.append(row)

        return tri

            
