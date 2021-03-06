# -*- coding: utf-8 -*-
import pytest

import binascii
import sys
sys.path.extend(["../"])
from bbc1.common.bbclib import BBcTransaction, BBcEvent, BBcReference, BBcAsset, BBcCrossRef, KeyPair, KeyType
from bbc1.common import bbclib

user_id = bbclib.get_new_id("user_id_test1")
user_id2 = bbclib.get_new_id("user_id_test2")
#domain_id = bbclib.get_new_id("testdomain")
asset_group_id = bbclib.get_new_id("asset_group_1")
transaction1_id = bbclib.get_new_id("transaction_1")
transaction2_id = bbclib.get_new_id("transaction_2")
keypair1 = KeyPair()
keypair1.generate()
keypair2 = KeyPair()
keypair2.generate()

transaction1 = None
asset1 = None
asset2 = None
event1 = None
event2 = None
transaction2 = None
asset_content = b'abcdefg'

print("\n")
print("private_key:", binascii.b2a_hex(keypair1.private_key))
print("private_key(pem):\n", keypair1.get_private_key_in_pem().decode())
print("public_key:", binascii.b2a_hex(keypair1.public_key))


class TestBBcLib(object):

    def test_00_keypair(self):
        print("-----", sys._getframe().f_code.co_name, "-----")
        global keypair1
        kp = KeyPair(pubkey=keypair1.public_key)
        assert kp.public_key_object

    def test_01_asset(self):
        print("-----", sys._getframe().f_code.co_name, "-----")
        global asset1, asset2
        asset1 = BBcAsset()
        asset1.add(asset_body=b'12345678', user_id=user_id)
        asset2 = BBcAsset()
        asset2.add(asset_file=asset_content, user_id=user_id)

        # --- for checking serialization function ---
        digest = asset1.digest()
        dat = asset1.serialize()
        print("Digest:", binascii.b2a_hex(digest))
        print("Serialized data:", binascii.b2a_hex(dat))
        asset_tmp = BBcAsset()
        asset_tmp.deserialize(dat)
        print("body_len:", asset_tmp.asset_body_size)
        if asset_tmp.asset_body_size > 0:
            print("body:", binascii.b2a_hex(asset_tmp.asset_body))
        print("digest:", binascii.b2a_hex(asset_tmp.asset_id))

    def test_02_event(self):
        print("-----", sys._getframe().f_code.co_name, "-----")
        print("asset_group_id:", binascii.b2a_hex(asset_group_id))
        global event1, event2
        event1 = BBcEvent(asset_group_id=asset_group_id)
        event1.add(asset=asset1, mandatory_approver=user_id)
        event2 = BBcEvent(asset_group_id=asset_group_id)
        event2.add(asset=asset2, mandatory_approver=user_id)

        # --- for checking serialization function ---
        dat = event1.serialize()
        print("Serialized data:", binascii.b2a_hex(dat))
        event_tmp = BBcEvent()
        event_tmp.deserialize(dat)
        print("mandatory_approvers:", [binascii.b2a_hex(d) for d in event_tmp.mandatory_approvers])
        print("asset_id:", binascii.b2a_hex(event_tmp.asset.asset_id))

    def test_03_transaction_1(self):
        print("-----", sys._getframe().f_code.co_name, "-----")
        global transaction1
        transaction1 = BBcTransaction()
        transaction1.add(event=[event1, event2])
        dummy_cross_ref1 = BBcCrossRef(asset_group_id=asset_group_id, transaction_id=transaction1_id)
        transaction1.add(cross_ref=dummy_cross_ref1)
        dummy_cross_ref2 = BBcCrossRef(asset_group_id=asset_group_id, transaction_id=transaction2_id)
        transaction1.add(cross_ref=dummy_cross_ref2)

        sig = transaction1.sign(key_type=KeyType.ECDSA_SECP256k1_XY,
                                private_key=keypair1.private_key,
                                public_key=keypair1.public_key)
        if sig is None:
            print(bbclib.error_text)
            assert sig
        transaction1.add_signature(signature=sig)

        # --- for checking serialization function ---
        digest = transaction1.digest()
        dat = transaction1.serialize()
        print("Digest:", binascii.b2a_hex(digest))
        print("Serialized data:", binascii.b2a_hex(dat))

        transaction_tmp = BBcTransaction()
        transaction_tmp.deserialize(dat)
        transaction1 = transaction_tmp
        #transaction1.events[1].asset.add(asset_file=asset_content)
        print("transaction_id:", binascii.b2a_hex(transaction1.transaction_id))
        print("transaction_id (recalc2):", binascii.b2a_hex(transaction1.digest()))
        asset_tmp = transaction1.events[0].asset
        print("asset_id1:", binascii.b2a_hex(asset_tmp.asset_id))
        asset_tmp = transaction1.events[1].asset
        print("asset_id2:", binascii.b2a_hex(asset_tmp.asset_id))
        print(" --> asset_file_size:", asset_tmp.asset_file_size)
        print(" --> asset_file_digest:", binascii.b2a_hex(asset_tmp.asset_file_digest))
        ret = asset_tmp.recover_asset_file(asset_content)
        assert ret
        print(" --> asset_file (after recover):", asset_tmp.asset_file)

    def test_04_transaction2_with_reference(self):
        print("-----", sys._getframe().f_code.co_name, "-----")
        global transaction2, event3, asset3
        asset3 = BBcAsset()
        asset3.add(asset_body=b'bbbbbbb', user_id=user_id)
        event3 = BBcEvent(asset_group_id=asset_group_id)
        event3.add(asset=asset3, option_approver_num_numerator=1, option_approver_num_denominator=2)
        event3.add(option_approver=user_id)
        event3.add(option_approver=user_id2)

        transaction2 = BBcTransaction()
        transaction2.add(event=event3)
        reference2 = BBcReference(asset_group_id=asset_group_id,
                                  transaction=transaction2, ref_transaction=transaction1, event_index_in_ref=0)
        transaction2.add(reference=reference2)
        dummy_cross_ref3 = BBcCrossRef(transaction_id=transaction1_id, asset_group_id=asset_group_id)
        dummy_cross_ref4 = BBcCrossRef(transaction_id=transaction2_id, asset_group_id=asset_group_id)
        transaction2.add(cross_ref=[dummy_cross_ref3, dummy_cross_ref4])

        sig = transaction2.sign(key_type=KeyType.ECDSA_SECP256k1_XY,
                                private_key=keypair1.private_key,
                                public_key=keypair1.public_key)
        if sig is None:
            print(bbclib.error_text)
            assert sig
        reference2.add_signature(user_id=user_id, signature=sig)

        transaction2.dump()

    def test_05_transaction3_with_reference(self):
        print("-----", sys._getframe().f_code.co_name, "-----")
        asset1 = BBcAsset()
        asset1.add(user_id=user_id, asset_body=b'ccccc')
        event = BBcEvent(asset_group_id=asset_group_id)
        event.add(asset=asset1, option_approver_num_numerator=1, option_approver_num_denominator=2)
        event.add(option_approver=user_id)
        event.add(option_approver=user_id2)

        global transaction1
        transaction1 = BBcTransaction()
        transaction1.add(event=event)
        reference = BBcReference(asset_group_id=asset_group_id,
                                 transaction=transaction1, ref_transaction=transaction2, event_index_in_ref=0)
        transaction1.add(reference=reference)
        dummy_cross_ref = BBcCrossRef(transaction_id=transaction1_id, asset_group_id=asset_group_id)
        transaction2.add(cross_ref=[dummy_cross_ref])

        sig = transaction1.sign(key_type=KeyType.ECDSA_SECP256k1_XY,
                                private_key=keypair2.private_key,
                                public_key=keypair2.public_key)
        if sig is None:
            print(bbclib.error_text)
            assert sig
        reference.add_signature(user_id=user_id2, signature=sig)
        sig = transaction1.sign(key_type=KeyType.ECDSA_SECP256k1_XY,
                                private_key=keypair1.private_key,
                                public_key=keypair1.public_key)
        if sig is None:
            print(bbclib.error_text)
            assert sig
        reference.add_signature(user_id=user_id, signature=sig)

        transaction1.dump()

    def test_06_proof(self):
        print("-----", sys._getframe().f_code.co_name, "-----")

        digest = transaction1.digest()
        ret = transaction1.signatures[0].verify(digest)
        print("Proof result:", ret)
        if not ret:
            print(bbclib.error_text)
            assert ret

    def test_07_proof(self):
        print("-----", sys._getframe().f_code.co_name, "-----")
        transaction1.timestamp = transaction1.timestamp + 1
        digest = transaction1.digest()
        ret = transaction1.signatures[0].verify(digest)
        assert not ret
