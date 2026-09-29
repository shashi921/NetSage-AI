import csv

# Dashboard Summary Data: Issue Themes and AI Agreement Rate
dashboard_data = [
    ["NetSage AI - Executive Dashboard"],
    [""],
    ["Metric", "Value"],
    ["Total Cases Analyzed", "30"],
    ["Cases Accepted (AI Correct)", "25"],
    ["Cases Rejected/Edited (Human Corrected)", "5"],
    ["AI Overall Agreement Rate", "83.3%"],
    [""],
    ["Issue Themes", "Count"],
    ["Routing & Layer 3", "9"],
    ["VLAN & Layer 2", "7"],
    ["ACL & Security", "5"],
    ["DHCP & DNS (Layer 7)", "5"],
    ["Physical & Wireless", "4"]
]

with open("dashboard.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(dashboard_data)

print("Success! Generated the final 'dashboard.csv'. Project files complete!")