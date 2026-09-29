import csv

# Define the 5 cases where the AI made a mistake and a human had to intervene
log_data = [
    ["Case ID", "Expected Fault", "AI Diagnosis", "Human Correction", "Reason for AI Failure"],
    ["CASE_04", "Interface administratively down", "Physical Layer 1 cable failure", "Engineer forgot to run 'no shutdown'", "AI confused 'administratively down' with a broken physical cable."],
    ["CASE_07", "Missing default route", "DNS server unreachable", "Added 'ip route 0.0.0.0 0.0.0.0' to router", "AI saw failing web traffic and assumed DNS, ignoring the empty routing table."],
    ["CASE_25", "Missing ip helper-address", "DHCP server service has crashed", "Added 'ip helper-address' to the gateway VLAN", "AI didn't realize the DHCP server was on a remote subnet requiring a relay."],
    ["CASE_08", "OSPF timer mismatch", "Missing OSPF network statement", "Matched Hello/Dead timers on both interfaces", "AI only checked 'show run ospf' and ignored the interface-level timer configurations."],
    ["CASE_13", "Static IP conflicts with DHCP pool", "Rogue DHCP server handing out bad IPs", "Created DHCP excluded-address range", "AI hallucinated a rogue server instead of realizing a static IP overlapped with the active pool."]
]

# Write to CSV
with open("responsible_ai_log.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(log_data)

print("Success! Generated 'responsible_ai_log.csv' with 5 human corrections.")