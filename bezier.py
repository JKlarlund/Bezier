class Beziér:
    def __init__(self):
        self.curves = []
        self.edges = {}

    @staticmethod
    def get_control_point(p, s, factor):
        x_1, y_1 = p
        x_2, y_2 = s

        x_m = 0.5*x_1 + 0.5*x_2
        y_m = 0.5*y_1 + 0.5*y_2

        a = -((y_2-y_1)/(x_2-x_1))
        b = y_m-a*x_m
        return factor, a * factor + b

    @staticmethod
    def calc_a(p_i, q_i, t):
        return q_i+(1-t)*(p_i-q_i)

    @staticmethod
    def calc_b(q_i, s_i, t):
        return q_i+t*(s_i-q_i)

    @staticmethod
    def calc_point(a_i, b_i, t):
        return a_i + t*(b_i-a_i)

    def a(self, p, q, t):
        p_x, p_y = p
        q_x, q_y = q

        return Beziér.calc_a(p_x, q_x, t), Beziér.calc_a(p_y, q_y, t)

    def b(self, q, s, t):
        q_x, q_y = q
        s_x, s_y = s
        return Beziér.calc_b(q_x, s_x, t), Beziér.calc_b(q_y, s_y, t)

    def point(self, p, q, s, t):
        a_x, a_y = self.a(p, q, t)
        b_x, b_y = self.b(q, s, t)
        return Beziér.calc_point(a_x, b_x, t), Beziér.calc_point(a_y, b_y, t)

    def add_curve(self, p, s):
        if (p, s) not in self.edges:
            self.edges[(p, s)] = 1
        else:
            self.edges[(p, s)] += 1

    def calculate_curves(self, smooth_factor):
        for (p, s) in self.edges:
            points = []
            n = self.edges[p, s]
            x_1 = p[0]
            x_2 = s[0]
            x_diff = x_2-x_1
            for i in range(n):
                factor = i/n*x_diff
                q = self.get_control_point(p, s, factor)
                for i in range(smooth_factor):
                    t = i / (smooth_factor - 1)
                    x, y = self.point(p, q, s, t)
                    points.append((x, y))


            self.curves.append(points)

    def get_curves(self):
        return self.curves






