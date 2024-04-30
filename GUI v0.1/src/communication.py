import wmi
from winusbcdc import ComPort
from time import sleep
from PySide6.QtCore import Signal, QObject
import queue


class CommunicationModule():
    # This function looks for (AT LEAST ONE) a DeviceID (attribute of Win32_USBHub WMI class)
    # Returns a bool, True if found
    def checkConnected(self, device_ID_check: str):
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
'''
    # This function orders a type of sampling
    # Returns a bytearray (truncating control messages) containing the sampled data
    # If an error occured, returns -1. For disconnected or unavailable, -2. For hardreset, -3
    def sendSamplingCommand(self, command: str):
        keep_reading_usb = True
        if self.checkConnected("VID_2E8A&PID_000A"): 
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
                usb_input_buffer = usb_input_buffer.removeFefix(b'#ACK;')
                # If we got an immediate response...
                if usb_input_buffer.endswith(b'#END;'):
                    usb_input_buffer = usb_input_buffer.removesuffix(b'#END;')
                    return_bytearray.extend(usb_input_buffer)
                    port_handler.close()
                    return 0, return_bytearray
                # Else, keep waiting for disconnection (reset), data, or trigger timeout 
                while keep_reading_usb:
                    sleep(0.01)
                    if self.checkConnected("VID_2E8A&PID_000A"):
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
                        return_bytearray.extend(usb_input_buffer)
                        port_handler.close()
                        usb_input_buffer.removesuffix(b'#END;')
                        return 0, return_bytearray
                    else:
                        return_bytearray.extend(usb_input_buffer)
                        keep_reading_usb = True
        else:
            return -1, bytearray()

    # This function configures a reference voltage or trigger timeout  
    # Returns 1 if successful, or -1 if failed
    def sendConfigCommand(self, command: str):
        if self.checkConnected("VID_2E8A&PID_000A"):
            port_handler = ComPort(vid=0x2E8A, pid=0x000A)
            port_handler.open()
        else:
            return -1
        if port_handler.is_open:
            port_handler.write(command.encode(encoding="ascii"))
            sleep(0.02)
            usb_input_buffer = port_handler.read()
            if usb_input_buffer.startswith(b'#ACK;'):
                return 1
            else:
                return -1
        else:
            return -1'''

class SamplingWorker(QObject):
    commandAcknowledged = Signal()
    dataIncoming = Signal(int)
    samplingFinished = Signal(int, bytearray)
    timeoutFinished = Signal(int)
    voltageFinished = Signal(int)
    finished = Signal()
    samplingQueue = queue.Queue()
    timeoutQueue = queue.Queue()
    voltageQueue = queue.Queue()
    
    def __init__(self):
        super().__init__()

    def sample(self):

        temp = self.sendConfigCommand(self.voltageQueue.get(block=True, timeout=None))
        self.voltageFinished.emit(temp)
        if temp == -1:
            self.finished.emit()
            return
        
        temp = self.sendConfigCommand(self.timeoutQueue.get(block=True, timeout=None))
        self.timeoutFinished.emit(temp)
        if temp == -1:
            self.finished.emit()
            return
        
        (ret1, ret2) = self.sendSamplingCommand(self.samplingQueue.get(block=True, timeout=None))
        self.samplingFinished.emit(ret1, ret2)
        self.finished.emit()

    # This function looks for (AT LEAST ONE) a DeviceID (attribute of Win32_USBHub WMI class)
    # Returns a bool, True if found
    def checkConnected(self, device_ID_check: str):
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
    
    # This function configures a reference voltage or trigger timeout  
    # Returns 1 if successful, or -1 if failed
    def sendConfigCommand(self, command: str):
        if self.checkConnected("VID_2E8A&PID_000A"):
            port_handler = ComPort(vid=0x2E8A, pid=0x000A)
            port_handler.open()
        else:
            return -1
        if port_handler.is_open:
            port_handler.write(command.encode(encoding="ascii"))
            sleep(0.02)
            usb_input_buffer = port_handler.read()
            if usb_input_buffer.startswith(b'#ACK;'):
                return 1
            else:
                return -1
        else:
            return -1
    
    # This function orders a type of sampling
    # Returns a bytearray (truncating control messages) containing the sampled data
    # If an error occured, returns -1. For disconnected or unavailable, -2. For hardreset, -3
    def sendSamplingCommand(self, command: str):
        keep_reading_usb = True
        if self.checkConnected("VID_2E8A&PID_000A"): 
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
                self.commandAcknowledged.emit()
                usb_input_buffer = usb_input_buffer.removeprefix(b'#ACK;')
                # If we got an immediate response...
                if usb_input_buffer.endswith(b'#END;'):
                    usb_input_buffer = usb_input_buffer.removesuffix(b'#END;')
                    return_bytearray.extend(usb_input_buffer)
                    port_handler.close()
                    return 0, return_bytearray
                # Else, keep waiting for disconnection (reset), data, or trigger timeout 
                self.dataIncoming.emit(len(usb_input_buffer))
                sleep(0.1)
                while keep_reading_usb:
                    if self.checkConnected("VID_2E8A&PID_000A"):
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
                        return_bytearray.extend(usb_input_buffer)
                        port_handler.close()
                        usb_input_buffer.removesuffix(b'#END;')
                        return 0, return_bytearray
                    else:
                        return_bytearray.extend(usb_input_buffer)
                        keep_reading_usb = True
        else:
            return -1, bytearray()