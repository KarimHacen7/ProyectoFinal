import wmi
from winusbcdc import ComPort
from time import sleep

def checkConnected(device_ID_check: str):
        # Connect to the WMI service
        c = wmi.WMI()
        # Define the WQL query to retrieve USB devices
        query = "SELECT DeviceID FROM Win32_USBHub"
        # Execute the query
        usb_devices_DeviceIDs = c.query(query)

        for device in usb_devices_DeviceIDs:
            if device.ole_object.DeviceID.find(device_ID_check) >= 0:
                return True
            else:
                continue
        return False

def sendSamplingCommand(command: str):
    keep_reading_usb = True
    if checkConnected("VID_2E8A&PID_000A"): 
        port_handler = ComPort(vid=0x2E8A, pid=0x000A)
        port_handler.open()
    else:
        return -1, bytearray()
    
    return_bytearray = bytearray()
    
    if port_handler.is_open:
        # Send command
        port_handler.write(command.encode(encoding="ascii"))
        sleep(0.01)
        # And check if response acknowledged
        usb_input_buffer = port_handler.read()
        if usb_input_buffer.startswith(b'#ACK;'):

            usb_input_buffer = usb_input_buffer.removeprefix(b'#ACK;')
            # If we got an immediate response...
            if usb_input_buffer.endswith(b'#END;'):
                usb_input_buffer = usb_input_buffer.removesuffix(b'#END;')
                return_bytearray.extend(usb_input_buffer)
                port_handler.close()
                return 0, return_bytearray
            
            sleep(0.1)
            while keep_reading_usb:
                if checkConnected("VID_2E8A&PID_000A"):
                    usb_input_buffer = port_handler.read()
                else:
                    return -1, bytearray()
                if usb_input_buffer.endswith(b'#HARDRESET;'):
                    port_handler.close()
                    return -2, bytearray()
                elif usb_input_buffer is None:
                    continue
                elif usb_input_buffer.endswith(b'#TRIGTIMEOUT;'):
                    port_handler.close()
                    return -3, bytearray()
                elif usb_input_buffer.endswith(b'#END;'):
                    
                    port_handler.close()
                    usb_input_buffer.removesuffix(b'#END;')
                    return 0, return_bytearray
                else:
                    print(usb_input_buffer)
                    return_bytearray.extend(usb_input_buffer)
                    keep_reading_usb = True
    else:
        return -1, bytearray()


print(sendSamplingCommand("#D31810020;"))
