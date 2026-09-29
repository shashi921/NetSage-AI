\# NetSage AI: Automated Network Troubleshooting Framework

\*\*Author:\*\* Chagamreddy Shashi Kumar Reddy (ECE Student)

\*\*Domains:\*\* Computer Networking, Applied Artificial Intelligence, Cyber Security



\## Project Overview

During my network engineering coursework and Cisco virtual labs, I observed that junior engineers frequently struggle to correlate complex CLI `show` command outputs with actual root causes. To solve this bottleneck, I designed and developed \*\*NetSage AI\*\*, a hybrid troubleshooting assistant for Cisco Packet Tracer environments. 



Instead of relying purely on generative AI—which can hallucinate and disrupt production routing—my project combines the reasoning capabilities of Large Language Models with the strict reliability of a deterministic Python rule-checker and mandatory human oversight.



\## Architecture \& Methodology

My troubleshooting system operates using a three-stage pipeline:

1\. \*\*Deterministic Rule Engine:\*\* I wrote a Python script (`rule\_checker.py`) that uses regular expressions to pre-validate basic configuration errors, such as duplicate IP addresses, gateway mismatches, and Layer 1/2 'administratively down' states.

2\. \*\*Structured Prompt Engineering:\*\* I engineered a strict JSON system prompt (`diagnose\_prompt.md`). This forces the AI to output highly structured data—the specific OSI layer, a confidence score, exact CLI evidence, and step-by-step remediation commands—rather than conversational text.

3\. \*\*Human-in-the-Loop (HITL) Safety Protocol:\*\* AI cannot be trusted blindly on enterprise networks. I enforced a strict rule where every AI diagnosis must be audited. Out of my 30 test cases, the AI hallucinated 5 times. I documented these failures in my Responsible AI Log, proving that mandatory human review is a non-negotiable safety requirement.



\## Empirical Results

\* \*\*Dataset:\*\* I built and benchmarked the system against a custom dataset of 30 complex Packet Tracer scenarios covering Inter-VLAN routing, OSPF, Access Control Lists (ACLs), DHCP, and NAT.

\* \*\*Accuracy:\*\* The system achieved an 83.3% first-try diagnostic accuracy rate.

\* \*\*Safety:\*\* Achieved a 100% safety rate by catching all 5 AI hallucinations via the HITL review process.



\## How to Run (Reproducibility)

1\. Clone this repository to your local machine.

2\. Ensure Python 3.x is installed.

3\. Run `python rule\_checker.py` to test the deterministic validation engine against sample cases.

4\. Run `python generate\_mits\_report.py` (requires `pip install fpdf`) to instantly generate the comprehensive 27-page technical project report.

