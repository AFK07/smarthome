class SmartPlug:

    def __init__(self):
        self.switchedOn = False
        self.consumptionRate = 0

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self):
        return self.switchedOn

    def getConsumptionRate(self):
        return self.consumptionRate

    def setConsumptionRate(self, newRate):
        if self.consumptionRate >= 0 and self.consumptionRate <= 150:
            self.consumptionRate = newRate

    def __str__(self):
        return f"Smart Plug: switchedOn={self.switchedOn}, consumptionRate={self.consumptionRate}"

def testSmartPlug():
     smartplug = SmartPlug()
     smartplug.toggleSwitch()
     print(f"switchedOn: {smartplug.getSwitchedOn()}")
     print(f"consumptionRate: {smartplug.getConsumptionRate()}")
     smartplug.setConsumptionRate(60)
     print(f"consumptionRate: {smartplug.getConsumptionRate()}")
     print(smartplug)
     print("\n")

testSmartPlug()

class SmartDoor:
    def __init__(self):
        self.switchedOn = False
        self.locked = True

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self):
        return self.switchedOn

    def getLock(self):
        return self.locked

    def setLock(self):
        self.locked = not self.locked

    def __str__(self):
        return f"SmartDoor: switchedOn = {self.switchedOn}, Locked = {self.locked}"

def testDevice():
    smartdoor = SmartDoor()
    smartdoor.toggleSwitch()
    print(f"SmartDoor: switchOn = {smartdoor.getSwitchedOn()}")
    print(f"SmartDoor: Lock = {smartdoor.getLock()}")
    smartdoor.setLock()
    print(f"SmartDoor: Lock = {smartdoor.getLock()}")
    print(smartdoor)
    print("\n")


testDevice()

class SmartHome:
    def __init__(self):
        self.devices = []

    def getDevices(self):
        return self.devices

    def getDeviceAt(self, index):
        return self.devices[index]

    def addDevice(self, device):
        self.devices.append(device)

    # def getDeviceLength(self):
    #     return len(self.devices)
#new
    def toggleSwitch(self, index):
        device = self.devices[index]
        device.toggleSwitch()

    def turnOnAll(self):
        for device in self.devices:
            if device.switchedOn == False:
                device.switchedOn = True

    def turnOffAll(self):
        for device in self.devices:
            if device.switchedOn == True:
                device.switchedOn = False

    def __str__(self):
        device_str = ""
        for device in self.devices:
            device_str += str(device) + "\n"
        return device_str

def testSmartHome():
    smarthome = SmartHome()
    plug1 = SmartPlug()
    plug2 = SmartPlug()
    smartdoor = SmartDoor()
    plug2.toggleSwitch()
    plug2.setConsumptionRate(45)
    smartdoor.setLock()
    smarthome.addDevice(plug1)
    smarthome.addDevice(plug2)
    smarthome.addDevice(smartdoor)
    print(smarthome)
    smarthome.turnOnAll()
    print(smarthome)




testSmartHome()

# def testSmartPlug():
#      smartdoor = SmartDoor()
#      smartdoor.toggleSwitch()
#      print(f"switchedOn: {smartdoor.getSwitchedOn()}")
# #idk if you need consumption rate of door?
# #     print(f"consumptionRate: {SmartDoor.getConsumptionRate()}")
# #     smartPlug.setConsumptionRate(50)
# #     print(f"consumptionRate (updated): {smartPlug.getConsumptionRate()}")
# #     print(smartPlug)