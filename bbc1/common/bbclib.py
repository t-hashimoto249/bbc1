# -*- coding: utf-8 -*-
"""
Copyright (c) 2017 beyond-blockchain.org.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import sys
import binascii
import hashlib
import random
import socket
import time
import traceback

import ecdsa
import ecdsa.ellipticcurve
from ecdsa import SigningKey, VerifyingKey

sys.path.append("../../")
from bbc1.common.bbc_error import *
from third_party.bbc1_serializer import *
from ctypes import *

LIB_NAME = "../third_party/lib_bbc1_serializer.so"
LIBC = cdll.LoadLibrary(LIB_NAME)

ECDSA_CURVE = ecdsa.SECP256k1

domain_global_0 = binascii.a2b_hex("0000000000000000000000000000000000000000000000000000000000000000")

error_code = -1
error_text = ""


def set_error(code=-1, txt=""):
    global error_code
    global error_text
    error_code = code
    error_text = txt


def reset_error():
    global error_code
    global error_text
    error_code = ESUCCESS
    error_text = ""


def get_new_id(seed_str=None, include_timestamp=True):
    if seed_str is None:
        return get_random_id()
    if include_timestamp:
        seed_str += "%f" % time.time()
    return hashlib.sha256(bytes(seed_str.encode())).digest()


def get_random_id():
    source_str = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output = "".join([random.choice(source_str) for x in range(16)])
    return hashlib.sha256(bytes(output.encode())).digest()


def get_random_value(length=8):
    val = bytearray()
    for i in range(length):
        val.append(random.randint(0,255))
    return bytes(val)


def convert_id_to_string(data, bytelen=32):
    res = binascii.b2a_hex(data)
    if len(res) < bytelen*2:
        res += "0"*(bytelen*2-len(res)) + res
    return res.decode()


def convert_idstring_to_bytes(datastr, bytelen=32):
    res = bytearray(binascii.a2b_hex(datastr))
    if len(res) < bytelen:
        res = bytearray([0]*(bytelen-len(res))).extend(res)
    return bytes(res)


def make_transaction_for_base_asset(asset_group_id=None, event_num=1):
    transaction = BBcTransaction()
    for i in range(event_num):
        evt = BBcEvent(asset_group_id=asset_group_id)
        ast = BBcAsset()
        evt.add(asset=ast)
        transaction.add(event=evt)
    return transaction


def add_reference_to_transaction(asset_group_id, transaction, ref_transaction_obj, event_index_in_ref):
    ref = BBcReference(asset_group_id=asset_group_id,
                       transaction=transaction, ref_transaction=ref_transaction_obj, event_index_in_ref=event_index_in_ref)
    if ref.transaction_id is None:
        return None
    transaction.add(reference=ref)
    return ref


def recover_transaction_object_from_rawdata(data):
    transaction = BBcTransaction()
    transaction.deserialize(data)
    return transaction


def recover_signature_object(data):
    sig = BBcSignature()
    sig.deserialize(data)
    return sig


def to_bigint(val, size=32):
    dat = bytearray(to_2byte(size))
    dat.extend(val)
    return dat


def to_8byte(val):
    return val.to_bytes(8, 'little')


def to_4byte(val):
    return val.to_bytes(4, 'little')


def to_2byte(val):
    return val.to_bytes(2, 'little')


def get_n_bytes(ptr, n, dat):
    return ptr+n, dat[ptr:ptr+n]


def get_n_byte_int(ptr, n, dat):
    return ptr+n, int.from_bytes(dat[ptr:ptr+n], 'little')


def get_bigint(ptr, dat):
    size = int.from_bytes(dat[ptr:ptr+2], 'little')
    return ptr+2+size, dat[ptr+2:ptr+2+size]


class KeyType:
    ECDSA_SECP256k1_XY = 1
    ECDSA_SECP256k1_X = 2


class KeyPair:
    def __init__(self, type=KeyType.ECDSA_SECP256k1_XY, privkey=None, pubkey=None):
        self.type = type
        self.private_key = privkey
        self.private_key_object = None
        self.mk_keyobj_from_private_key()
        self.public_key = pubkey
        self.public_key_object = None
        self.mk_public_keyobj()
        self.key_len = 0

    def generate(self):
        if self.type == KeyType.ECDSA_SECP256k1_XY or self.type == KeyType.ECDSA_SECP256k1_X:
            self.private_key_object = SigningKey.generate(curve=ECDSA_CURVE)
            self.public_key_object = self.private_key_object.get_verifying_key()
            self.key_len = len(self.to_binary(self.private_key_object.privkey.order))
            self.private_key = bytes(self.to_binary(self.private_key_object.privkey.secret_multiplier))
            self.public_key = self.to_binary(self.public_key_object.pubkey.point.x())
            if self.type == KeyType.ECDSA_SECP256k1_XY:
                self.public_key.extend(self.to_binary(self.public_key_object.pubkey.point.y()))
            self.public_key = bytes(self.public_key)

    def mk_keyobj_from_private_key(self):
        if self.private_key is None:
            return
        if self.type != KeyType.ECDSA_SECP256k1_X and self.type != KeyType.ECDSA_SECP256k1_XY:
            return
        self.private_key_object = SigningKey.from_secret_exponent(self.to_bigint(self.private_key), curve=ECDSA_CURVE)
        self.public_key_object = self.private_key_object.get_verifying_key()

    def mk_keyobj_from_private_key_pem(self, pemdat):
        self.private_key_object = SigningKey.from_pem(pemdat, curve=ECDSA_CURVE)
        self.public_key_object = self.private_key.get_verifying_key()

    def mk_public_keyobj(self):
        if self.public_key is None:
            return
        if self.type == KeyType.ECDSA_SECP256k1_XY:
            self.key_len = int(len(self.public_key)/2)
            x = self.to_bigint(self.public_key[0:self.key_len])
            y = self.to_bigint(self.public_key[self.key_len:self.key_len*2])
            point = ecdsa.ellipticcurve.Point(ECDSA_CURVE.curve, x, y)
            if not ecdsa.ecdsa.point_is_valid(ECDSA_CURVE.generator, x, y):
                return
            self.public_key_object = VerifyingKey.from_public_point(point, curve=ECDSA_CURVE)
        elif self.type == KeyType.ECDSA_SECP256k1_X:
            self.key_len = len(self.public_key)
            x = self.to_bigint(self.public_key)
            # TODO: calc Y and make point object(X,Y)
            pass

    def to_binary(self, dat):
        byteval = bytearray()
        if self.key_len > 0:
            for i in range(self.key_len):
                byteval.append(dat % 256)
                dat = dat // 256
        else:
            while True:
                byteval.append(dat % 256)
                dat = dat // 256
                if dat == 0:
                    break
        return byteval

    def to_bigint(self, dat):
        intval = 0
        for i in range(len(dat)):
            intval += int(dat[i])*(256**i)
        return intval

    def get_private_key_in_der(self):
        return self.private_key_object.to_der()

    def get_private_key_in_pem(self):
        return self.private_key_object.to_pem()


class BBcSignature:
    def __init__(self, key_type=KeyType.ECDSA_SECP256k1_XY):
        self.type = key_type
        self.signature = None
        self.pubkey = None
        self.keypair = None

        self.serializer = Signature(LIBC)

    def add(self, signature=None, pubkey=None):
        if signature is not None:
            self.signature = signature
            print("signature:::::::::",signature)
        if pubkey is not None:
            self.pubkey = pubkey
            self.keypair = KeyPair(type=self.type, pubkey=pubkey)
        return True

    def serialize(self):
        self.serializer.inited()
        self.serializer.set_type(self.type)

        if self.pubkey != None and len(self.signature) != 0:
            self.serializer.set_public_key_length(len(self.pubkey))
            self.serializer.set_public_key(self.pubkey)
        else:
            self.serializer.set_public_key_length(0)

        if self.signature != None and len(self.signature) != 0:
            self.serializer.set_signature_length(len(self.signature))
            self.serializer.set_signature(self.signature)
        else:
            self.serializer.set_signature_length(0)

        return self.serializer.get_packet()

    def deserialize(self, data):
        self.serializer.inited()
        try:
            LIBC.parse_Signature(data, byref(self.serializer))
            self.type = self.serializer.get_type()

            if self.serializer.get_public_key_length() != 0:
                self.pubkey = self.serializer.get_public_key()
            #else:
            #    self.pubkey = bytes()

            if self.serializer.get_signature_length() != 0:
                self.signature = self.serializer.get_signature()
            #else:
            #    self.signature = bytes()

            self.add(signature=self.signature, pubkey=self.pubkey)
            LIBC.free_Signiture(byref(self.serializer))

        except:
            return False
        return True

    def verify(self, digest):
        reset_error()
        if self.keypair is None:
            set_error(code=EBADKEYPAIR, txt="Bad private_key/public_key")
            return False
        try:
            flag = self.keypair.public_key_object.verify(self.signature, digest)
        except:
            return False
        return flag


class BBcTransaction:
    def __init__(self, version=0):
        self.version = version
        self.timestamp = int(time.time())
        self.events = []
        self.references = []
        self.cross_refs = []
        self.signatures = []
        self.userid_sigidx_mapping = dict()
        self.transaction_id = None
        self.transaction_base_digest = None

        self.serializer = Transaction(LIBC)
        self.transaction_base = Transaction_Base(LIBC)
        self.intermediate = Intermediate(LIBC)

    def add(self, event=None, reference=None, cross_ref=None):
        if event is not None:
            if isinstance(event, list):
                self.events.extend(event)
            else:
                self.events.append(event)
        if reference is not None:
            if isinstance(reference, list):
                self.references.extend(reference)
            else:
                self.references.append(reference)
        if cross_ref is not None:
            if isinstance(cross_ref, list):
                self.cross_refs.extend(cross_ref)
            else:
                self.cross_refs.append(cross_ref)
        return True

    def get_sig_index(self, user_id):
        if user_id not in self.userid_sigidx_mapping:
            self.userid_sigidx_mapping[user_id] = len(self.userid_sigidx_mapping)
            self.signatures.append(None)
        return self.userid_sigidx_mapping[user_id]

    def add_signature(self, user_id=None, signature=None):
        if user_id not in self.userid_sigidx_mapping:
            return False
        idx = self.userid_sigidx_mapping[user_id]
        self.signatures[idx] = signature
        return True

    def digest(self):
        target = self.serialize(for_id=True)
        d = hashlib.sha256(target).digest()
        self.transaction_id = d
        return d

    def serialize(self, for_id=False):
        if for_id:

            self.transaction_base.inited()

            self.transaction_base.set_version(self.version)
            self.transaction_base.set_timestamp(self.timestamp)

            if len(self.events) > 0:
                for i in range(len(self.events)):
                    u_byte = self.events[i].serialize()
                    LIBC.add_to_events_list_of_Transaction_Base(byref(self.transaction_base), len(u_byte), u_byte);

            if len(self.references) > 0:
                for i in range(len(self.references)):
                    u_byte = self.references[i].serialize()
                    LIBC.add_to_references_list_of_Transaction_Base(byref(self.transaction_base),  len(u_byte), u_byte);

            intermediate = self.transaction_base.get_packet()
            intermediate_txid = hashlib.sha256(intermediate).digest()

            self.intermediate.inited()
            self.intermediate.get_transaction_base_digest().set_value(intermediate_txid)
            self.intermediate.get_transaction_base_digest().set_len(len(intermediate_txid))

            if len(self.cross_refs) > 0:
                for i in range(len(self.cross_refs)):
                    u_byte = self.cross_refs[i].serialize()
                    LIBC.add_to_cross_refs_list_of_Intermediate(byref(self.intermediate),  len(u_byte), u_byte)

            packet = self.intermediate.get_packet()

            LIBC.free_events_of_Transaction_Base(byref(self.transaction_base))
            LIBC.free_references_of_Transaction_Base(byref(self.transaction_base))
            LIBC.free_cross_refs_of_Intermediate(byref(self.intermediate))
            return packet

        else:

            self.serializer.inited()

            self.serializer.set_version(self.version)
            self.serializer.set_timestamp(self.timestamp)

            for i in range(len(self.events)):
                u_byte = self.events[i].serialize()
                LIBC.add_to_events_list_of_Transaction(byref(self.serializer),
                                                 len(u_byte), u_byte)

            for i in range(len(self.references)):
                u_byte = self.references[i].serialize()
                LIBC.add_to_references_list_of_Transaction(byref(self.serializer),
                                                     len(u_byte), u_byte)

            for i in range(len(self.cross_refs)):
                u_byte = self.cross_refs[i].serialize()
                LIBC.add_to_cross_refs_list_of_Transaction(byref(self.serializer),
                                                      len(u_byte), u_byte)

            for i in range(len(self.signatures)):
                if self.signatures[i] is not None:
                    b_byte = self.signatures[i].serialize()
                    LIBC.add_to_signatures_list_of_Transaction(byref(self.serializer),
                                                          len(b_byte), b_byte)
                else:

                    b_byte = bytes(0x00)
                    LIBC.add_to_signatures_list_of_Transaction(byref(self.serializer),
                                                          len(b_byte), b_byte)

            packet = self.serializer.get_packet()
            LIBC.free_events_of_Transaction(byref(self.serializer))
            LIBC.free_references_of_Transaction(byref(self.serializer))
            LIBC.free_cross_refs_of_Transaction(byref(self.serializer))
            LIBC.free_signatures_of_Transaction(byref(self.serializer))
            return packet

    def deserialize(self, data):
        self.serializer.inited()
        try:
            LIBC.parse_Transaction(data, byref(self.serializer))

            self.version = self.serializer.get_version()
            self.timestamp = self.serializer.get_timestamp()

            if self.serializer.get_event_num() > 0:
                self.events = [BBcEvent() for i in range(self.serializer.get_event_num())]
                for i in range(self.serializer.get_event_num()):
                    self.events[i].deserialize(self.serializer.get_events_list_using_index(i).get_Length_Value_value())

            if self.serializer.get_reference_num() > 0:
                self.references = [BBcReference(None, None) for i in range(self.serializer.get_reference_num())]
                for i in range(self.serializer.get_reference_num()):
                    self.references[i].deserialize(
                        self.serializer.get_references_list_using_index(i).get_Length_Value_value())

            if self.serializer.get_cross_ref_num() > 0:
                self.cross_refs = [BBcCrossRef() for i in range(self.serializer.get_cross_ref_num())]
                for i in range(self.serializer.get_cross_ref_num()):
                    self.cross_refs[i].deserialize(
                        self.serializer.get_cross_refs_list_using_index(i).get_Length_Value_value())

            if self.serializer.get_signature_num() > 0:
                self.signatures = [BBcSignature() for i in range(self.serializer.get_signature_num())]
                for i in range(self.serializer.get_signature_num()):
                    if self.serializer.get_signatures_list_using_index(i).get_Length_Value_value() != bytes(0x00):
                        self.signatures[i].deserialize(
                            self.serializer.get_signatures_list_using_index(i).get_Length_Value_value())
            self.digest()
            LIBC.free_Transaction(byref(self.serializer))
        except Exception as e:
            print("Transaction data deserialize: %s" % e)
            print(traceback.format_exc())
            return False
        return True

    def sign(self, key_type=KeyType.ECDSA_SECP256k1_XY, private_key=None, public_key=None, keypair=None):
        """
        Sign transaction
        :param key_type: KeyType.ECDSA_SECP256k1_XY/X
        :param private_key: bytes format
        :param public_key: bytes format
        :return: BBcSignature object
        """
        reset_error()
        if keypair is None:
            if not isinstance(private_key, bytes) or not isinstance(public_key, bytes):
                set_error(code=EBADKEYPAIR, txt="Bad private_key/public_key (must be in bytes format)")
                return None
            keypair = KeyPair(type=key_type, privkey=private_key, pubkey=public_key)
            if keypair is None:
                set_error(code=EBADKEYPAIR, txt="Bad private_key/public_key")
                return None

        sig = BBcSignature(key_type=keypair.type)
        if keypair.type == KeyType.ECDSA_SECP256k1_XY or keypair.type == KeyType.ECDSA_SECP256k1_X:
            s = keypair.private_key_object.sign(self.digest())
        else:
            set_error(code=EOTHER, txt="sig_type %d is not supported" % keypair.type)
            return None
        sig.add(signature=s, pubkey=keypair.public_key)
        return sig

    def dump(self):
        import binascii
        print("------- Dump of the transaction data ------")
        if self.transaction_id is not None:
            print("transaction_id:", binascii.b2a_hex(self.transaction_id))
        else:
            print("transaction_id: None")
        print("version:", self.version)
        print("timestamp:", self.timestamp)
        print("Event[]:")
        if len(self.events) > 0:
            for i, evt in enumerate(self.events):
                print("[%d]" % i)
                print("  asset_group_id:", binascii.b2a_hex(evt.asset_group_id))
                print("  reference_indices:", evt.reference_indices)
                print("  mandatory_approvers:")
                if len(evt.mandatory_approvers) > 0:
                    for user in evt.mandatory_approvers:
                        print("    - ", binascii.b2a_hex(user))
                else:
                    print("    - NONE")
                print("  option_approvers:")
                if len(evt.option_approvers) > 0:
                    for user in evt.option_approvers:
                        print("    - ", binascii.b2a_hex(user))
                else:
                    print("    - NONE")
                print("  option_approver_num_numerator:", evt.option_approver_num_numerator)
                print("  option_approver_num_denominator:", evt.option_approver_num_denominator)
                print("  Asset:")
                print("     asset_id:", binascii.b2a_hex(evt.asset.asset_id))
                if evt.asset.user_id is not None:
                    print("     user_id:", binascii.b2a_hex(evt.asset.user_id))
                else:
                    print("     user_id: NONE")
                print("     nonce:", binascii.b2a_hex(evt.asset.nonce))
                print("     file_size:", evt.asset.asset_file_size)
                if evt.asset.asset_file_digest is not None:
                    print("     file_digest:", binascii.b2a_hex(evt.asset.asset_file_digest))
                print("     body_size:", evt.asset.asset_body_size)
                print("     body:", evt.asset.asset_body)
        else:
            print("  None")
        print("Reference[]:",len(self.references))
        if len(self.references) > 0:
            for i, refe in enumerate(self.references):
                print("[%d]" % i)
                print("  asset_group_id:", binascii.b2a_hex(refe.asset_group_id))
                print("  transaction_id:", binascii.b2a_hex(refe.transaction_id))
                print("  event_index_in_ref:", refe.event_index_in_ref)
                print("  sig_index:", refe.sig_indices)
        else:
            print("  None")
        print("Cross_Ref[]:",len(self.cross_refs))
        if len(self.cross_refs) > 0:
            for i, cross in enumerate(self.cross_refs):
                print("[%d]" % i)
                print("  asset_group_id:", binascii.b2a_hex(cross.asset_group_id))
                print("  transaction_id:", binascii.b2a_hex(cross.transaction_id))
        else:
            print("  None")
        print("Signature[]:")
        if len(self.signatures) > 0:
            for i, sig in enumerate(self.signatures):
                print("[%d]" % i)
                if sig is None:
                    print("  *RESERVED*")
                    continue
                print("  type:", sig.type)
                print("  signature:", binascii.b2a_hex(sig.signature))
                print("  pubkey:", binascii.b2a_hex(sig.pubkey))
        else:
            print("  None")


class BBcEvent:
    def __init__(self, asset_group_id=None):
        self.asset_group_id = asset_group_id
        self.reference_indices = []
        self.mandatory_approvers = []
        self.option_approver_num_numerator = 0
        self.option_approver_num_denominator = 0
        self.option_approvers = []
        self.asset = None

        self.serializer = Event(LIBC)

    def add(self, asset_group_id=None, reference_index=None, mandatory_approver=None,
            option_approver_num_numerator=0, option_approver_num_denominator=0,
            option_approver=None, asset=None):
        if asset_group_id is not None:
            self.asset_group_id = asset_group_id
        if reference_index is not None:
            self.reference_indices.append(reference_index)
        if mandatory_approver is not None:
            self.mandatory_approvers.append(mandatory_approver)
        if option_approver_num_numerator > 0:
            self.option_approver_num_numerator = option_approver_num_numerator
        if option_approver_num_denominator > 0:
            self.option_approver_num_denominator = option_approver_num_denominator
        if option_approver is not None:
            self.option_approvers.append(option_approver)
        if asset is not None:
            self.asset = asset
        return True


    def serialize(self):
        self.serializer.inited()

        if self.asset_group_id != None:
            self.serializer.get_asset_group_id().set_len(len(self.asset_group_id))
            self.serializer.get_asset_group_id().set_value(self.asset_group_id)
        else:
            self.serializer.get_asset_group_id().set_len(0)

        if self.reference_indices != None and len(self.reference_indices) > 0:
            for i in range(len(self.reference_indices)):
                uint16_list = List_c_uint16(LIBC)
                u_byte = self.reference_indices[i]
                uint16_list.set_c_uint16_value(u_byte)
                self.serializer.add_to_reference_indices_list(uint16_list)
        else:
            self.serializer.set_reference_num(0)

        if self.mandatory_approvers != None and len(self.mandatory_approvers) > 0:
            for i in range(len(self.mandatory_approvers)):
                u_byte = self.mandatory_approvers[i]
                LIBC.add_to_mandatory_approvers_list_of_Event(byref(self.serializer), len(u_byte), u_byte);

        else:
            self.serializer.set_mandatory_approver_num(0)

        self.serializer.set_option_approval_numerator(self.option_approver_num_numerator)

        if len(self.option_approvers) != None and len(self.option_approvers) > 0:
            for i in range(len(self.option_approvers)):
                u_byte = self.option_approvers[i]
                LIBC.add_to_option_approvers_list_of_Event(byref(self.serializer), len(u_byte), u_byte);

        else:
            self.serializer.set_option_approval_denominator(0)

        if self.asset != None:
            a_byte = self.asset.serialize()
            self.serializer.set_asset(a_byte)
            self.serializer.set_asset_length(len(a_byte))
        else:
            self.serializer.set_asset_length(0)

        packet = self.serializer.get_packet()
        LIBC.free_mandatory_approvers_of_Event(byref(self.serializer))
        LIBC.free_option_approvers_of_Event(byref(self.serializer))

        return packet

    def deserialize(self, data):
        self.serializer.inited()
        try:
            LIBC.parse_Event(data, byref(self.serializer))

            if self.serializer.get_asset_group_id().get_len() > 0:
                self.asset_group_id = self.serializer.get_asset_group_id().get_value()

            self.reference_indices = []
            if self.serializer.get_reference_num() > 0:
                for i in range(self.serializer.get_reference_num()):
                    u_byte = self.serializer.get_reference_indices_list_using_index(i).get_c_uint16_value()
                    self.reference_indices.append(u_byte)

            self.mandatory_approvers = []
            if self.serializer.get_mandatory_approver_num() > 0:
                for i in range(self.serializer.get_mandatory_approver_num()):
                    u_byte = self.serializer.get_mandatory_approvers_list_using_index(i).get_Length_Value_value()
                    self.mandatory_approvers.append(u_byte)

            self.option_approver_num_numerator = self.serializer.get_option_approval_numerator()
            self.option_approver_num_denominator = self.serializer.get_option_approval_denominator()

            self.option_approvers = []
            if self.option_approver_num_denominator > 0:
                for i in range(self.option_approver_num_denominator):
                    u_byte = self.serializer.get_option_approvers_list_using_index(i).get_Length_Value_value()
                    self.option_approvers.append(u_byte)

            self.asset = BBcAsset()
            if self.serializer.get_asset_length() > 0:
                b_asset = self.serializer.get_asset()
                self.asset.deserialize(b_asset)
            LIBC.free_Event(byref(self.serializer))
        except:
            print("Event_expect")
            return False

        return True


class BBcReference:
    def __init__(self, asset_group_id, transaction, ref_transaction=None, event_index_in_ref=0):
        self.asset_group_id = asset_group_id
        self.transaction_id = None
        self.transaction = transaction
        self.ref_transaction = ref_transaction
        self.event_index_in_ref = event_index_in_ref
        self.sig_indices = []
        self.mandatory_approvers = None
        self.option_approvers = None
        self.option_sig_ids = []

        self.serializer = Reference(LIBC)

        if ref_transaction is None:
            return
        self.prepare_reference(ref_transaction=ref_transaction)

    def prepare_reference(self, ref_transaction):
        self.ref_transaction = ref_transaction
        try:
            evt = ref_transaction.events[self.event_index_in_ref]
            for user in evt.mandatory_approvers:
                self.sig_indices.append(self.transaction.get_sig_index(user))
            for i in range(evt.option_approver_num_numerator):
                dummy_id = get_random_value(4)
                self.option_sig_ids.append(dummy_id)
                self.sig_indices.append(self.transaction.get_sig_index(dummy_id))
            self.mandatory_approvers = evt.mandatory_approvers
            self.option_approvers = evt.option_approvers
            self.transaction_id = ref_transaction.digest()
        except Exception as e:
            print(traceback.format_exc())

    def add_signature(self, user_id=None, signature=None):
        if user_id in self.option_approvers:
            if len(self.option_sig_ids) == 0:
                return
            user_id = self.option_sig_ids.pop(0)
        self.transaction.add_signature(user_id=user_id, signature=signature)

    def get_referred_transaction(self):
        return {self.ref_transaction.transaction_id: self.ref_transaction.serialize()}

    def get_destinations(self):
        return self.mandatory_approvers+self.option_approvers

    def serialize(self):
        self.serializer.inited()

        if self.asset_group_id != None:
            self.serializer.get_asset_group_id().set_len(len(self.asset_group_id))
            self.serializer.get_asset_group_id().set_value(self.asset_group_id)
        else:
            self.serializer.get_asset_group_id().set_len(0)

        if self.transaction_id != None:
            self.serializer.get_transaction_id().set_len(len(self.transaction_id))
            self.serializer.get_transaction_id().set_value(self.transaction_id)
        else:
            self.serializer.get_transaction_id().set_len(0)

        self.serializer.set_event_index(self.event_index_in_ref)
        length = len(self.sig_indices)
        if length != None and length != 0:
            for i in range(length):
                uint16_list = List_c_uint16(LIBC)
                u_byte = self.sig_indices[i]
                uint16_list.set_c_uint16_value(u_byte)
                self.serializer.add_to_signature_indices_list(uint16_list)

        return self.serializer.get_packet()

    def deserialize(self, data):
        self.serializer.inited()
        try:
            LIBC.parse_Reference(data, byref(self.serializer))

            if self.serializer.get_asset_group_id().get_len() != 0:
                self.asset_group_id = self.serializer.get_asset_group_id().get_value()
            else:
                self.asset_group_id = None

            if self.serializer.get_transaction_id().get_len() != 0:
                self.transaction_id = self.serializer.get_transaction_id().get_value()
            else:
                self.transaction_id = None

            self.event_index = self.serializer.get_event_index()
            self.sig_indices = []
            if self.serializer.get_signature_indice_num() != 0:
                for i in range(self.serializer.get_signature_indice_num()):

                    self.sig_indices.append(self.serializer.get_signature_indices_list_using_index(i).get_c_uint16_value())
            else:
                self.sig_indices = []
            LIBC.free_Reference(byref(self.serializer))
        except:
            return False
        return True

class BBcAsset:
    def __init__(self):
        self.asset_id = None
        self.user_id = None
        self.nonce = get_random_value()
        self.asset_file_size = 0
        self.asset_file = None
        self.asset_file_digest = None
        self.asset_body_size = 0
        self.asset_body = []    # up to 256 bytes

        self.serializer = Asset(LIBC)
        #self.asset_base = Asset_Base(LIBC)

    def add(self, user_id=None, asset_file=None, asset_body=None):
        if user_id is not None:
            self.user_id = user_id
        if asset_file is not None:
            self.asset_file = asset_file
            self.asset_file_size = len(asset_file)
            self.asset_file_digest = hashlib.sha256(asset_file).digest()
        if asset_body is not None:
            if len(asset_body) > 256:
                self.asset_file = asset_body
                self.asset_file_size = len(asset_body)
                self.asset_file_digest = hashlib.sha256(asset_body).digest()
            else:
                self.asset_body = asset_body
                if isinstance(asset_body, str):
                    self.asset_body = asset_body.encode()
                self.asset_body_size = len(asset_body)
        self.digest()

    def digest(self):
        target = self.serialize(for_digest_calculation=True)
        self.asset_id = hashlib.sha256(target).digest()
        return self.asset_id

    def get_asset_file(self):
        if self.asset_file is None:
            return None, None
        return self.asset_file_digest, self.asset_file

    def recover_asset_file(self, asset_file):
        digest = hashlib.sha256(asset_file).digest()
        if digest == self.asset_file_digest:
            self.asset_file = asset_file
            return True
        else:
            return False

    def serialize(self, for_digest_calculation=False):
        if for_digest_calculation:
            self.serializer.inited()
            if self.asset_id != None and self.asset_id != 0:
                u_byte = self.asset_id
                self.serializer.get_asset_id().set_len(len(u_byte))
                self.serializer.get_asset_id().set_value(u_byte)
            else:
               self.serializer.get_asset_id().set_len(0)

            if self.user_id != None and self.user_id != 0:
                self.serializer.get_user_id().set_len(len(self.user_id))
                self.serializer.get_user_id().set_value(self.user_id)
            else:
                self.serializer.get_user_id().set_len(0)

            if self.nonce != None:
                self.serializer.set_nonce_length(len(self.nonce))  # nonceは8バイト固定
                self.serializer.set_nonce(self.nonce)
            else:
                self.serializer.set_nonce_length(0)

            if self.asset_file_size != None and self.asset_file_size != 0:
                self.serializer.set_asset_file_size(self.asset_file_size)
            else:
                self.serializer.set_asset_file_size(0)

            if self.asset_file_digest != None and len(self.asset_file_digest) != 0:
                self.serializer.get_asset_file_digest().set_len(len(self.asset_file_digest))
                self.serializer.get_asset_file_digest().set_value(self.asset_file_digest)
            else:
                self.serializer.get_asset_file_digest().set_len(0)

            if self.asset_body_size != None and self.asset_body_size != 0:
                if type(self.asset_body) is str:
                    u_byte = self.asset_body.encode()
                    self.serializer.set_body(u_byte)
                    self.serializer.set_body_size(len(u_byte))
                elif type(self.asset_body) is bytes:
                    self.serializer.set_body(self.asset_body)
                    self.serializer.set_body_size(len(self.asset_body))
            else:
                self.serializer.set_body_size(0)


            return self.serializer.get_packet()

        else:
            self.serializer.inited()
            if self.asset_id != None and self.asset_id != 0:
                u_byte = self.asset_id
                self.serializer.get_asset_id().set_len(len(u_byte))
                self.serializer.get_asset_id().set_value(u_byte)
            else:
               self.serializer.get_asset_id().set_len(0)

            if self.user_id != None and self.user_id != 0:
                u_byte = self.user_id
                self.serializer.get_user_id().set_len(len(u_byte))
                self.serializer.get_user_id().set_value(u_byte)

            else:
                self.serializer.get_user_id().set_len(0)

            if self.nonce != None and self.nonce !=0:
                self.serializer.set_nonce_length(len(self.nonce))  # nonceは8バイト固定
                self.serializer.set_nonce(self.nonce)

            else:
                self.serializer.set_nonce_length(0)

            if self.asset_file_size != None and self.asset_file_size != 0:
                self.serializer.set_asset_file_size(self.asset_file_size)
            else:
                self.serializer.set_asset_file_size(0)

            if self.asset_file_digest != None:
                u_byte = self.asset_file_digest
                self.serializer.get_asset_file_digest().set_len(len(u_byte))
                self.serializer.get_asset_file_digest().set_value(u_byte)

            else:
                self.serializer.get_asset_file_digest().set_len(0)

            if self.asset_body_size != None and self.asset_body_size != 0:
                if type(self.asset_body) is str:
                    u_byte = self.asset_body.encode()
                    self.serializer.set_body(u_byte)
                    self.serializer.set_body_size(len(u_byte))
                elif type(self.asset_body) is bytes:
                    self.serializer.set_body(self.asset_body)
                    self.serializer.set_body_size(len(self.asset_body))

            else:
                self.serializer.set_body_size(0)

            return self.serializer.get_packet()

    def deserialize(self, data):
        self.serializer.inited()
        try:
            LIBC.parse_Asset(data, byref(self.serializer))

            if self.serializer.get_asset_id().get_len()>0:
                self.asset_id = self.serializer.get_asset_id().get_value()

            if self.serializer.get_user_id().get_len()>0:
                self.user_id = self.serializer.get_user_id().get_value()

            if self.serializer.get_nonce_length()>0:
                self.nonce = self.serializer.get_nonce()

            self.asset_file_size = self.serializer.get_asset_file_size()
            if self.serializer.get_asset_file_digest().get_len() != 0:

                self.asset_file_digest = self.serializer.get_asset_file_digest().get_value()

            self.asset_body_size = self.serializer.get_body_size()
            if self.asset_body_size > 0:
                self.asset_body = self.serializer.get_body()
            else:
                self.asset_body = bytearray()
            self.asset_in_storage = None
            LIBC.free_Asset(byref(self.serializer))
        except:
            #print("Asset")
            traceback.print_exc()
            return False
        return True


class BBcCrossRef:
    def __init__(self, asset_group_id=None, transaction_id=None):
        self.asset_group_id = asset_group_id
        self.transaction_id = transaction_id

        self.serializer = Cross_Ref(LIBC)

    def serialize(self):
        if self.asset_group_id != None and self.asset_group_id != 0:
            u_byte = self.asset_group_id
            self.serializer.get_asset_group_id().set_len(len(u_byte))
            self.serializer.get_asset_group_id().set_value(u_byte)
        else:
            self.serializer.get_asset_group_id().set_len(0)

        if self.transaction_id != None and self.transaction_id != 0:
            u_byte = self.transaction_id
            self.serializer.get_transaction_id().set_len(len(u_byte))
            self.serializer.get_transaction_id().set_value(u_byte)
        else:
            self.serializer.get_transaction_id().set_len(0)

        return self.serializer.get_packet()

    def deserialize(self, data):
        self.serializer.inited()

        try:
            LIBC.parse_Cross_Ref(data, byref(self.serializer))
            if self.serializer.get_asset_group_id().get_len()!=0:
                self.asset_group_id = self.serializer.get_asset_group_id().get_value()
            else:
                self.asset_group_id = None

            if self.serializer.get_transaction_id().get_len() != 0:
                self.transaction_id = self.serializer.get_transaction_id().get_value()
            else:
                self.transaction_id = None

            LIBC.free_Cross_Ref(byref(self.serializer))
        except:
            return False
        return True


class ServiceMessageType:
    REQUEST_SETUP_DOMAIN = 0
    RESPONSE_SETUP_DOMAIN = 1
    REQUEST_GET_PEERLIST = 2
    RESPONSE_GET_PEERLIST = 3
    REQUEST_SET_STATIC_NODE = 4
    RESPONSE_SET_STATIC_NODE = 5
    REQUEST_SETUP_ASSET_GROUP = 6
    RESPONSE_SETUP_ASSET_GROUP = 7
    REQUEST_GET_CONFIG = 8
    RESPONSE_GET_CONFIG = 9
    REQUEST_MANIP_LEDGER_SUBSYS = 10
    RESPONSE_MANIP_LEDGER_SUBSYS = 11
    DOMAIN_PING = 12
    REQUEST_GET_DOMAINLIST = 13
    RESPONSE_GET_DOMAINLIST = 14

    REGISTER = 32
    UNREGISTER = 33
    MESSAGE = 34

    REQUEST_GATHER_SIGNATURE = 35
    RESPONSE_GATHER_SIGNATURE = 36
    REQUEST_SIGNATURE = 37
    RESPONSE_SIGNATURE = 38
    REQUEST_INSERT = 39
    RESPONSE_INSERT = 40

    REQUEST_SEARCH_ASSET = 66
    RESPONSE_SEARCH_ASSET = 67
    REQUEST_SEARCH_TRANSACTION = 68
    RESPONSE_SEARCH_TRANSACTION = 69
    REQUEST_CROSS_REF = 70
    RESPONSE_CROSS_REF = 71

    REQUEST_REGISTER_HASH_IN_SUBSYS = 128
    RESPONSE_REGISTER_HASH_IN_SUBSYS = 129
    REQUEST_VERIFY_HASH_IN_SUBSYS = 130
    RESPONSE_VERIFY_HASH_IN_SUBSYS = 131


def is_less_than(val_a, val_b):
    """
    return True if val_a is less than val_b (evaluate as integer)
    :param val_a:
    :param val_b:
    :return:
    """
    size = len(val_a)
    if size != len(val_b):
        return False
    for i in reversed(range(size)):
        if val_a[i] < val_b[i]:
            return True
        elif val_a[i] > val_b[i]:
            return False
    return False


class NodeInfo:
    """
    node information entry (socket info)
    """
    def __init__(self, node_id=domain_global_0, ipv4=None, ipv6=None, port=None):
        self.node_id = node_id
        if ipv4 is None or len(ipv4) == 0:
            self.ipv4 = "0.0.0.0"
        else:
            if isinstance(ipv4, bytes):
                self.ipv4 = ipv4.decode()
            else:
                self.ipv4 = ipv4
        if ipv6 is None or len(ipv6) == 0:
            self.ipv6 = "::"
        else:
            if isinstance(ipv6, bytes):
                self.ipv6 = ipv6.decode()
            else:
                self.ipv6 = ipv6
        self.port = port
        self.created_at = self.updated_at = time.time()
        self.is_alive = False
        self.disconnect_at = 0

    def __lt__(self, other):
        if self.is_alive and other.is_alive:
            return is_less_than(self.node_id, other.node_id)
        elif self.is_alive and not other.is_alive:
            return True
        elif not self.is_alive and other.is_alive:
            return False
        else:
            return is_less_than(self.node_id, other.node_id)

    def __len__(self):
        return len(self.node_id)

    def touch(self):
        self.updated_at = time.time()
        self.is_alive = True

    def detect_disconnect(self):
        self.disconnect_at = time.time()
        self.is_alive = False

    def update(self, ipv4=None, ipv6=None, port=None):
        if ipv4 is not None:
            self.ipv4 = ipv4
        if ipv6 is not None:
            self.ipv6 = ipv6
        if port is not None:
            self.port = port
        self.updated_at = time.time()

    def get_nodeinfo(self):
        ipv4 = socket.inet_pton(socket.AF_INET, self.ipv4)
        ipv6 = socket.inet_pton(socket.AF_INET6, self.ipv6)
        return self.node_id, ipv4, ipv6, socket.htons(self.port).to_bytes(2, 'little')

    def recover_nodeinfo(self, node_id, ipv4, ipv6, port):
        self.node_id = node_id
        self.ipv4 = socket.inet_ntop(socket.AF_INET, ipv4)
        self.ipv6 = socket.inet_ntop(socket.AF_INET6, ipv6)
        self.port = socket.ntohs(int.from_bytes(port, 'little'))
        self.touch()


class StorageType:
    NONE = 0
    FILESYSTEM = 1
    #HTTP_PUT = 2
    #HTTP_POST = 3

