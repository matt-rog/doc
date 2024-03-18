# Introduction to Splunk & SPL

https://academy.hackthebox.com/module/218/section/2356

# Labs

1. Navigate to http://[Target IP]:8000, open the "Search & Reporting" application, and find through an SPL search against all data the account name with the highest amount of Kerberos authentication ticket requests. Enter it as your answer.

<details>
<summary>Guide</summary>

It looks like the index we're going to use is 'main'.

https://www.manageengine.com/products/active-directory-audit/how-to/audit-kerberos-authentication-events.html

We want to use the security logs and event id 4768.

```
index="main" sourcetype="WinEventLog:Security" EventCode=4768
| stats count by Account_Name
| sort - count
```

</details>
<details>
<summary>Answer</summary>
waldo
</details>

2. Navigate to http://[Target IP]:8000, open the "Search & Reporting" application, and find through an SPL search against all 4624 events the count of distinct computers accessed by the account name SYSTEM. Enter it as your answer.

<details>
<summary>Guide</summary>

The logs are a little weird to interpret but after some poking and using the hint, I arrived at.

```
index="main" EventCode=4624 Account_Name=SYSTEM
| stats dc(ComputerName) as dccn
| table dccn
```

</details>
<details>
<summary>Answer</summary>
10
</details>

3. Navigate to http://[Target IP]:8000, open the "Search & Reporting" application, and find through an SPL search against all 4624 events the account name that made the most login attempts within a span of 10 minutes. Enter it as your answer.

<details>
<summary>Guide</summary>

You have to know about how these auth logs are generated.
Using [this](https://forum.hackthebox.com/t/understanding-log-sources-investigating-with-splunk-introduction-to-splunk-spl/287545/19) as a guide.

```
index=* EventCode=4624
| stats min(_time) as firstLogin, max(_time) as lastLogin by Account_Name
| eval timeDiff=lastLogin - firstLogin
| where timeDiff <= 600
| eval firstLogin=strftime(firstLogin,"%Y-%m-%d %H:%M:%S")
| eval lastLogin=strftime(lastLogin, "%Y-%m-%d %H:%M:%S")
| table Account_Name, firstLogin, lastLogin, timeDiff
| sort - timeDiff
```

</details>
<details>
<summary>Answer</summary>
aparsa
</details>
