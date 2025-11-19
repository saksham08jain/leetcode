# Last updated: 19/11/2025, 22:16:06
class Solution:
    def isEscapePossible(self, blocked, source, target):
        """
        Coordinate compression approach:
        - Only blocked, source, target coordinates matter
        - Compress 10^6 x 10^6 grid to ~(2*len(blocked) + 6) sized grid
        - Run BFS on compressed grid
        """
        if not blocked:
            return True
        
        # Collect all relevant coordinates
        x_coords = set([0, 10**6 - 1])  # Boundaries
        y_coords = set([0, 10**6 - 1])
        
        # Add blocked cell coordinates and their neighbors
        for x, y in blocked:
            x_coords.add(x)
            y_coords.add(y)
            # Add neighbors to ensure we can move around blocks
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= x + dx < 10**6:
                        x_coords.add(x + dx)
                    if 0 <= y + dy < 10**6:
                        y_coords.add(y + dy)
        
        # Add source and target coordinates and neighbors
        for x, y in [source, target]:
            x_coords.add(x)
            y_coords.add(y)
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= x + dx < 10**6:
                        x_coords.add(x + dx)
                    if 0 <= y + dy < 10**6:
                        y_coords.add(y + dy)
        
        # Create sorted lists and compression mappings
        x_sorted = sorted(x_coords)
        y_sorted = sorted(y_coords)
        
        x_compress = {x: i for i, x in enumerate(x_sorted)}
        y_compress = {y: i for i, y in enumerate(y_sorted)}
        
        # Compress coordinates
        blocked_compressed = {(x_compress[x], y_compress[y]) for x, y in blocked}
        source_compressed = [x_compress[source[0]], y_compress[source[1]]]
        target_compressed = [x_compress[target[0]], y_compress[target[1]]]
        
        # BFS on compressed grid
        return self.bfs(source_compressed, target_compressed, blocked_compressed, 
                       len(x_sorted), len(y_sorted))
    
    def bfs(self, source, target, blocked, max_x, max_y):
        queue = [source]
        seen = {tuple(source)}
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        while queue:
            x0, y0 = queue.pop(0)
            
            if [x0, y0] == target:
                return True
            
            for dx, dy in directions:
                x, y = x0 + dx, y0 + dy
                
                # Check bounds in compressed space
                if not (0 <= x < max_x and 0 <= y < max_y):
                    continue
                if (x, y) in seen or (x, y) in blocked:
                    continue
                
                queue.append([x, y])
                seen.add((x, y))
        
        return False