Network Intrusion Detection System (Snort 3)

Project Description
This task involved setting up and configuring **Snort 3** as a Network Intrusion Detection System (NIDS) on Kali Linux. The goal was to monitor network traffic for potential threats and generate real-time alerts.

Implementation Details
- Environment: Kali Linux 2026
- Interface: `eth0` (IP: 192.168.220.37)
- Configuration: Modified `snort.lua` to define `HOME_NET` variables.
- Custom Detection: Created rules in `local.rules` to capture ICMP (Ping) traffic.

Key Achievements
- Successfully validated Snort 3 configuration with 0 warnings.
- Implemented signature-based detection for ICMP packets.
- Demonstrated real-time alerting via the Snort console.

Evidence of Completion
1. Real-Time Alerts
![Snort Live Alerts](Screenshots/snort_alerts.png)
Figure: Snort 3 capturing and alerting on live ICMP traffic.

2. Custom Ruleset
![Local Rules](Screenshots/local_rules.png)
Figure: Custom rule signature used for traffic detection.
