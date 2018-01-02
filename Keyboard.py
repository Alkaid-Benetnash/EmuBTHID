import subprocess
import keymap
import dbus
import dbus.service
import shlex
from gi.repository import GObject
from dbus.mainloop.glib import DBusGMainLoop
from bluetooth import *

DBusGMainLoop(set_as_default=True)
from Bluetooth import *


class Keyboard:
    def __init__(self):
        self.state = bytearray([
            0xA1,
            0x01,  # Report ID
            0x00,  # Modifier keys
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00
        ])
        print("Calling libinput")
        try:
            self.libinput = subprocess.Popen(shlex.split("stdbuf -oL libinput debug-events --show-keycode"), stdout=subprocess.PIPE, bufsize=0, universal_newlines=True)
        except Exception as ex:
            sys.exit("Can't listen to libinput")
        self.parser = {"KEYBOARD_KEY": self.parser_key}
        print("Keyboard initialized")

    def parser_key(self, line_str_list):
        """
        event0   KEYBOARD_KEY      +2.82s	KEY_F (33) release/pressed
        0        1                 2        3     4    5
        :param line_str_list:
        :return:
        """
        key_sym = line_str_list[3]
        action = line_str_list[5]
        hid_keycode = keymap.keytable.get(key_sym, None)
        if hid_keycode is None:
            hid_modkeys = keymap.modkeys.get(key_sym, None)
            if (hid_modkeys is not None):
                if action == "pressed":
                    self.state[3] &= hid_modkeys
                elif action == "released":
                    self.state[3] &= ~hid_modkeys
                else:
                    raise NotImplemented("Unknown action " + action)
            else:
                raise NotImplementedError("Unknown key " + key_sym)
        else:
            for i in range(4, 10):
                if action == "released" and self.state[i] == hid_keycode:
                    self.state[i] = 0x00
                    break
                elif action == "pressed" and self.state[i] == 0x00:
                    self.state[i] = hid_keycode
                    break

    def event_loop(self, send_call_back):
        for line in self.libinput.stdout:
            line_str_list = line.split()
            event_type = line_str_list[1]
            handler = self.parser.get(event_type, None)
            print("READ: " + line)
            if handler is not None:
                handler(line_str_list)
                send_call_back(bytes(self.state))


class BTKeyboardProfile(dbus.service.Object):
    def __init__(self, bus, path, input_dev):
        super(BTKeyboardProfile, self).__init__(bus, path)
        self.input_dev = input_dev
        self.fd = -1

    @dbus.service.method("org.bluez.Profile1", in_signature="", out_signature="")
    def Release(self):
        raise NotImplementedError("Release")

    @dbus.service.method("org.bluez.Profile1", in_signature="", out_signature="")
    def Cancel(self):
        raise NotImplementedError("Cancel")

    @dbus.service.method("org.bluez.Profile1", in_signature="oha{sv}", out_signature="")
    def NewConnection(self, path, fd, properties):
        import pdb
        pdb.set_trace()
        self.fd = fd.take()
        print("New Connection from (%s, %d)" % (path, self.fd))
        for k, v in properties.items():
            if k == "Version" or k == "Features":
                print("    %s = 0x%04x " % (k, v))
            else:
                print("    %s = %s" % (k, v))

    @dbus.service.method("org.bluez.Profile1",
                         in_signature="o", out_signature="")
    def RequestDisconnection(self, path):
        print("RequestDisconnection(%s)" % (path))

        if (self.fd > 0):
            os.close(self.fd)
            self.fd = -1

def error_handler(e):
    mainloop.quit()
    raise RuntimeError(str(e))


if __name__ == "__main__":
    P_CTRL = 0x0011
    P_INTR = 0x0013
    HOST = 0
    PORT = 1
    SELFMAC = "7C:67:A2:94:6B:B8"
    DBusGMainLoop(set_as_default=True)
    profile_path = "/org/bluez/btk_profile"
    bus = dbus.SystemBus()
    bluez_obj = bus.get_object("org.bluez", "/org/bluez")
    manager = dbus.Interface(bluez_obj, "org.bluez.ProfileManager1")
    kbd = Keyboard()
    # kbd.event_loop(print)
    BTKP = BTKeyboardProfile(bus, profile_path, kbd)
    service_record = open("sdp_record_kbd.xml").read()
    opts = {
        "ServiceRecord": service_record,
        "Name": "BTKeyboardProfile",
        "RequireAuthentication" : False,
        "RequireAuthorization" : False,
        "Service" : "MY BTKBD",
        "Role" : "server"
    }
    soccontrol = BluetoothSocket(L2CAP)
    sockinter = BluetoothSocket(L2CAP)
    soccontrol.bind((SELFMAC, P_CTRL))
    sockinter.bind((SELFMAC, P_INTR))
    manager.RegisterProfile(profile_path, "00001124-0000-1000-8000-00805f9b34fb", opts)
    print("Registered")
    soccontrol.listen(1)
    sockinter.listen(1)
    print("waiting for connection")
    ccontrol, cinfo = soccontrol.accept()
    print("Control channel connected to " + cinfo[HOST])
    cinter, cinfo = sockinter.accept()
    print("Interrupt channel connected to " + cinfo[HOST])
    kbd.event_loop(cinter.send)
    mainloop = GObject.MainLoop()
    mainloop.run()
