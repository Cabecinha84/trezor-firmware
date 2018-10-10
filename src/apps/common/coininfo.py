# generated from coininfo.py.mako
# do not edit manually!
from trezor.crypto.base58 import blake256_32, groestl512d_32, sha256d_32
from trezor.crypto.scripts import blake256_ripemd160_digest, sha256_ripemd160_digest


class CoinInfo:
    def __init__(
        self,
        coin_name: str,
        coin_shortcut: str,
        address_type: int,
        address_type_p2sh: int,
        maxfee_kb: int,
        signed_message_header: str,
        xpub_magic: int,
        xpub_magic_segwit_p2sh: int,
        xpub_magic_segwit_native: int,
        bech32_prefix: str,
        cashaddr_prefix: str,
        slip44: int,
        segwit: bool,
        fork_id: int,
        force_bip143: bool,
        version_group_id: int,
        bip115: bool,
        decred: bool,
        curve_name: str,
    ):
        self.coin_name = coin_name
        self.coin_shortcut = coin_shortcut
        self.address_type = address_type
        self.address_type_p2sh = address_type_p2sh
        self.maxfee_kb = maxfee_kb
        self.signed_message_header = signed_message_header
        self.xpub_magic = xpub_magic
        self.xpub_magic_segwit_p2sh = xpub_magic_segwit_p2sh
        self.xpub_magic_segwit_native = xpub_magic_segwit_native
        self.bech32_prefix = bech32_prefix
        self.cashaddr_prefix = cashaddr_prefix
        self.slip44 = slip44
        self.segwit = segwit
        self.fork_id = fork_id
        self.force_bip143 = force_bip143
        self.version_group_id = version_group_id
        self.bip115 = bip115
        self.decred = decred
        self.curve_name = curve_name
        if curve_name == "secp256k1-groestl":
            self.b58_hash = groestl512d_32
            self.sign_hash_double = False
            self.script_hash = sha256_ripemd160_digest
        elif curve_name == "secp256k1-decred":
            self.b58_hash = blake256_32
            self.sign_hash_double = False
            self.script_hash = blake256_ripemd160_digest
        else:
            self.b58_hash = sha256d_32
            self.sign_hash_double = True
            self.script_hash = sha256_ripemd160_digest


