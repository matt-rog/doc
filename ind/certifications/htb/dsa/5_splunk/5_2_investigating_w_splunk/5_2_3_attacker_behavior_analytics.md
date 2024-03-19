# Detecting Attacker Behavior With Splunk Based On Analytics

https://academy.hackthebox.com/module/218/section/2390

# Labs

1. Navigate to http://[Target IP]:8000, open the "Search & Reporting" application, and find through an analytics-driven SPL search against all data the source process images that are creating an unusually high number of threads in other processes. Enter the outlier process name as your answer where the number of injected threads is greater than two standard deviations above the average. Answer format: \_.exe

<details>
<summary>Guide</summary>

From the sysmon docs, we'll likely want to use a combination of the first command in the module and events with code `8`.

```
index="main" sourcetype="WinEventLog:Sysmon" EventCode=8 | bin _time span=1h | stats count as Threads by _time, SourceImage | streamstats time_window=24h avg(Threads) as avg stdev(Threads) as stdev by SourceImage | eval isOutlier=if(Threads > (avg + (2*stdev)), 1, 0) | search isOutlier=1
```

For some reason this was returning no results, so I took off the "isOutlier" qualifier and just looked at the most prominent processes.

```
index="main" sourcetype="WinEventLog:Sysmon" EventCode=8
| bin _time span=1h
| stats count as Threads by _time, SourceImage
| streamstats time_window=24h avg(Threads) as avg stdev(Threads) as stdev by SourceImage
| sort - stdev
```

Take the executable with the highest stdev.

</details>
<details>
<summary>Answer</summary>
randomfile.exe
</details>
