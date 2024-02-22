# Analyzing Evil With Sysmon & Event Logs
**System Monitor (Sysmon)** is a Windows system service and device driver that 
remains resident across system reboots to monitor and log system activity to the Windows event log. 
Sysmon provides detailed information about process creation, network connections, changes to file creation time, and more. \
Includes:
- A Windows service for monitoring system activity.
- A device driver that assists in capturing the system activity data.
- An event log to display captured activity data.

Docs and Event IDs: https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon \
XML Config: https://github.com/SwiftOnSecurity/sysmon-config \
Download: https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon

Install command
```ps
sysmon.exe -i -accepteula -h md5,sha256,imphash -l -n
```
Use custom config
```ps
sysmon.exe -c filename.xml
```
Once config updated, to view these events, navigate to the Event Viewer and access "Applications and Services" -> "Microsoft" -> "Windows" -> "Sysmon."
