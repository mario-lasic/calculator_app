class Calculate():
    def __init__(self, statement):
        self.statement = statement

    def calculate(self):
        try:
            self.statement = self.statement.replace('^', '**')
            self.statement = self.statement.replace('X', '*')
            self.statement = self.statement.replace('%', '/100')
            result = eval(self.statement)
            return result
        except Exception as e:
            return str(e)