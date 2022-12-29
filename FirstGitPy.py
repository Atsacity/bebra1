import operator
import time

start_time = time.time()


class MiniCalculator:
    def __init__(self, value_1, _operator, value_2):
        self.value_1 = value_1
        self._operator = _operator
        self.value_2 = value_2
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '/': operator.truediv,
            '//': operator.floordiv,
            '*': operator.mul,
            '**': operator.pow,
            '%': operator.mod
        }

    def calculation(self):
        result = self.operations[self._operator](self.value_1, self.value_2)
        return f'{self.value_1} {self._operator} {self.value_2} = {result}'


MiniCalculator = MiniCalculator(
    value_1=int(input("Enter a first number: ")),
    _operator=input("Enter an operator: "),
    value_2=int(input("Enter a second number: "))
)

print(MiniCalculator.calculation())
print('--- %s seconds ---' % (time.time() - start_time))