# fmt: off
COINS = [
    CoinInfo(
        coin_name="Bitcoin",
        coin_shortcut="BTC",
        address_type=0,
        address_type_p2sh=5,
        maxfee_kb=2000000,
        signed_message_header="Bitcoin Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=0x049d7cb2,
        xpub_magic_segwit_native=0x04b24746,
        bech32_prefix="bc",
        cashaddr_prefix=None,
        slip44=0,
        segwit=True,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Testnet",
        coin_shortcut="TEST",
        address_type=111,
        address_type_p2sh=196,
        maxfee_kb=10000000,
        signed_message_header="Bitcoin Signed Message:\n",
        xpub_magic=0x043587cf,
        xpub_magic_segwit_p2sh=0x044a5262,
        xpub_magic_segwit_native=0x045f1cf6,
        bech32_prefix="tb",
        cashaddr_prefix=None,
        slip44=1,
        segwit=True,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Bcash",
        coin_shortcut="BCH",
        address_type=0,
        address_type_p2sh=5,
        maxfee_kb=500000,
        signed_message_header="Bitcoin Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix="bitcoincash",
        slip44=145,
        segwit=False,
        fork_id=0,
        force_bip143=True,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Bcash Testnet",
        coin_shortcut="TBCH",
        address_type=111,
        address_type_p2sh=196,
        maxfee_kb=10000000,
        signed_message_header="Bitcoin Signed Message:\n",
        xpub_magic=0x043587cf,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix="bchtest",
        slip44=1,
        segwit=False,
        fork_id=0,
        force_bip143=True,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Bgold",
        coin_shortcut="BTG",
        address_type=38,
        address_type_p2sh=23,
        maxfee_kb=500000,
        signed_message_header="Bitcoin Gold Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=0x049d7cb2,
        xpub_magic_segwit_native=None,
        bech32_prefix="btg",
        cashaddr_prefix=None,
        slip44=156,
        segwit=True,
        fork_id=79,
        force_bip143=True,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Bgold Testnet",
        coin_shortcut="TBTG",
        address_type=111,
        address_type_p2sh=196,
        maxfee_kb=500000,
        signed_message_header="Bitcoin Gold Signed Message:\n",
        xpub_magic=0x043587cf,
        xpub_magic_segwit_p2sh=0x044a5262,
        xpub_magic_segwit_native=None,
        bech32_prefix="tbtg",
        cashaddr_prefix=None,
        slip44=156,
        segwit=True,
        fork_id=79,
        force_bip143=True,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Bprivate",
        coin_shortcut="BTCP",
        address_type=4901,
        address_type_p2sh=5039,
        maxfee_kb=1000000,
        signed_message_header="BitcoinPrivate Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=183,
        segwit=False,
        fork_id=42,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Dash",
        coin_shortcut="DASH",
        address_type=76,
        address_type_p2sh=16,
        maxfee_kb=100000,
        signed_message_header="DarkCoin Signed Message:\n",
        xpub_magic=0x02fe52cc,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=5,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Dash Testnet",
        coin_shortcut="tDASH",
        address_type=140,
        address_type_p2sh=19,
        maxfee_kb=100000,
        signed_message_header="DarkCoin Signed Message:\n",
        xpub_magic=0x043587cf,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=1,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Decred",
        coin_shortcut="DCR",
        address_type=1855,
        address_type_p2sh=1818,
        maxfee_kb=1000000,
        signed_message_header="Decred Signed Message:\n",
        xpub_magic=0x02fda926,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=42,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=True,
        curve_name='secp256k1-decred',
    ),
    CoinInfo(
        coin_name="Decred Testnet",
        coin_shortcut="TDCR",
        address_type=3873,
        address_type_p2sh=3836,
        maxfee_kb=10000000,
        signed_message_header="Decred Signed Message:\n",
        xpub_magic=0x043587d1,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=1,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=True,
        curve_name='secp256k1-decred',
    ),
    CoinInfo(
        coin_name="Denarius",
        coin_shortcut="DNR",
        address_type=30,
        address_type_p2sh=90,
        maxfee_kb=100000,
        signed_message_header="Denarius Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=116,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="DigiByte",
        coin_shortcut="DGB",
        address_type=30,
        address_type_p2sh=63,
        maxfee_kb=500000,
        signed_message_header="DigiByte Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=0x049d7cb2,
        xpub_magic_segwit_native=None,
        bech32_prefix="dgb",
        cashaddr_prefix=None,
        slip44=20,
        segwit=True,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Dogecoin",
        coin_shortcut="DOGE",
        address_type=30,
        address_type_p2sh=22,
        maxfee_kb=1000000000,
        signed_message_header="Dogecoin Signed Message:\n",
        xpub_magic=0x02facafd,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=3,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Feathercoin",
        coin_shortcut="FTC",
        address_type=14,
        address_type_p2sh=5,
        maxfee_kb=40000000,
        signed_message_header="Feathercoin Signed Message:\n",
        xpub_magic=0x0488bc26,
        xpub_magic_segwit_p2sh=0x049d7cb2,
        xpub_magic_segwit_native=None,
        bech32_prefix="fc",
        cashaddr_prefix=None,
        slip44=8,
        segwit=True,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Flashcoin",
        coin_shortcut="FLASH",
        address_type=68,
        address_type_p2sh=130,
        maxfee_kb=4000000,
        signed_message_header="Flashcoin Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=0x049d7cb2,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=120,
        segwit=True,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Fujicoin",
        coin_shortcut="FJC",
        address_type=36,
        address_type_p2sh=16,
        maxfee_kb=10000000,
        signed_message_header="FujiCoin Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=0x049d7cb2,
        xpub_magic_segwit_native=0x04b24746,
        bech32_prefix="fc",
        cashaddr_prefix=None,
        slip44=75,
        segwit=True,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Groestlcoin",
        coin_shortcut="GRS",
        address_type=36,
        address_type_p2sh=5,
        maxfee_kb=100000,
        signed_message_header="GroestlCoin Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=0x049d7cb2,
        xpub_magic_segwit_native=0x04b24746,
        bech32_prefix="grs",
        cashaddr_prefix=None,
        slip44=17,
        segwit=True,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1-groestl',
    ),
    CoinInfo(
        coin_name="Groestlcoin Testnet",
        coin_shortcut="tGRS",
        address_type=111,
        address_type_p2sh=196,
        maxfee_kb=100000,
        signed_message_header="GroestlCoin Signed Message:\n",
        xpub_magic=0x043587cf,
        xpub_magic_segwit_p2sh=0x044a5262,
        xpub_magic_segwit_native=0x045f1cf6,
        bech32_prefix="tgrs",
        cashaddr_prefix=None,
        slip44=1,
        segwit=True,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1-groestl',
    ),
    CoinInfo(
        coin_name="Koto",
        coin_shortcut="KOTO",
        address_type=6198,
        address_type_p2sh=6203,
        maxfee_kb=1000000,
        signed_message_header="Koto Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=510,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=0x02e7d970,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Litecoin",
        coin_shortcut="LTC",
        address_type=48,
        address_type_p2sh=50,
        maxfee_kb=40000000,
        signed_message_header="Litecoin Signed Message:\n",
        xpub_magic=0x019da462,
        xpub_magic_segwit_p2sh=0x01b26ef6,
        xpub_magic_segwit_native=None,
        bech32_prefix="ltc",
        cashaddr_prefix=None,
        slip44=2,
        segwit=True,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Litecoin Testnet",
        coin_shortcut="TLTC",
        address_type=111,
        address_type_p2sh=58,
        maxfee_kb=40000000,
        signed_message_header="Litecoin Signed Message:\n",
        xpub_magic=0x043587cf,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix="tltc",
        cashaddr_prefix=None,
        slip44=1,
        segwit=True,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="MonetaryUnit",
        coin_shortcut="MUE",
        address_type=16,
        address_type_p2sh=76,
        maxfee_kb=100000,
        signed_message_header="MonetaryUnit Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=31,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Monacoin",
        coin_shortcut="MONA",
        address_type=50,
        address_type_p2sh=55,
        maxfee_kb=5000000,
        signed_message_header="Monacoin Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=0x049d7cb2,
        xpub_magic_segwit_native=None,
        bech32_prefix="mona",
        cashaddr_prefix=None,
        slip44=22,
        segwit=True,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Myriad",
        coin_shortcut="XMY",
        address_type=50,
        address_type_p2sh=9,
        maxfee_kb=2000000,
        signed_message_header="Myriadcoin Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=90,
        segwit=True,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Namecoin",
        coin_shortcut="NMC",
        address_type=52,
        address_type_p2sh=5,
        maxfee_kb=10000000,
        signed_message_header="Namecoin Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=7,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Pesetacoin",
        coin_shortcut="PTC",
        address_type=47,
        address_type_p2sh=22,
        maxfee_kb=1000000000,
        signed_message_header="Pesetacoin Signed Message:\n",
        xpub_magic=0x0488c42e,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix="null",
        cashaddr_prefix=None,
        slip44=109,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="SmartCash",
        coin_shortcut="SMART",
        address_type=63,
        address_type_p2sh=18,
        maxfee_kb=1000000,
        signed_message_header="SmartCash Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=224,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1-smart',
    ),
    CoinInfo(
        coin_name="SmartCash Testnet",
        coin_shortcut="tSMART",
        address_type=65,
        address_type_p2sh=21,
        maxfee_kb=1000000,
        signed_message_header="SmartCash Signed Message:\n",
        xpub_magic=0x043587cf,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=224,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1-smart',
    ),
    CoinInfo(
        coin_name="Vertcoin",
        coin_shortcut="VTC",
        address_type=71,
        address_type_p2sh=5,
        maxfee_kb=40000000,
        signed_message_header="Vertcoin Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=0x049d7cb2,
        xpub_magic_segwit_native=None,
        bech32_prefix="vtc",
        cashaddr_prefix=None,
        slip44=28,
        segwit=True,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Viacoin",
        coin_shortcut="VIA",
        address_type=71,
        address_type_p2sh=33,
        maxfee_kb=40000000,
        signed_message_header="Viacoin Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=0x049d7cb2,
        xpub_magic_segwit_native=None,
        bech32_prefix="via",
        cashaddr_prefix=None,
        slip44=14,
        segwit=True,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Zcash",
        coin_shortcut="ZEC",
        address_type=7352,
        address_type_p2sh=7357,
        maxfee_kb=1000000,
        signed_message_header="Zcash Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=133,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=0x03c48270,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Zcash Testnet",
        coin_shortcut="TAZ",
        address_type=7461,
        address_type_p2sh=7354,
        maxfee_kb=10000000,
        signed_message_header="Zcash Signed Message:\n",
        xpub_magic=0x043587cf,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=1,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=0x03c48270,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Zcoin",
        coin_shortcut="XZC",
        address_type=82,
        address_type_p2sh=7,
        maxfee_kb=1000000,
        signed_message_header="Zcoin Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=136,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Zcoin Testnet",
        coin_shortcut="tXZC",
        address_type=65,
        address_type_p2sh=178,
        maxfee_kb=1000000,
        signed_message_header="Zcoin Signed Message:\n",
        xpub_magic=0x043587cf,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=1,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=False,
        decred=False,
        curve_name='secp256k1',
    ),
    CoinInfo(
        coin_name="Zencash",
        coin_shortcut="ZEN",
        address_type=8329,
        address_type_p2sh=8342,
        maxfee_kb=2000000,
        signed_message_header="Zencash Signed Message:\n",
        xpub_magic=0x0488b21e,
        xpub_magic_segwit_p2sh=None,
        xpub_magic_segwit_native=None,
        bech32_prefix=None,
        cashaddr_prefix=None,
        slip44=121,
        segwit=False,
        fork_id=None,
        force_bip143=False,
        version_group_id=None,
        bip115=True,
        decred=False,
        curve_name='secp256k1',
    ),
]