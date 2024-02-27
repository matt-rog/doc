# Skills Assessment

# Lab

1. By examining the logs located in the "C:\Logs\DLLHijack" directory, determine the process responsible for executing a DLL hijacking attack. Enter the process name as your answer. Answer format: \_.exe

<details>
<summary>Guide</summary>

Get-WinEvent allows for fast iterations on queries and also easy data output, which is useful for analysis in other tools. Let's use it to find the executable responsible.

We at least know to start with:

```ps
Get-WinEvent -Path 'C:\Logs\DLLHijack\DLLHijack.evtx' | Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message > output.txt
```

We need to know something about DLL hijacking to narrow down results. We know the EventID for image loading (?) is `7`. Our query becomes:

```ps
Get-WinEvent -Path 'C:\Logs\DLLHijack\DLLHijack.evtx' | Where-Object { $_.ID -eq 7 } | Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message > output.txt
```

The module mentions:

```
The event log contains the DLL's signing status (in this case, it is Microsoft-signed), the process or image responsible for loading the DLL, and the specific DLL that was loaded. In our example, we observe that "MMC.exe" loaded "psapi.dll", which is also Microsoft-signed. Both files are located in the System32 directory.
```

It seems like images loading from the Sys32 directory are most likely safe. Also the dll-hijack demo from that modules requires us to use images outside of sys32. Let's only look for images loaded outside of sys32.

```ps
Get-WinEvent -Path 'C:\Logs\DLLHijack\DLLHijack.evtx' | Where-Object { $_.ID -eq 7 -and $_.Message -notmatch "ImageLoaded: C:\\Windows\\System32\\" } | Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message > output.txt
```

This will get you some dozen results. You'll see many are false positives from `C:\Program Files (x86)\Microsoft\`. You could
filter to also exclude this directory, but even without it you can scroll around a bit and find an event that's the exception.

</details>
<details>
<summary>Answer</summary>
Dism.exe
</details>

2. By examining the logs located in the "C:\Logs\PowershellExec" directory, determine the process that executed unmanaged PowerShell code. Enter the process name as your answer. Answer format: \_.exe

<details>
<summary>Guide</summary>

Similar to part 1, let's look back at what the module says about unmanaged processes.

```
C# is considered a "managed" language, meaning it requires a backend runtime to execute its code. The Common Language Runtime (CLR) serves as this runtime environment. Managed code does not directly run as assembly; instead, it is compiled into a bytecode format that the runtime processes and executes. Consequently, a managed process relies on the CLR to execute C# code.

The presence of "Microsoft .NET Runtime...", clr.dll, and clrjit.dll should attract our attention. These 2 DLLs are used when C# code is ran as part of the runtime to execute the bytecode. If we observe these DLLs loaded in processes that typically do not require them, it suggests a potential execute-assembly or unmanaged PowerShell injection attack.
```

We'll try to target these dll's to narrow down our results.

```ps
Get-WinEvent -Path 'C:\Logs\PowershellExec\PowershellExec.evtx' -Oldest | Where-Object { $_.ID -eq 7 -and $_.Message -like "*clrjit.dll*"} | Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message > output.txt
```

You'll have two results. One is a shell that loaded the dll, the other is program that loaded the dll. The flag is this program.

</details>
<details>
<summary>Answer</summary>
Calculator.exe
</details>

3. By examining the logs located in the "C:\Logs\PowershellExec" directory, determine the process that injected into the process that executed unmanaged PowerShell code. Enter the process name as your answer. Answer format: \_.exe

<details>
<summary>Guide</summary>

I found this one difficult. The tooling became very slow and it was harder to iterate on queries.

Knowing that we're looking for the parent process of `Calculator.exe` from problem 2, I first tried experimenting with the following query, using variations of `Calculator.exe`

```ps
Get-WinEvent -Path 'C:\Logs\PowershellExec\PowershellExec.evtx' -Oldest | Where-Object { $_.ID -eq 7 -and $_.Message -like "*Calculator.exe*"} | Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message > output.txt
```

I was getting no results from this, at least no timely results. After some hours no luck, I looked online for help and find [this](https://forum.hackthebox.com/t/windows-event-logs-finding-evil-mini-module/301639), which recommended looking at the `CreateRemoteThread` events (EventId is 8).

```ps
Get-WinEvent -Path 'C:\Logs\PowershellExec\PowershellExec.evtx' -Oldest | Where-Object { $_.ID -eq 8 -and $_.Message -like "*Calculator.exe*"} | Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message > output.txt
```

This gave me two relevant results, both mentioning Calculator.exe and another executable. The other is the flag.

</details>
<details>
<summary>Answer</summary>
rundll32.exe
</details>
