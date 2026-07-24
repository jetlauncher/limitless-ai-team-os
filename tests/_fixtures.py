"""Helpers to build fake-secret strings at runtime.

Assembling these from variables (rather than string literals) keeps the
assembled token out of the compiled .pyc constants, so the repo's own
secret scanner never flags the test artifacts.
"""

_FILL = "A"
_FILL2 = "B"


def tok(prefix, n=25, ch=_FILL):
    return prefix + ch * n
