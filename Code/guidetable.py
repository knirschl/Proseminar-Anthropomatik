import numpy as np

class GuideTable:
    def __init__(self, N, f_inv) -> None:
        self.T = []
        self.PS = np.array([])
        self.N = N
        self.f_inv = f_inv
        for i in range(0, self.N):
            self.T.append(self.f_inv(i / self.N))
        self.T = np.array(self.T)
    
    def setup_partial_sums(self, partial_sums) -> None:
        self.PS = np.array(partial_sums)
    
    def setup_partial_sums_uniform(self, f, max) -> None:
        ps = []
        i = 0.0
        step = max / self.N
        while (i < max):
            if (i == 0.0):
                ps.append(f(0))
            else:
                ps.append(ps[-1] + f(i))
            i += step
        self.PS = np.array(ps)
    
    def hash(self, U) -> int:
        return (self.N * U).astype(np.int64)
    
    def search_single(self, U) -> np.double:
        Z = self.hash(U)
        while (self.PS[Z] <= U):
            Z += 1
        
        return self.T[Z]

    def search(self, U) -> np.ndarray:
        points = []
        for u_vec in U:
            vpoints = []
            for u_ in u_vec:
                vpoints.append(self.search_single(u_))
            points.append(vpoints)
        return np.array(points)
    
    def test(self, U) -> np.double:
        return self.hash(U)
        
