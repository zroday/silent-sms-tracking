import pygsm

def process_received_sms(modem):
    while True:
        sms = modem.next_message()
        if sms is None:
            break
        print(f"Received: {sms}")
        # Process the SMS data here
        process_sms_data(sms)

def process_sms_data(sms):
    # Extract relevant information from the SMS
    # This is where you'd implement your specific processing logic
    pass

# Example usage (can be commented out when used as a module)
# modem = pygsm.GsmModem(port="/dev/ttyUSB0", baudrate=115200)
# modem.connect()
# process_received_sms(modem)
