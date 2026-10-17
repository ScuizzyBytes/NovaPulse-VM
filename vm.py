from typing import Any, List  # noqa: UP035

from opcodes import OpCodes


class VirtualMachine:
    def __init__(self, bytecode: List[tuple]) -> None:
        self.bytecode: List[tuple] = bytecode
        self.stack: List[Any] = []
        self.ip: int = 0
        
    def run(self) -> None:
        while self.ip < len(self.bytecode):
            opcode, operand = self.bytecode[self.ip]     
            if opcode  == OpCodes.PUSH:
                self.stack.append(operand)
            elif opcode == OpCodes.ADD:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
            elif opcode == OpCodes.PRINT:
                value = self.stack.pop()
                print(f"[VM OUTPUT] {value}")
            elif opcode == OpCodes.HALT:
                break
                
            self.ip += 1
                