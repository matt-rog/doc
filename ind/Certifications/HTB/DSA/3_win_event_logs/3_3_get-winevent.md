# Get-WinEvent

The Get-WinEvent cmdlet is an indispensable tool in PowerShell for querying Windows Event logs en masse.
https://academy.hackthebox.com/module/216/section/2322
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent?view=powershell-7.3

### Usage Examples

Identify available logs:

```
Get-WinEvent -ListLog * | Select-Object LogName, RecordCount, IsClassicLog, IsEnabled, LogMode, LogType | Format-Table -AutoSize
```

Identify event log providers:

```
Get-WinEvent -ListProvider * | Format-Table -AutoSize
```

By default it returns the newest logs, `-Oldest` sorts opposite

Reading from existing .evtx files:

```
Get-WinEvent -Path 'C:\path\to.evtx' -MaxEvents 5 | Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message | Format-Table -AutoSize
```

### FIlterHashTable

The command retrieves events with IDs 1 and 3 from the Microsoft-Windows-Sysmon/Operational event log,

```
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; ID=1,3} | ...
```

Same filter with an .evtx

```
Get-WinEvent -FilterHashtable @{Path='C:\path\to.evtx'; ID=1,3}
```

Date filtering

```
$startDate = (Get-Date -Year 2023 -Month 5 -Day 28).Date; $endDate   = (Get-Date -Year 2023 -Month 6 -Day 3).Date;
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; ID=1,3; StartTime=$startDate; EndTime=$endDate}
```

Filtering via xml (ultra useful)

```
PS C:\Users\Administrator> $Query = @"
	<QueryList>
		<Query Id="0">
			<Select Path="Microsoft-Windows-Sysmon/Operational">*[System[(EventID=7)]] and *[EventData[Data='mscoree.dll']] or *[EventData[Data='clr.dll']]
			</Select>
		</Query>
	</QueryList>
	"@
PS C:\Users\Administrator> Get-WinEvent -FilterXml $Query | ...
```

Also some in-line regex filter options

# Lab

1. Utilize the Get-WinEvent cmdlet to traverse all event logs located within the "C:\Tools\chainsaw\EVTX-ATTACK-SAMPLES\Lateral Movement" directory and determine when the \\\\\*\PRINT share was added. Enter the time of the identified event in the format HH:MM:SS as your answer.

<details>
<summary>Guide</summary>

If you look in C:\Tools\chainsaw\EVTX-ATTACK-SAMPLES\Lateral Movement, you'll see a ton of .evtx files. It turns out you can just put a wildcard `*` in your query to catch them all. \
So then we get something like this.

```
Get-WinEvent -Path 'C:\Tools\chainsaw\EVTX-ATTACK-SAMPLES\Lateral Movement\*.evtx'
```

Because there are so many, this will take several seconds to run and give us way too much data. We know we're trying to find a "print" share. Quick [search](https://stackoverflow.com/questions/45376593/grep-string-from-message-in-get-winevent) and we can use something like:

```
Get-WinEvent -Path 'C:\Tools\chainsaw\EVTX-ATTACK-SAMPLES\Lateral Movement\*.evtx' | Where-Object{$_.Message -like "*PRINT*"}
```

Format and catch the output

```
Get-WinEvent -Path 'C:\Tools\chainsaw\EVTX-ATTACK-SAMPLES\Lateral Movement\*.evtx' | Where-Object{$_.Message -like "*PRINT*"} | Select-Object TimeCreated, ID, ProviderName, LevelDisplayName, Message > output.txt
```

This will give you ~5 results. Look around and you'll find one that matches \\\\\*\PRINT. The time is the flag.

Note: You could certainly optimize the filtering done here to give you quicker and narrower results.

</details>
<details>
<summary>Answer</summary>
12:30:30
</details>
