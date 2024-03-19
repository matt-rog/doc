# Skills Assessment

https://academy.hackthebox.com/module/218/section/2358

# Lab

1. Navigate to http://[Target IP]:8000, open the "Search & Reporting" application, and find through SPL searches against all data the process that created remote threads in rundll32.exe. Answer format: \_.exe

<details>
<summary>Guide</summary>

This very directly lines up with the question.

```
EventCode=8 TargetImage="*rundll32.exe*"
| table SourceImage
```

</details>
<details>
<summary>Answer</summary>
randomfile.exe
</details>

2. Navigate to http://[Target IP]:8000, open the "Search & Reporting" application, and find through SPL searches against all data the process that started the infection. Answer format: \_.exe

<details>
<summary>Guide</summary>

Poorly-worded question. HTB Discord pointed me to the process exploited in part 1.

</details>
<details>
<summary>Answer</summary>
rundll32.exe
</details>
