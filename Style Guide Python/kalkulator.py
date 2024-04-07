# based on PEP8 this code is incorrect
# try to test using pycodestyle, pylint, flake8

# class Kalkulator:
#     """kalkulator tambah kurang"""
#     def __init__(self, _i):
#         self.i = _i
#     def tambah(self, _i): return self.i + _i
#     def kurang(self, _i):
#     return self.i - _i


# reformat this code using black, yapf, autopep8


class Kalkulator:
    """kalkulator tambah kurang"""

    def __init__(self, _i):
        self.i = _i

    def tambah(self, _i):
        return self.i + _i

    def kurang(self, _i):
        return self.i - _i
