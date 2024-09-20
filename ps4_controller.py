import evdev
from evdev import InputDevice, categorize, ecodes

# Find your controller
devices = [InputDevice(path) for path in evdev.list_devices()]
controller = None

for device in devices:
    if 'Wireless Controller' in device.name:  # PS4 controller name
        controller = device
        break

if controller:
    print(f"Connected to {controller.name} at {controller.path}")
    # Start reading input events
    for event in controller.read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            print(f"Button {key_event.keycode} {'pressed' if key_event.keystate == key_event.key_down else 'released'}")
        elif event.type == ecodes.EV_ABS:
            axis_event = categorize(event)
            print(f"Axis {axis_event.event.code} value: {axis_event.event.value}")
else:
    print("PS4 controller not found.")
