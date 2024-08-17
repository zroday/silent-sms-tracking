import smpplib
import smpplib.gsm

def send_silent_sms(target_number, message=""):
    client = smpplib.client.Client("localhost", 2775)
    client.set_message_sent_handler(
        lambda pdu: sys.stdout.write('sent {} {}\n'.format(pdu.sequence, pdu.message_id)))
    client.connect()
    client.bind_transmitter(system_id="user", password="password")

    parts, encoding_flag, msg_type_flag = smpplib.gsm.make_parts(message)

    for part in parts:
        pdu = client.send_message(
            source_addr_ton=smpplib.consts.SMPP_TON_ALNUM,
            source_addr_npi=smpplib.consts.SMPP_NPI_UNK,
            source_addr="SilentSMS",
            dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
            dest_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
            destination_addr=target_number,
            short_message=part,
            data_coding=encoding_flag,
            esm_class=msg_type_flag,
            registered_delivery=True,
        )
   
    client.unbind()
    client.disconnect()

# Example usage (can be commented out when used as a module)
# send_silent_sms("+1234567890")
