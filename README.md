# NEC IR Remote for MicroPython

A simple MicroPython module to decode NEC protocol IR signals using Raspberry Pi Pico or any MicroPython-compatible board.

## 📦 Features

- Decode 32-bit NEC IR signals
- Validate address and command integrity
- Built-in button mapping for popular remotes
- Easy to integrate into MicroPython projects

## 📁 File Structure

```
nec_ir_remote/
├── nec_ir_remote.py
└── README.md
```

## 📸 Hardware Required

- Raspberry Pi Pico (or similar MicroPython board)
- IR receiver module (e.g., VS1838B)
- NEC-compatible IR remote

## 🔧 Pin Wiring

| IR Receiver Pin | Raspberry Pi Pico |
|-----------------|-------------------|
| Signal (OUT)    | GPIO 15           |
| VCC             | 3.3V              |
| GND             | GND               |

## 🚀 Getting Started

1. Flash your board with MicroPython.
2. Upload `nec_ir_remote.py` to the board.
3. Use the module in your script:

```python
from nec_ir_remote import NECIRRemote

remote = NECIRRemote(pin_num=15)

while True:
    remote.listen()
```

## 🎮 Supported Button Mappings

| Button       | Hex Code |
|--------------|----------|
| POWER        | 0x45     |
| MENU         | 0x46     |
| TEST         | 0x47     |
| LEFT         | 0x44     |
| PLAY/PAUSE   | 0x40     |
| RIGHT        | 0x43     |
| DOWN         | 0x07     |
| UP           | 0x15     |
| EQ           | 0x09     |
| 0            | 0x16     |
| 1–9          | 0x0C–0x4A|

Unknown button codes will be printed in hex for your mapping.

## 📝 License

MIT License

---

Happy Hacking! 🔧📡