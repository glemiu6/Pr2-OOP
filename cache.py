class Cache:
    def __init__(self, size):
        self._size = size
        self.d = {}
        self._chaves = []

    def put(self, k, v):
        if k not in self.d:
            if len(self.d) >= self._size:
                first_key = self._chaves.pop(0)
                del self.d[first_key]

            self.d[k] = v
            self._chaves.append(k)

        else:
            self.d[k] = v

    def get(self, chave):
        if chave not in self.d.keys():
            return None
        return self.d[chave]



def fib(n, cache=Cache(100)):
  if n==1 or n==2:
    return 1
  if cache.get(n):
    return cache.get(n)

  cache.put(n, fib(n-1, cache) + fib(n-2, cache))
  return cache.get(n)

print(fib(110))