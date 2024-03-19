# Detecting Attacker Behavior With Splunk Based On TTPs

https://academy.hackthebox.com/module/218/section/2388

# Labs

1. Navigate to http://[Target IP]:8000, open the "Search & Reporting" application, and find through SPL searches against all data the password utilized during the PsExec activity. Enter it as your answer.

<details>
<summary>Guide</summary>

Using commands directly provided in the module:

```
index="main" sourcetype="WinEventLog:Sysmon" EventCode=1 Image=*\\ipconfig.exe OR Image=*\\net.exe OR Image=*\\whoami.exe OR Image=*\\netstat.exe OR Image=*\\nbtstat.exe OR Image=*\\hostname.exe OR Image=*\\tasklist.exe | stats count by Image,CommandLine | sort - count
```

You'll have a series of commands, some of them feature a password.

</details>
<details>
<summary>Answer</summary>
Password@123
</details>
