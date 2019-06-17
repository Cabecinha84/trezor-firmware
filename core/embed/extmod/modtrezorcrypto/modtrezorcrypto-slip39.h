/*
 * This file is part of the TREZOR project, https://trezor.io/
 *
 * Copyright (c) SatoshiLabs
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include "py/obj.h"
#include "py/runtime.h"

#include "slip39.h"

/// package: trezorcrypto.slip39

/// def compute_mask(prefix: str) -> int:
///     """
///     TODO: check czenglish
///     Calculates which buttons still can be pressed after some input.
///     Returns a 9-bit bitmask, where each bit specifies which buttons
///     still can be pressed.
///
///     Example: 011000011 - second, third, eighth and ninth button still can be
///     pressed.
///     """
STATIC mp_obj_t mod_trezorcrypto_slip39_compute_mask(mp_obj_t _prefix) {
  uint16_t prefix = mp_obj_get_int(_prefix);

  if (prefix < 1 || prefix > 9999) {
    mp_raise_ValueError("Invalid button prefix (range between 1 and 9999 is allowed)");
  }
  return mp_obj_new_int_from_uint(compute_mask(prefix));
}
STATIC MP_DEFINE_CONST_FUN_OBJ_1(mod_trezorcrypto_slip39_compute_mask_obj,
                                 mod_trezorcrypto_slip39_compute_mask);


STATIC const mp_rom_map_elem_t mod_trezorcrypto_slip39_globals_table[] = {
    {MP_ROM_QSTR(MP_QSTR___name__), MP_ROM_QSTR(MP_QSTR_slip39)},
    {MP_ROM_QSTR(MP_QSTR_compute_mask),
     MP_ROM_PTR(&mod_trezorcrypto_slip39_compute_mask_obj)},
};
STATIC MP_DEFINE_CONST_DICT(mod_trezorcrypto_slip39_globals,
                            mod_trezorcrypto_slip39_globals_table);

STATIC const mp_obj_module_t mod_trezorcrypto_slip39_module = {
    .base = {&mp_type_module},
    .globals = (mp_obj_dict_t *)&mod_trezorcrypto_slip39_globals,
};

