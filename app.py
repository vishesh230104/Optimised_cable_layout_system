from flask import Flask, render_template, request, jsonify
import numpy as np
from numpy import sqrt  

app = Flask(__name__)

def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points"""
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_total_cost(total_length, cost_rate):
    """Calculate the total cost based on the total length and cost rate"""
    return total_length * cost_rate

def kruskal_mst(points):
    """Implement Kruskal's algorithm to find Minimum Spanning Tree"""
    n = len(points)
    edges = []
    
    # Create all possible edges with their weights
    for i in range(n):
        for j in range(i + 1, n):
            weight = calculate_distance(points[i], points[j])
            edges.append((weight, i, j))
    
    # Sort edges by weight
    edges.sort()
    
    # Initialize disjoint set
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return False
        
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True
    
    # Kruskal's algorithm
    mst_edges = []
    total_cost = 0
    
    for weight, u, v in edges:
        if union(u, v):
            mst_edges.append((points[u], points[v]))
            total_cost += weight
    
    return mst_edges, total_cost

def kruskal_mst_with_edges(points, edges):
    """Kruskal's algorithm using provided edges"""
    n = len(points)
    edges.sort()
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return False
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True

    mst_edges = []
    total_cost = 0
    for weight, u, v in edges:
        if union(u, v):
            mst_edges.append((points[u], points[v]))
            total_cost += weight
    return mst_edges, total_cost

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    points = [(float(x), float(y)) for x, y in data['points']]
    cost_rate = float(data['cost_rate'])
    edge_costs = data.get('edge_costs')  # New: custom edge costs

    # If edge_costs provided, use them in MST
    if edge_costs:
        # edge_costs is a dict with keys like "0-1": cost
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                key = f"{i}-{j}"
                weight = float(edge_costs.get(key, calculate_distance(points[i], points[j])))
                edges.append((weight, i, j))
        mst_edges, total_length = kruskal_mst_with_edges(points, edges)
    else:
        mst_edges, total_length = kruskal_mst(points)

    total_cost = calculate_total_cost(total_length, cost_rate)

    return jsonify({
        'edges': mst_edges,
        'total_length': round(total_length, 2),
        'total_cost': round(total_cost, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)