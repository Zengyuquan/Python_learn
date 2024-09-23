class Phone:
    IMEi = None
    producer = "HM1"

    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("2022新功能：5g通话")

class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoveControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")

class MyPhone(Phone, NFCReader, RemoveControl):
    pass

phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

print(phone.producer)