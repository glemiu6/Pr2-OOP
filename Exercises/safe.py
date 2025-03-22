class Safe:
    def __init__(self, code: list):
        self.__code = code
        self._state = True
        self._message= ""
        self._enter_code = []

    def open(self):
        return self._state

    def inserNumber(self, num):

        if self._state == True:
            return
        self._enter_code.append(num)
        if self._enter_code == self.__code[:len(self._enter_code)]:
            if len(self._enter_code) == len(self.__code):
                self._state = True
        else:
            self._enter_code = []

    def inserMesage(self, mes):
        if self._state == True:
            self._message = mes
            self.close()

    def close(self):
        self._state = False
        self._enter_code = []

    def __repr__(self):
        if self._state:
            return self._message
        else:
            return " <closed>"


#Exemple

safe = Safe([1,2,3])
safe.inserMesage('hello world')
print('message:', safe)

safe.inserNumber(1)
safe.inserNumber(2)
safe.inserNumber(3)
print('message:', safe)


safe.close()
safe.inserNumber(1)
safe.inserNumber(2)
print('message:', safe)
safe.inserNumber(3)
print('message:', safe)


safe.close()
safe.inserNumber(1)
safe.inserNumber(2)
safe.inserNumber(2)
safe.inserNumber(3)
print('message:', safe)