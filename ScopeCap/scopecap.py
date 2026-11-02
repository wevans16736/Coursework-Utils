# Wyatt Evans
# Updated 09/16/2026 (MM/DD/YYYY)
# Iowa State University

#!/usr/bin/env python3
import sys
import pyvisa

def get_resource_manager():
    # try native windows lib first
    try:
        return pyvisa.ResourceManager('@ivi')
    except Exception:
        # fallback to python backend
        return pyvisa.ResourceManager('@py')

def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "capture.png"
    rm = get_resource_manager()
    
    # auto-detect usbtmc devices
    resources = rm.list_resources('USB?*INSTR')
    if not resources:
        print("Error: No USB scope detected.")
        sys.exit(1)
        
    target = resources[0]
    print(f"Connecting to {target}...")
    
    try:
        scope = rm.open_resource(target)
        scope.timeout = 15000  # 15s timeout for transfer
        
        print("Querying screenshot data...")
        # get raw binary PNG payload from Keysight/Agilent scope
        img_bytes = scope.query_binary_values(':DISPlay:DATA? PNG, COLOR', datatype='B', container=bytes)
        
        with open(filename, 'wb') as f:
            f.write(img_bytes)
            
        print(f"Saved capture to {filename}")
        scope.close()
    except Exception as e:
        print(f"Error during capture: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

