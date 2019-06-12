# isort:skip_file

# unlock the device
import boot  # noqa: F401

# prepare the USB interfaces, but do not connect to the host yet
import usb

from trezor import loop, wire, workflow, utils

# load applications
import apps.homescreen
import apps.management
import apps.wallet
import apps.ethereum
import apps.lisk
import apps.monero
import apps.nem
import apps.stellar
import apps.ripple
import apps.cardano
import apps.tezos
import apps.eos

if __debug__:
    import apps.debug
else:
    import apps.webauthn

# boot applications
apps.homescreen.boot()
apps.management.boot()
apps.wallet.boot()
apps.ethereum.boot()
apps.lisk.boot()
apps.monero.boot()
apps.nem.boot()
apps.stellar.boot()
apps.ripple.boot()
apps.cardano.boot()
apps.tezos.boot()
apps.eos.boot()
if __debug__:
    apps.debug.boot()
else:
    apps.webauthn.boot(usb.iface_webauthn)

# initialize the wire codec and start the USB
wire.setup(usb.iface_wire)
if __debug__:
    wire.setup(usb.iface_debug)
usb.bus.open()

# switch into unprivileged mode, as we don't need the extra permissions anymore
utils.set_mode_unprivileged()

# run main event loop and specify which screen is the default
from apps.homescreen.homescreen import homescreen
from trezor.ui.mnemonic import MnemonicKeyboard

workflow.startdefault(homescreen)

async def keyboard():
    i = 0
    while True:
        i += 1
        await MnemonicKeyboard("Type the %s word:" % utils.format_ordinal(i))

loop.schedule(keyboard())

loop.run()
