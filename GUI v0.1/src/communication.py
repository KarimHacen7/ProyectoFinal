import wmi
from winusbcdc import ComPort
from time import sleep

# This function looks for (AT LEAST ONE) a DeviceID (attribute of Win32_USBHub WMI class)
# Returns a bool, True if found
def check_if_connected(device_ID_check: str):
    # Connect to the WMI service
    c = wmi.WMI()
    # Define the WQL query to retrieve USB devices
    query = "SELECT * FROM Win32_USBHub"
    # Execute the query
    usb_devices_DeviceIDs = c.query(query)

    for device in usb_devices_DeviceIDs:
        if device.ole_object.DeviceID.find(device_ID_check) >= 0:
            return True
        else:
            continue
    return False

# This function orders a type of sampling
# Returns a bytearray (truncating control messages) containing the sampled data
# If an error occured, returns -1 for disconnected or unavailable, -2 for hardreset, -3 for triggertimeout
def send_command_and_get_data(command: str):
    keep_reading_usb = True
    if check_if_connected("VID_2E8A&PID_000A"): 
        port_handler = ComPort(vid=0x2E8A, pid=0x000A)
        port_handler.open()
    else:
        return -1
    
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
                return return_bytearray
            # Else, keep waiting for disconnection (reset), data, or trigger timeout 
            while keep_reading_usb:
                sleep(0.01)
                if check_if_connected("VID_2E8A&PID_000A"):
                    usb_input_buffer = port_handler.read()
                else:
                    return -1
                if usb_input_buffer.endswith(b'#HARDRESET;'):
                    port_handler.close()
                    return -2
                elif usb_input_buffer is None:
                    continue
                elif usb_input_buffer.endswith(b'#TRIGTIMEOUT;'):
                    port_handler.close()
                    return -3
                elif usb_input_buffer.endswith(b'#END;'):
                    return_bytearray.extend(usb_input_buffer)
                    port_handler.close()
                    return return_bytearray
                else:
                    return_bytearray.extend(usb_input_buffer)
                    keep_reading_usb = True
    else:
        return -1

# This function configures a reference voltage or trigger timeout  
# Returns 1 if successful, or -1 if failed
def send_config(command: str):
    if check_if_connected("VID_2E8A&PID_000A"):
        port_handler = ComPort(vid=0x2E8A, pid=0x000A)
        port_handler.open()
    else:
        return -1
    if port_handler.is_open:
        port_handler.write(command.encode(encoding="ascii"))
        sleep(0.01)
        usb_input_buffer = port_handler.read()
        if usb_input_buffer.startswith(b'#ACK;'):
            return 1
        else:
            return -1
    else:
        return -1


print(send_command_and_get_data("#D01805001;"))