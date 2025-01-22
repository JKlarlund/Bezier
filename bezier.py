class Beziér:
    def __init__(self):
        self.curves = []

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

        return self.calc_a(p_x, q_x, t), self.calc_a(p_y, q_y, t)

    def b(self, q, s, t):
        q_x, q_y = q
        s_x, s_y = s
        return self.calc_b(q_x, s_x, t), self.calc_b(q_y, s_y, t)

    def point(self, p, q, s, t):
        a_x, a_y = self.a(p, q, t)
        b_x, b_y = self.b(q, s, t)
        return self.calc_point(a_x, b_x, t), self.calc_point(a_y, b_y, t)

    def add_curve(self, p, q, s, n):

        points = []

        for i in range(n):
            t = i / (n - 1)
            x, y = self.point(p, q, s, t)
            points.append((x, y))

        self.curves.append(points)

    def get_curves(self):
        return self.curves






