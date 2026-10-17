<div align="center">

  <h1>⚡ StackByte-VM</h1>
  <p><b>A custom, stack-based Bytecode Virtual Machine and execution engine built from scratch in Python.</b></p>

  <p>
    <a href="https://github.com/YOUR_USERNAME/StackByte-VM">
      <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+" />
    </a>
    <a href="https://github.com/YOUR_USERNAME/StackByte-VM">
      <img src="https://img.shields.io/badge/Architecture-Stack--Based-FF6B6B?style=for-the-badge" alt="Stack-Based" />
    </a>
    <a href="https://github.com/YOUR_USERNAME/StackByte-VM">
      <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License: MIT" />
    </a>
  </p>

</div>

<hr />

<div id="overview">

## 🚀 Overview

**StackByte-VM** is a lightweight, low-level execution engine designed to demonstrate how virtual machines process bytecode using a LIFO data structure, custom instruction pointer (`IP`), and decoupled opcode evaluation loops.

</div>

<div id="features">

## 🛠️ Key Features

<ul>
  <li><b>LIFO Stack Data Architecture</b>: Efficient variable-free runtime state manipulation.</li>
  <li><b>Instruction Pointer Engine</b>: Deterministic linear execution with customizable instruction flow.</li>
  <li><b>Zero External Dependencies</b>: Pure Python implementation leveraging standard libraries only.</li>
  <li><b>Modular 3-Tier Design</b>: Clean separation between system opcodes, core engine state, and execution setup.</li>
</ul>

</div>

<div id="architecture">

## 🏗️ Architecture & Execution Flow

<div align="center">

```
  +-----------------------+
  |    Bytecode Stream    |  -> [ (OpCodes.PUSH, 23), (OpCodes.ADD, None) ]
  +-----------------------+
              |
              v
  +-----------------------+
  |     Fetch & Decode    |  -> Loop through stream using IP counter
  +-----------------------+
              |
              v
  +-----------------------+
  |  Stack Manipulation   |  -> Evaluate LIFO operations (PUSH / POP / MATH)
  +-----------------------+
```

</div>

### Project Structure

```
├── opcodes.py      # Enum definitions for supported hardware instruction sets
├── vm.py           # Core Virtual Machine execution loop and stack state
└── main.py         # Program entry point and bytecode stream definition
```

</div>

<div id="opcodes">

## 📜 Instruction Set (Opcodes)

| Opcode | Hex Representation | Description |
| :--- | :---: | :--- |
| `PUSH` | `0x01` | Pushes a literal integer operand onto the top of the stack. |
| `ADD` | `0x02` | Pops the top two elements, computes `a + b`, pushes result back. |
| `PRINT` | `0x03` | Pops the top element from the stack and writes to terminal. |
| `HALT` | `0x04` | Immediately stops the virtual machine execution loop. |

</div>

<div id="usage">

## 💻 Example Usage

<div id="code-snippet">

```python
from vm import VirtualMachine
from opcodes import OpCodes

def main() -> None:
    bytecode = [
        (OpCodes.PUSH, 23),
        (OpCodes.PUSH, 12),
        (OpCodes.ADD, None),
        (OpCodes.PRINT, None),
        (OpCodes.HALT, None)
    ]
    
    print("Starting VirtualMachine...")
    machine = VirtualMachine(bytecode)
    machine.run()
    print("Vipolneno")

if __name__ == "__main__":
    main()
```

</div>

### Output

```console
Starting VirtualMachine...
[VM OUTPUT] 35
Vipolneno
```

</div>

<hr />

<div id="license" align="center">

  <sub>Built with passion for low-level systems. Licensed under <a href="LICENSE">MIT</a>.</sub>

</div>
