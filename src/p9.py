class Node:
    def __init__(self, label):
        self.label = label
        self.neighbors = []

def find_path(graph, start, end):
    def dfs(node, path, visited):
        if node.label == end:
            path.append(node.label)
            return True

        visited.add(node.label)

        for neighbor in node.neighbors:
            if neighbor.label not in visited:
                if dfs(neighbor, path, visited):
                    path.append(node.label)
                    return True

        return False

    visited = set()
    start_node = None

    for node in graph:
        if node.label == start:
            start_node = node
            break

    if start_node is None:
        return False, []

    path = []
    exists = dfs(start_node, path, visited)

    if exists:
        return True, path[::-1]  # Reverse the path to get the correct order
    else:
        return False, []

# Example usage:
if __name__ == "__main__":
    # Create the graph
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")

    A.neighbors = [B]
    B.neighbors = [A]
    C.neighbors = [B]
    D.neighbors = [B]
    E.neighbors = [F]
    F.neighbors = [B]
    G.neighbors = [F]

    graph = [A, B, C, D, E, F, G]

    # Test cases
    start_end_pairs = [("D", "B"), ("F", "A"), ("G", "C"), ("E", "D")]

    for start, end in start_end_pairs:
        exists, path = find_path(graph, start, end)
        print(f"Input: Start = {start}, End = {end}")
        print(f"Expected output: {'True' if exists else 'False'}")
        if exists:
            print(f"Path: {' --> '.join(path)}")
        print()

'''
Python is a preferred choice for solving these problems due to its clear and readable syntax, 
extensive standard library, cross-platform compatibility, strong community support, and rapid development capabilities.
'''
