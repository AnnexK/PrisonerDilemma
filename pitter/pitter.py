import numpy as np


class PaymentMatrixError(Exception):
    pass


class PaymentMatrix:
    def __init__(self, cc, cd, dc, dd):
        if not all(a >= 0.0 for a in (cc, cd, dc, dd)):
            raise PaymentMatrixError('Matrix has negative entries')
        if not dc < cc < dd < cd:
            raise PaymentMatrixError('Matrix elements are not ordered')
        
        self.M = np.zeros((2,2,2))
        self.M[0,0] = np.array([dd, dd])
        self.M[0,1] = np.array([dc, cd])
        self.M[1,0] = np.array([cd, dc])
        self.M[1,1] = np.array([cc, cc])

    def __getitem__(self, decision):
        return self.M[tuple(int(d) for d in decision)]


class BasicPitter:
    '''Базовый класс для организации различных видов турниров между программами-заключёнными.
Предоставляет реализацию методов разыгрывания многоигровой партии дилеммы между двумя программами
и разыгрывания турнира в самом простом варианте (одна партия между двумя программами).'''
    def __init__(self, paymtx: PaymentMatrix, n: int):
        self.paymtx = paymtx
        self.n = n

    def pit(self, A, B):
        losses = np.zeros(2)

        for i in range(self.n):
            da, db = A.make_decision(), B.make_decision()
            payment = self.paymtx[da, db]
            losses += payment
            self.tell(A, db)
            self.tell(B, da)

        return losses

    def tell(self, pris, oppt):
        pris.get(oppt)

    def commence(self, P):
        return self.pit(*P)

    def tournament(self, P):
        points = self.commence(P)
        S = points.argsort()
        return P[S], points[S]
