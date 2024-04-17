import time
import wmi

from communication import CommunicationModule

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


#cm = CommunicationModule()
start = time.monotonic_ns()
checkConnected("VID_2E8A&PID_000A")

end = time.monotonic_ns()
diff = end-start
print(start)
print(end)

print(str((end-start)/1e6) + " milisegundos")



