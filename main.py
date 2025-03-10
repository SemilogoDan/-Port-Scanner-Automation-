import nmap

def port_scan(target, start_port, end_port):
    """
    Scans a specific range of ports on the given target using Nmap.
    
    :param target: Target IP or hostname
    :param start_port: Start of the port range
    :param end_port: End of the port range
    """
    scanner = nmap.PortScanner()

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    # Perform the scan
    try:
        scanner.scan(target, f"{start_port}-{end_port}", arguments="-sS -Pn")
        
        # Check if the target is reachable
        if target not in scanner.all_hosts():
            print(f"❌ Error: Host {target} is down or unreachable.\n")
            return

        print(f"✅ Host {target} is up.\nOpen Ports:")
        
        # Process scan results
        for port in range(start_port, end_port + 1):
            try:
                state = scanner[target]['tcp'][port]['state']
                service = scanner[target]['tcp'][port].get('name', 'Unknown Service')
                print(f"🔹 Port {port}: {state} ({service})")
            except KeyError:
                print(f"⚠️  Port {port}: No response (filtered or closed)")

    except Exception as e:
        print(f"❌ Scan failed: {e}")

        # Example Usage
if __name__ == "__main__":
    target_ip = input("Enter target IP or hostname: ") or "127.0.0.1"
    start_port = int(input("Enter start port (default 75): ") or 75)
    end_port = int(input("Enter end port (default 80): ") or 80)

    port_scan(target_ip, start_port, end_port)