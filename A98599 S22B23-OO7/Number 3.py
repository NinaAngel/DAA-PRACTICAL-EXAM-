from collections import deque

def bfs(graph, start):#BFS (graph, start):
    visited = set()
    queue = deque([(start, [start])])


    while queue: #While the queue is not empty:
        node, path = queue.popleft() #Extract the first node and its path from the queue.

        if node not in visited: #if the node has not been visited
            visited.add(node) # Add node to the visisted set

            for neighbor in graph[node]: #For each unvisited neighbor of the current node:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor])) 
                    #Add the neighbor and its extended path to the queue

    return visited

def mutual_friends(graph, user1, user2):
    friends_user1 = bfs(graph, user1)
    friends_user2 = bfs(graph, user2)

    mutual_friends = friends_user1.intersection(friends_user2)
    return mutual_friends

#Names
social_graph = {
    'Nina': ['Dodo', 'Charles'],
    'Dodo': ['Nina', 'David'],
    'Charles': ['Nina', 'Eve'],
    'David': ['Dodo'],
    'Eve': ['Charles']
}

user1 = 'Nina'
user2 = 'Charles'

result = mutual_friends(social_graph, user1, user2)
print(f"Mutual friends between {user1} and {user2}: {result}")


