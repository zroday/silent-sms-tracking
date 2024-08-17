import threading
import time
import pygsm
from send_sms import send_silent_sms
from receive_sms import process_received_sms

def main():
    # Set up the GSM modem
    modem = pygsm.GsmModem(port="/dev/ttyUSB0", baudrate=115200)
    modem.connect()

    # Start a thread for processing received messages
    receive_thread = threading.Thread(target=process_received_sms, args=(modem,))
    receive_thread.start()

    # Main loop for sending Silent SMS and performing triangulation
    while True:
        target_number = "+1234567890"  # Replace with actual target number
        send_silent_sms(target_number)
        time.sleep(60)  # Wait for 60 seconds before next ping

        # Perform triangulation (assuming you have the necessary data)
        # estimated_location = triangulate(tower1, tower2, tower3, dist1, dist2, dist3)
        # print(f"Estimated location: {estimated_location}")

    # Clean up
    receive_thread.join()
    modem.disconnect()

if __name__ == "__main__":
    main()
