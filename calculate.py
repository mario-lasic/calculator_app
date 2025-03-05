import math

class Calculate():
    def __init__(self, statement):
        self.statement = statement

    def calculate(self):
        try:
            self.statement = self.statement.replace('^', '**')
            self.statement = self.statement.replace('X', '*')
            self.statement = self.statement.replace('%', '/100')
            result = eval(self.statement)
            if isinstance(result, (int, float)) and (result > 1e10 or result < -1e10):
                return "{:.2e}".format(result)
            result = round(result, 3)
            return result
        except Exception as e:
            return str(e)