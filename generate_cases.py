import csv

# Define the 30 troubleshooting cases required for the project
cases = [
    ["Symptom", "Topology Note", "Show Outputs", "Expected Fault", "OSI Layer", "Concept Tag", "Severity"],
    ["PC gets IP but cannot reach server in VLAN 30", "Gateway ping works", "show ip route; show access-lists", "Inter-VLAN routing or ACL issue", "Layer 3/4", "Routing/ACL", "High"],
    ["Guest WiFi can reach internal server", "Guest isolation required", "show access-lists; show run", "Guest isolation failure", "Layer 3", "Security/ACL", "High"],
    ["PC cannot reach default gateway", "PC and router connected directly", "show interfaces; show run", "Interface administratively down", "Layer 1", "Physical", "High"],
    ["No PCs in VLAN 10 can communicate", "Switches connected via trunk", "show interfaces trunk", "VLAN 10 not allowed on trunk", "Layer 2", "VLAN", "High"],
    ["PC in VLAN 20 has no IP address", "DHCP server on router", "show ip dhcp binding", "DHCP pool exhausted", "Layer 7", "DHCP", "Medium"],
    ["PC cannot browse to www.cisco.com", "Ping to 8.8.8.8 succeeds", "show run", "Wrong DNS server IP configured on PC", "Layer 7", "DNS", "Medium"],
    ["Router cannot reach remote subnet", "OSPF configured", "show ip ospf neighbor", "OSPF subnet mismatch", "Layer 3", "Routing", "High"],
    ["Internal PCs cannot access internet", "NAT configured", "show ip nat translations", "Missing 'ip nat inside/outside' on interface", "Layer 3", "NAT", "High"],
    ["Wireless laptop keeps disconnecting", "WPA2 configured", "show run", "WPA2 password mismatch", "Layer 2", "Wireless", "High"],
    ["PC port LED is amber and blinking", "Switchport configured for access", "show interfaces status", "Port security violation (err-disabled)", "Layer 2", "Security", "High"],
    ["Router drops all incoming web traffic", "Standard ACL applied inbound", "show access-lists", "Implicit deny blocking all traffic", "Layer 3/4", "ACL", "High"],
    ["PCs getting IPs from wrong subnet", "Two routers on same segment", "show ip dhcp conflict", "Rogue DHCP server active", "Layer 7", "DHCP", "Critical"],
    ["Cannot ping across serial link", "Point-to-point serial connection", "show controllers", "Clock rate not set on DCE", "Layer 1", "Physical", "High"],
    ["Traffic routing through slow backup link", "EIGRP configured", "show ip eigrp topology", "Bandwidth statement incorrect on primary interface", "Layer 3", "Routing", "Medium"],
    ["DNS queries timing out", "DNS server reachable", "show ip access-lists", "ACL blocking UDP port 53", "Layer 4", "ACL", "High"],
    ["VLAN 40 exists on Sw1 but not Sw2", "VTP configured", "show vtp status", "VTP domain name mismatch", "Layer 2", "VLAN", "Medium"],
    ["Router routing table is empty", "RIPv2 configured", "show ip protocols", "Auto-summary combining disparate subnets", "Layer 3", "Routing", "High"],
    ["Only one PC can access internet at a time", "NAT configured", "show ip nat statistics", "NAT pool exhausted (overload/PAT missing)", "Layer 3", "NAT", "High"],
    ["Wireless AP not broadcasting SSID", "WLC connected to network", "show capwap ip config", "AP disconnected from WLC", "Layer 2/3", "Wireless", "High"],
    ["Inter-VLAN routing failing (Router on a stick)", "Subinterfaces created", "show vlans", "Encapsulation dot1Q VLAN ID mismatch", "Layer 2", "VLAN", "High"],
    ["Ping fails with 'Destination host unreachable'", "Static routing used", "show ip route", "Missing static route to destination", "Layer 3", "Routing", "High"],
    ["Web server inaccessible from internet", "Static NAT configured", "show run", "Wrong inside local IP mapped in NAT rule", "Layer 3", "NAT", "High"],
    ["Switch interface experiencing high collisions", "Direct connection to old hub", "show interfaces", "Duplex mismatch (Half/Full)", "Layer 2", "Physical", "Medium"],
    ["DHCP clients not receiving IPs on remote VLAN", "Router acting as DHCP server", "show run interface", "Missing ip helper-address on gateway", "Layer 3/7", "DHCP", "High"],
    ["Access port assigned to missing VLAN", "PC connected to switch", "show vlan brief", "VLAN does not exist in VLAN database", "Layer 2", "VLAN", "Medium"],
    ["Network 10.0.0.0 unreachable via OSPF", "Multiple areas configured", "show ip ospf", "Missing network statement in Area 0", "Layer 3", "Routing", "High"],
    ["Extended ACL not blocking specific host", "ACL applied closest to source", "show access-lists", "Wrong sequence order (permit statement before deny)", "Layer 3/4", "ACL", "Medium"],
    ["IPv6 clients cannot reach internet", "Dual-stack network", "show ipv6 route", "Missing IPv6 default route", "Layer 3", "Routing", "High"],
    ["Switch administration via SSH failing", "VTY lines configured", "show run", "Transport input set to telnet only", "Layer 7", "Security", "Medium"],
    ["Network unstable with looping traffic", "Redundant links between switches", "show spanning-tree", "STP disabled globally", "Layer 2", "STP", "Critical"]
]

# Write to CSV
with open("cases.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(cases)

print("Success! Generated 'cases.csv' with 30 troubleshooting cases.")