from typing import *


# extmod/modtrezorcrypto/modtrezorcrypto-slip39.h
def compute_mask(prefix: str) -> int:
    """
    TODO: check czenglish
    Calculates which buttons still can be pressed after some input.
    Returns a 9-bit bitmask, where each bit specifies which buttons
    still can be pressed.
    Example: 011000011 - second, third, eighth and ninth button still can be
    pressed.
    """
