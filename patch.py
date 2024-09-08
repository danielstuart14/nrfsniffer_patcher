from intelhex import IntelHex
import sys

def parse_patch(patch):
    addr, data = patch.split(':')
    addr = int(addr, 16)
    old, new = data.split('>')

    return addr, bytearray.fromhex(old), bytearray.fromhex(new)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python patch.py <version.patch> <input.hex> <output.hex>")
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as f:
        patches = [parse_patch(line) for line in f.read().splitlines()]
    
    input_fw = IntelHex()
    input_fw.loadfile(sys.argv[2], format='hex')

    for addr, old, new in patches:
        if len(old) != len(new):
            raise ValueError(f"Patch at {addr:08X} has mismatched lengths")
        
        for i in range(len(old)):
            if input_fw[addr + i] != old[i]:
                raise ValueError(f"Patch at {addr:08X} does not match input firmware (expected {old[i]:02X}, got {input_fw[addr + i]:02X})")
            
            input_fw[addr + i] = new[i]
    
    input_fw.write_hex_file(sys.argv[3])
            
            

