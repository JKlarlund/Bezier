import networkx as nx
import plotly.graph_objects as go

import bezier
import bezier as b
from bezier import Beziér


class Graph:
    def __init__(self, smooth_factor):
        self.g = nx.Graph()
        self.pos = nx.spring_layout(self.g)
        self.N = 0
        self.node_x = []
        self.node_y = []
        self.edge_x = []
        self.edge_y = []
        self.bezier = b.Beziér()
        self.smooth_factor = smooth_factor

    def add_node(self, x, y):
        self.g.add_node(str(self.N))
        self.pos[str(self.N)] = (x, y)
        self.node_x.append(x)
        self.node_y.append(y)
        self.N += 1
        return self.N-1

    def add_edge(self, n_1, n_2):
        self.bezier.add_curve(self.pos[n_1], self.pos[n_2])

    def get_edge_trace(self):
        self.bezier.calculate_curves(self.smooth_factor)
        edge_x = []
        edge_y = []
        for curve in self.bezier.curves:
            for edge in curve:
                # x, y points
                (x0, y0) = edge
                edge_x.append(x0)
                edge_y.append(y0)

            edge_x.append(None)
            edge_y.append(None)

        edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=2, color='#888'),
                                hoverinfo='none', mode='lines')
        return edge_trace

    def get_node_trace(self):
        node_trace = go.Scatter(x=self.node_x, y=self.node_y, mode='markers+text',
                                marker=dict(size=10, color='blue'), text=list(self.g.nodes()))
        return node_trace

    def show(self):
        edge_trace = self.get_edge_trace()
        node_trace = self.get_node_trace()

        fig = go.Figure(data=[node_trace, edge_trace])
        fig.show()
