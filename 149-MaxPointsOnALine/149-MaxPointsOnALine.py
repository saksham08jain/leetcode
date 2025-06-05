# Last updated: 5/6/2025, 11:09:10 pm
from fractions import Fraction

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        slopes = {}
        n = len(points)
        count = 0
        Xs = {}
        Ys = {}

        for i in range(n):
            if points[i][1] in Ys:
                Ys[points[i][1]] += 1
            else:
                Ys[points[i][1]] = 1

            if points[i][0] in Xs:
                Xs[points[i][0]] += 1
            else:
                Xs[points[i][0]] = 1
                continue

        for i in range(n):
            for j in range(i + 1, n):
                dely = points[i][1] - points[j][1]
                delx = points[i][0] - points[j][0]

                if dely == 0:
                    continue

                if delx == 0:
                    continue

                slope = Fraction(dely, delx)
                c = points[i][1] - points[i][0] * slope

                if (slope, c) in slopes:
                    slopes[(slope, c)] += 1
                else:
                    slopes[(slope, c)] = 1

        print(slopes, Xs, Ys)
        Ys[10**4 + 1] = -1
        Xs[10**4 + 1] = -1
        slopes[(0, 0)] = 0

        ans1 = ((8 * max(slopes.values()) + 1) ** 0.5 + 1)
        ans1 = int(ans1 / 2)

        return max(ans1, max(Ys.values()), max(Xs.values()))