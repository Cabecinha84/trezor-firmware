/**
 * This file is part of the TREZOR project, https://trezor.io/
 *
 * Copyright (c) SatoshiLabs
 *
 * Permission is hereby granted, free of charge, to any person obtaining
 * a copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included
 * in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
 * OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 * THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
 * OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 * ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 */

#include <math.h>
#include "slip39.h"
#include "slip39_wordlist.h"

/**
 * Calculates which buttons still can be pressed after few others were pressed.
 * Returns a 9-bit bitmask, where each bit specifies which buttons
 * still can be pressed (there still words in this combination).
 * 
 * Example: 011000011 - second, third, eighth and ninth button still can be pressed.
 */
uint16_t compute_mask(uint16_t prefix) {
  uint16_t min = prefix;
  uint16_t max = 0;
  uint8_t multiplier = 0;
  uint16_t bitmap = 0;
  uint8_t digit = 0;

  max = prefix + 1;
  while (min < 1000) {
    min = min * 10;
    max = max * 10;
    multiplier++;
  }

  // TODO: replace this with binary search or smth similar
  for (uint16_t i = 0; i < WORDS_COUNT; i++) {
    if (words_button_seq[i] < min) {
      continue;
    } else if (words_button_seq[i] > max) {
      break;
    }

    digit = (words_button_seq[i] / (uint8_t)pow(10, multiplier - 1)) % 10;
    bitmap |= 1 << digit;
  }

  return bitmap;
}
