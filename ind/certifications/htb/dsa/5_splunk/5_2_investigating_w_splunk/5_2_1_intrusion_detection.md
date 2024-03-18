# Intrusion Detection With Splunk (Real-world Scenario)

https://academy.hackthebox.com/module/218/section/2357

# Labs

1. Navigate to http://[Target IP]:8000, open the "Search & Reporting" application, and find through an SPL search against all data the other process that dumped lsass. Enter its name as your answer. Answer format: \_.exe

<details>
<summary>Guide</summary>

Searching through past labs for 'lsass', we see an old lab where we used event id 10 and 'C:\Windows\system32\lsass.exe' to find lsass dumps. Let's start here.

```
EventCode=10 TargetImage="C:\\Windows\\system32\\lsass.exe"
```

This gives us ~240 events, with 8 distinct SourceImage values, many of which look like false positives. We see most of the events are NT AUTH -> NT AUTH, and a fraction is user -> NT AUTH.
It is more likely a user is dumping lsass.

```
EventCode=10 TargetImage="C:\\Windows\\system32\\lsass.exe" SourceUser!="NT AUTHORITY\\SYSTEM"
```

This gives us only 5 events with only 2 distinct SourceImage values. We know one of these images can be used to execute malicious code.

</details>
<details>
<summary>Answer</summary>
rundll32.exe
</details>

2. Navigate to http://[Target IP]:8000, open the "Search & Reporting" application, and find through SPL searches against all data the method through which the other process dumped lsass. Enter the misused DLL's name as your answer. Answer format: \_.dll

<details>
<summary>Guide</summary>

Using the process guid from the rundll32 events, `96192a2a-09d5-6368-3b05-000000000900`, I searched to find all events referencing some dll.

```
96192a2a-09d5-6368-3b05-000000000900 "*.dll*"
```

This returned some events, with a couple referencing command line arguments involving a dll.

</details>
<details>
<summary>Answer</summary>
comsvcs.dll
</details>

3. Navigate to http://[Target IP]:8000, open the "Search & Reporting" application, and find through an SPL search against all data any suspicious loads of clr.dll that could indicate a C# injection/execute-assembly attack. Then, again through SPL searches, find if any of the suspicious processes that were returned in the first place were used to temporarily execute code. Enter its name as your answer. Answer format: \_.exe

<details>
<summary>Guide</summary>

Looking back at 3_4_skills_assessment, lab 2, we were faced with a similar problem and targeted event code 7 and clrjit.dll and clr.dll.

```
EventCode=7 "*clr*.dll*"
```

This gives us ~900 results. But if the execution tree is executable 1 > executable 2 > clr.dll, then our answer will be executable #2. This query has ~900 executable #2's, but we only want to look at the ones which have an executable #1 associated with it. Using more info from 3_4_skills_assessment, we'll look at events with code 8 that are spawning our executable 2.

```
EventCode=7 "*clr*.dll*"
| join Image
    [search index=* EventCode=8
    | rename TargetImage as Image
    | fields Image]
```

This gives us 2 executables in the Image field. One of them is commonly used to load code, this is the flag.

</details>
<details>
<summary>Answer</summary>
rundll32.exe
</details>

4. Navigate to http://[Target IP]:8000, open the "Search & Reporting" application, and find through SPL searches against all data the two IP addresses of the C2 callback server. Answer format: 10.0.0.1XX and 10.0.0.XX

<details>
<summary>Guide</summary>

We'll look for network events regarding the previous executable.

```
"C:\\Windows\\system32\\rundll32.exe" EventCode=3
```

There are only two destination IP's in these logs and they fit the appropriate format.

</details>
<details>
<summary>Answer</summary>
10.0.0.186 and 10.0.0.91
</details>

5. Navigate to http://[Target IP]:8000, open the "Search & Reporting" application, and find through SPL searches against all data the port that one of the two C2 callback server IPs used to connect to one of the compromised machines. Enter it as your answer.

<details>
<summary>Guide</summary>

```
EventCode=3 SourceIp=10.0.0.91 OR SourceIp=10.0.0.186
```

We're looking for the (destination) port on the compromised machine.

</details>
<details>
<summary>Answer</summary>
3389
</details>
