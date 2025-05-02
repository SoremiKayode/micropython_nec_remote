from machine import Pin
import time

class NECIRRemote:
    def __init__(self, pin_num):
        self.pin = Pin(pin_num, Pin.IN)
        self.button_map = {
            0x45: "POWER",
            0x46: "MENU",
            0x47: "TEST",
            0x44: "LEFT",
            0x40: "PLAY/PAUSE",
            0x43: "RIGHT",
            0x07: "DOWN",
            0x15: "UP",
            0x09: "EQ",
            0x16: "0",
            0x0C: "1",
            0x18: "2",
            0x5E: "3",
            0x08: "4",
            0x1C: "5",
            0x5A: "6",
            0x42: "7",
            0x52: "8",
            0x4A: "9"
        }

    def wait_for_signal(self, timeout_ms=5000):
        start = time.ticks_ms()
        while self.pin.value() == 1:
            if time.ticks_diff(time.ticks_ms(), start) > timeout_ms:
                return False
        return True

    def read_nec(self):
        if not self.wait_for_signal():
            return None

        while self.pin.value() == 0:
            pass
        while self.pin.value() == 1:
            pass

        bits = []
        for _ in range(32):
            while self.pin.value() == 0:
                pass
            start = time.ticks_us()
            while self.pin.value() == 1:
                pass
            duration = time.ticks_diff(time.ticks_us(), start)

            bits.append('1' if duration > 1600 else '0')

        value = int(''.join(bits), 2)
        addr = (value >> 24) & 0xFF
        addr_inv = (value >> 16) & 0xFF
        cmd = (value >> 8) & 0xFF
        cmd_inv = value & 0xFF

        if (addr ^ addr_inv) != 0xFF or (cmd ^ cmd_inv) != 0xFF:
            return None
        return cmd

    def listen(self):
        print("Waiting for IR signal...")
        command = self.read_nec()
        if command is None:
            print("Invalid or no signal")
            return

        print(f"Received button command: 0x{command:02X}")
        name = self.button_map.get(command, "Unknown")
        print(f"You pressed: {name}")
        return command