# Using Splunk Applications

https://academy.hackthebox.com/module/218/section/2389

# Labs

1. Access the Sysmon App for Splunk and go to the "Reports" tab. Fix the search associated with the "Net - net view" report and provide the complete executed command as your answer. Answer format: net view /Domain:\_.local

<details>
<summary>Guide</summary>

The command line is probably not just "net view". Accounting for this:

```
`sysmon` process=net.exe (CommandLine="*net  view*") | stats count by Computer,CommandLine
```

Still nothing. There's also rarely double spaces in commands:

```
`sysmon` process=net.exe (CommandLine="*net view*") | stats count by Computer,CommandLine
```

</details>
<details>
<summary>Answer</summary>
net view /DOMAIN:uniwaldo.local
</details>

2. Access the Sysmon App for Splunk, go to the "Network Activity" tab, and choose "Network Connections". Fix the search and provide the number of connections that SharpHound.exe has initiated as your answer.

<details>
<summary>Guide</summary>

I cheesed this one, just aiming for the flag.

```
sourcetype="WinEventLog:Sysmon" EventCode=3
| stats count by Image
| search Image="*SharpHound.exe*"
```

</details>
<details>
<summary>Answer</summary>
6
</details>
