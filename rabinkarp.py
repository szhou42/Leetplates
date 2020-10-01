class RabinKarp:
    def __init__(self, pattern):
        self.Q = 113
        self.M = len(pattern)
        self.R = 256
        
        self.RM = 1
        for i in range(self.M-1):
            self.RM = (self.RM * self.R) % self.Q
        self.pattern_hash = self.hash(pattern, self.M)
        
    def hash(self, text, M):
        h = 0
        for j in range(M):
            h = (self.R * h + ord(text[j])) % self.Q
        return h
        
    def search(self, s):
        N = len(s)
        s_hash = self.hash(s, self.M)
        if s_hash == self.pattern_hash:
            return 0
        
        for i in range(self.M, N):
            # Here we're adding self.Q just to ensure the whole thing is positive, it doesn't change anything else because we'll do % self.Q in the end
            s_hash = (s_hash + self.Q - (ord(s[i-self.M]) * self.RM) % self.Q) % self.Q
            s_hash = (s_hash * self.R + ord(s[i])) % self.Q
            if s_hash == self.pattern_hash:
                return i - self.M + 1
        return -1
rk = RabinKarp("123")
print(rk.search("abcde123f")) # should print 5

# Here's a good video for learning rabin karp: https://www.coursera.org/lecture/algorithms-part2/rabin-karp-3KiqT
# Note: try to write a blog explaining this algorithm to solidify understanding
