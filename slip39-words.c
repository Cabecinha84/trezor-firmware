#include "slip39-words.h"
#include <math.h>
#include <stdio.h>

int main() {
  uint16_t input = 32;
  uint16_t result = compute_mask(input);
}

// Calculates which buttons still can be pressed after
// few others were pressed.
// Returns a 9-bit bitmask, where each bit specifies which buttons
// still can be pressed (there still words in this combination).
// Example: 011000011 - second, third, eighth and ninth button still can be
// pressed.
uint16_t compute_mask(uint16_t prefix) {

  if (prefix == 0 || prefix > 9999) {
    printf("nope");
    // err
  }
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

  printf("min: %d\n", min);
  printf("max: %d\n", max);

  // TODO: replace this with binary search or similar magick
  for (uint16_t i = 0; i < WORDS_COUNT; i++) {
    if (words_button_seq[i] < min) {
      continue;
    } else if (words_button_seq[i] > max) {
      break;
    }

    digit = (words_button_seq[i] / (uint8_t) pow(10, multiplier - 1)) % 10;
    bitmap |= 1 << digit;
    printf("digit: %d\n", digit);
    printf("x: %d\n", words_button_seq[i]);
  }
  printf("bitmap: ");
  while (bitmap) {
    if (bitmap & 1)
      printf("1");
    else
      printf("0");

    bitmap >>= 1;
  }
  printf("\n");
  return bitmap;
}
