from tkinter import *
from testbackend import SmartHome, SmartPlug, SmartDoor
#4:1
mainWin = Tk()  #5:0
smarthome = SmartHome() #4:2

def setupHome():
    smartplug1 = SmartPlug()
    smartplug2 = SmartPlug()
    smartdoor1 = SmartDoor()
    smartdoor2 = SmartDoor()
    smartdoor3 = SmartDoor()

    smarthome.addDevice(smartplug1)
    smarthome.addDevice(smartplug2)
    smarthome.addDevice(smartdoor1)
    smarthome.addDevice(smartdoor2)
    smarthome.addDevice(smartdoor3)
    #4:3

def SmartHome():
    mainWin.title("SmartHome")
    mainWin.geometry("500x350")
    title_label = Label(mainWin, text="Smart Home", font=("Arial", 26, "bold"))
    title_label.grid(row=0, columnspan=2, pady=10, padx=10, sticky="n")
    mainWin.resizable(False, False)
    mainWin.columnconfigure(index=0, weight=1)
    mainWin.columnconfigure(index=1, weight=1)
#5:4

    listDevices()
    mainWin.mainloop()

def listDevices():
    numberOfDevices = len(smarthome.getDevices())

    for deviceIndex in range(numberOfDevices):
        devices = smarthome.getDeviceAt(deviceIndex)

        deviceTxt = Text(mainWin, height=2, width=50)
        deviceTxt.insert("1.0", str(devices))
        #deviceTxt.config(state='disabled')
        deviceTxt.grid(row=deviceIndex+2, column=0, padx=10, pady=5)

        def toggleCmd(i=deviceIndex, text=deviceTxt):
            toggle(i, text)

        def turnOnAllCmd():
            smarthome.turnOnAll()
            updateDeviceStatus()

        def turnOffAllCmd():
            smarthome.turnOffAll()
            updateDeviceStatus()


        togBtn = Button(mainWin, text="Toggle this", command=toggleCmd)
        togBtn.grid(row=deviceIndex+2, column=1, padx=10, pady=5)

    OnBtn = Button(mainWin, text="Turn On All.", command=turnOnAllCmd)
    OnBtn.grid(row=0, column=0, padx=15, pady=10, sticky="w")

    OffBtn = Button(mainWin, text="Turn Off All", command=turnOffAllCmd)
    OffBtn.grid(row=1, column=0, padx=15, pady=10, sticky="w")
def toggle(deviceIndex, deviceTxt):
    smarthome.toggleSwitch(deviceIndex)
    devices = smarthome.getDeviceAt(deviceIndex)
    deviceTxt.config(state='normal')
    deviceTxt.delete('1.0', END)
    deviceTxt.insert("1.0", str(devices))
    deviceTxt.config(state='disabled')

def updateDeviceStatus():
    for i in range(len(smarthome.getDevices())):
        device = smarthome.getDeviceAt(i)
        devices = mainWin.grid_slaves(row=i+2, column=0)
        devices[0].config(state='normal')
        devices[0].delete('1.0', END)
        devices[0].insert("1.0", device)
        devices[0].config(state=DISABLED)


def turnAllOn(deviceIndex, deviceTxt):
    pass


def turnAllOff():
    pass

def main():
    setupHome() #4:4
    SmartHome()

#4:5
main()