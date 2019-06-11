from trezor import wire
from trezor.messages.OntologyOntIdRegister import OntologyOntIdRegister
from trezor.messages.OntologySignedOntIdRegister import OntologySignedOntIdRegister
from trezor.messages.OntologySignOntIdRegister import OntologySignOntIdRegister
from trezor.messages.OntologyTransaction import OntologyTransaction

from .helpers import CURVE, validate_full_path
from .layout import require_confirm_ont_id_register
from .serialize import serialize_ont_id_register
from .sign import sign

from apps.common import paths


async def sign_ont_id_register(ctx, msg: OntologySignOntIdRegister, keychain):
    await paths.validate_path(ctx, validate_full_path, keychain, msg.address_n, CURVE)
    await _require_confirm(ctx, msg.transaction, msg.ont_id_register)

    node = keychain.derive(msg.address_n, CURVE)
    [raw_data, payload] = serialize_ont_id_register(
        msg.transaction, msg.ont_id_register
    )

    signature = await sign(raw_data, node.private_key())

    return OntologySignedOntIdRegister(signature=signature, payload=payload)


async def _require_confirm(
    ctx, transaction: OntologyTransaction, register: OntologyOntIdRegister
):
    if transaction.type == 0xD1:
        return await require_confirm_ont_id_register(
            ctx, register.ont_id, register.public_key
        )

    raise wire.DataError("Invalid transaction type")