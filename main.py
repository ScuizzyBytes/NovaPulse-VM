from opcodes import OpCodes
from vm import VirtualMachine


def main() -> None:
    
    bytescode = [
        (OpCodes.PUSH, 23),
        (OpCodes.PUSH, 12),
        (OpCodes.ADD, None),
        (OpCodes.PRINT, None),
        (OpCodes.HALT, None)
    ]
    
    print("Starting VirtualMachine...")
    machine = VirtualMachine(bytescode)
    machine.run()
    print("Vipolneno")

main()