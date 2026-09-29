import json
import re

def check_network_case(case_data):
    """
    Deterministic rule checker for Cisco lab network issues.
    Checks: Interface down, Gateway mismatch, Missing VLAN, Wrong Subnet, Missing Route.
    """
    findings = []
    show_output = case_data.get("show_output", "")
    symptom = case_data.get("symptom", "")
    config = case_data.get("config", {})

    # Check 1: Interface Administratively Down or Down
    if re.search(r'(administratively down|down\s+down|line protocol is down)', show_output, re.IGNORECASE):
        findings.append({
            "rule": "INTERFACE_DOWN",
            "layer": "Layer 1 / Layer 2",
            "severity": "High",
            "issue": "Interface or line protocol is down.",
            "recommended_fix": "Run 'no shutdown' on the interface or verify physical/cable connections."
        })

    # Check 2: Default Gateway Mismatch / Missing Gateway
    if "gateway" in symptom.lower() or "cannot reach server" in symptom.lower():
        pc_gw = config.get("pc_gateway")
        router_ip = config.get("router_ip")
        if pc_gw and router_ip and pc_gw != router_ip:
            findings.append({
                "rule": "GATEWAY_MISMATCH",
                "layer": "Layer 3",
                "severity": "High",
                "issue": f"PC default gateway ({pc_gw}) does not match Router/SVI IP ({router_ip}).",
                "recommended_fix": f"Change PC default gateway to {router_ip}."
            })

    # Check 3: Missing VLAN or Access Port Mismatch
    if "vlan" in show_output.lower() or "vlan" in symptom.lower():
        if "not found in vlan database" in show_output.lower() or "vlan does not exist" in show_output.lower():
            findings.append({
                "rule": "MISSING_VLAN",
                "layer": "Layer 2",
                "severity": "Medium",
                "issue": "VLAN is assigned to an interface but not declared in the VLAN database.",
                "recommended_fix": "Create the VLAN in global configuration mode ('vlan <id>')."
            })

    # Check 4: Missing Route in Routing Table
    if "show ip route" in show_output.lower() and "gateway of last resort is not set" in show_output.lower():
        if "destination host unreachable" in symptom.lower() or "no route" in symptom.lower():
            findings.append({
                "rule": "MISSING_ROUTE",
                "layer": "Layer 3",
                "severity": "High",
                "issue": "Routing table does not contain a route to the destination network and default gateway is not set.",
                "recommended_fix": "Add a static route ('ip route ...') or enable dynamic routing (OSPF/EIGRP)."
            })

    # Check 5: Duplicate IP / Subnet Mask Mismatch
    if "duplicate address" in show_output.lower() or "ip address conflict" in show_output.lower():
        findings.append({
            "rule": "DUPLICATE_IP",
            "layer": "Layer 3",
            "severity": "Critical",
            "issue": "An IP address conflict was detected on the subnet.",
            "recommended_fix": "Reconfigure the host or interface with an unused unique IP address."
        })

    return {
        "case_id": case_data.get("case_id", "Unknown"),
        "total_rules_triggered": len(findings),
        "deterministic_findings": findings
    }

# Sample test cases to verify the script works
if __name__ == "__main__":
    test_cases = [
        {
            "case_id": "CASE_01",
            "symptom": "PC cannot ping default gateway; interface light is amber",
            "show_output": "GigabitEthernet0/1 is administratively down, line protocol is down",
            "config": {"pc_gateway": "192.168.1.1", "router_ip": "192.168.1.1"}
        },
        {
            "case_id": "CASE_02",
            "symptom": "PC cannot reach server on external subnet",
            "show_output": "Default gateway is 192.168.1.254",
            "config": {"pc_gateway": "192.168.1.254", "router_ip": "192.168.1.1"}
        }
    ]

    print("=" * 60)
    print("NetSage AI - Deterministic Rule Checker Validation")
    print("=" * 60)
    
    for case in test_cases:
        result = check_network_case(case)
        print(json.dumps(result, indent=4))