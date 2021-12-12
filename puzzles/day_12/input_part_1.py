from typing import List

raw_input = """
fw-ll
end-dy
tx-fw
tx-tr
dy-jb
ZD-dy
dy-BL
dy-tr
dy-KX
KX-start
KX-tx
fw-ZD
tr-end
fw-jb
fw-yi
ZD-nr
start-fw
tx-ll
ll-jb
yi-jb
yi-ll
yi-start
ZD-end
ZD-jb
tx-ZD
"""


def get_input() -> List[str]:
    return raw_input.split("\n")[1:-1]
