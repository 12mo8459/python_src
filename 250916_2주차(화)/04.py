class OutOfRangeError(Exception):
    def __init__(self, strname):
        super().__init__(strname)

number = 11
if not 0 <= number <= 10:
    raise OutOfRangeError("Number is out of range")