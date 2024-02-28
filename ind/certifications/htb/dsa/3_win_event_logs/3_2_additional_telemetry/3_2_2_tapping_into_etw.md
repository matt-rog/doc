# Tapping Into ETW

https://academy.hackthebox.com/module/216/section/2325

# Lab

1. Replicate executing Seatbelt and SilkETW as described in this section and provide the ManagedInteropMethodName that starts with "G" and ends with "ion" as your answer. "c:\Tools\SilkETW_SilkService_v8\v8" and "C:\Tools\GhostPack Compiled Binaries" on the spawned target contain everything you need.

<details>
<summary>Guide</summary>

Since the question mentions ManagedInteropMethodName (sounds like a C# name) and binaries, we'll probably just be following along with the second example in this section , "Detecting Malicious .NET Assembly Loading".

We want to track any .NET logs using SilkETW. \
From this directory (given by module)

```
c:\Tools\SilkETW_SilkService_v8\v8\SilkETW
```

Run this command (given by module)

```ps
SilkETW.exe -t user -pn Microsoft-Windows-DotNETRuntime -uk 0x2038 -ot file -p C:\windows\temp\etw.json
```

SilkETW will be recording logs to C:\windows\temp\etw.json. \
Via cmd, go into `C:\Tools\GhostPack Compiled Binaries`. \
Load the assembly by running Seatbelt (given by module) like

```ps
.\Seatbelt.exe TokenPrivileges
```

Check your etw.json. We're looking for something like ManagedInteropMethodName=G**\_\_\_**ion. Do CTRL+F and enter `ManagedInteropMethodName=G`. You'll find a method name, this is your flag.

</details>
<details>
<summary>Answer</summary>
GetTokenInformation
</details>
