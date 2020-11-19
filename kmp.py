class KMP:
  def __init__(self, pattern):
    self.pattern = pattern
    self.lps = [0 for i in range(len(pattern))]
    j = 0
    i = 1
    while i < len(pattern):
      if pattern[j] == pattern[i]:
        self.lps[i] = j + 1
        j += 1
        i += 1
      else:
        if j != 0:
            j = self.lps[j-1]
        else:
            self.lps[i] = 0
            i += 1

  def search(self, s):
    i = 0
    j = 0

    while i < len(s) and j < len(self.pattern):
      if s[i] == self.pattern[j]:
        i += 1
        j += 1
      else:
        if j != 0:
          j = self.lps[j-1]
        else:
            i += 1
    return j == len(self.pattern)
