from texttable import Texttable
table = Texttable()

table.set_deco(Texttable.HEADER)
table.set_cols_dtype(['t',  # text
                      'f',  # float (decimal)
                      'e',  # float (exponent)
                      'i',  # integer
                      'a'])  # automatic
table.set_cols_align(["l", "r", "r", "r", "l"])
table.add_rows([["text", "float", "exp", "int", "auto"],
                ["abcd", "67", 654, 89, 128.001],
                ["efghijk", 67.5434, .654, 89.6, 12800000000000000000000.00023],
                ["lmn", 5e-78, 5e-78, 89.4, .000000000000128],
                ["opqrstu", .023, 5e+78, 92., 12800000000000000000000]])

print(table.draw())