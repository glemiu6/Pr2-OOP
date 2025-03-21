# Pr2-OOP
<h3>Cache</h3>
<p>The first program is a class Cache that helps with improving the speed for a recursiv program , where we can store the value in a dictionary </p>
<hr>


```python
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
```
<hr>
<p>Exemples to use :</p>

```python

def fib(n, cache=Cache(100)):
  if n==1 or n==2:
    return 1
  if cache.get(n):
    return cache.get(n)

  cache.put(n, fib(n-1, cache) + fib(n-2, cache))
  return cache.get(n)

assert fib(110) == 43566776258854844738105
```