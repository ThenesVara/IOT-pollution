from network import Bluetooth
import pycom
import time

BLE_Name = "OnOff Server 18"

def blink_led(n):
    for x in range(n):
        pycom.rgbled(0xffff00) # yellow on
        time.sleep(0.3)
        pycom.rgbled(0x000000) # off
        time.sleep(0.3)

def server_cb(new_state, event, recv_op):
    print("SERVER | State: ", new_state)

    # Turn on LED on board based on State
    if new_state == True:
        pycom.rgbled(0x007f00) # green
    else:
        pycom.rgbled(0x7f0000) # red

def prov_callback(event, oob_pass):
    if(event == BLE_Mesh.PROV_REGISTER_EVT or event == BLE_Mesh.PROV_RESET_EVT):
        # Yellow if not Provision yet or Reseted
        pycom.rgbled(0x555500)
    if(event == BLE_Mesh.PROV_COMPLETE_EVT):
        # Green if Provisioned
        pycom.rgbled(0x007f00)
    if(event == BLE_Mesh.PROV_OUTPUT_OOB_REQ_EVT):
        print("Privisioning blink LED num:", oob_pass)
        blink_led(oob_pass)

# BLE Mesh module
BLE_Mesh = Bluetooth.BLE_Mesh

# Turn off the heartbeat behavior of the LED
pycom.heartbeat(False)

# Need to turn ON Bluetooth before using BLE Mesh
bluetooth = Bluetooth()

# Create a Primary Element with GATT Proxy feature and add a Server model to the Element
element = BLE_Mesh.create_element(primary=True, feature=BLE_Mesh.GATT_PROXY)
model_server = element.add_model(BLE_Mesh.GEN_ONOFF, BLE_Mesh.SERVER, callback=server_cb)

# Initialize BLE_Mesh
BLE_Mesh.init(BLE_Name, auth=BLE_Mesh.OOB_OUTPUT, callback=prov_callback)

# Turn on Provisioning Advertisement
BLE_Mesh.set_node_prov(BLE_Mesh.PROV_ADV|BLE_Mesh.PROV_GATT)

print("\nBLE Mesh started")
print(BLE_Name, "waits to be provisioned\n")

"""
# After this node was provisioned
# Current state can be read using
model_server.get_state()
"""
