# from azure.iot.device import IoTHubDeviceClient, Message

# import json

# denemeClient = IoTHubDeviceClient.create_from_connection_string("HostName=tutorial-iot-raspberrypi.azure-devices.net;DeviceId=myPi;SharedAccessKey=qrnNfkAz+haJrrz+EmBSGMZS5qGAtBVW8d7BM1otY3g=")

# message = Message("Selam")

# ERROR_MESSAGE = {"type":"error", "data":"connect error"}

# ERROR_MESSAGE = json.dumps(ERROR_MESSAGE)

# denemeClient.send_message(ERROR_MESSAGE)