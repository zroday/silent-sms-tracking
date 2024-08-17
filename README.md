# Silent SMS Tracking System

This project implements a silent SMS tracking system that sends silent SMS messages to a target phone number, receives any SMS responses, and performs triangulation to estimate the target's location. The project is organized into several Python modules, each responsible for a specific aspect of the system.

pip install pygsm smpplib geopy

## Project Structure

```plaintext
silent-sms-tracking/
├── README.md
├── send_sms.py
├── receive_sms.py
├── triangulation.py
└── main.py



send_sms.py
This module contains the function send_silent_sms which is responsible for sending silent SMS messages to a specified target number.

receive_sms.py
This module contains functions for receiving SMS messages using a GSM modem and processing the received data.

triangulation.py
This module performs basic triangulation using distances from three cell towers to estimate the location of the target.

main.py
The main script that ties everything together. It handles sending silent SMS messages, receiving responses, and performing triangulation.

Usage
Sending Silent SMS:

Use the send_silent_sms(target_number) function from send_sms.py to send a silent SMS to the target phone number.
Receiving SMS Messages:

The process_received_sms(modem) function from receive_sms.py is used to process any incoming SMS messages via a GSM modem.
Triangulation:

The triangulate function in triangulation.py is used to estimate the location of the target based on distances from three cell towers.
Running the System:

Run the main.py script to start the system. It will continuously send silent SMS messages and attempt to triangulate the target's location based on the received data.
