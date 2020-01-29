# file __init__.py : adalah file untuk inisialisasi module
# file __init__.py : harus selalu ada didalam peckage

# 1)
# from .matematika import *
# from .fisika import *

# 2)
from .matematika import tambah, kurang
from .fisika import kecepatan, waktu_tempuh

# NB : tanda (.)/dot : sebagai absolute direktori
#     matematika dan fisika adalah nama file module
#     tambah, kurang, adalah method
