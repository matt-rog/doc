# Skills Assessment

https://academy.hackthebox.com/module/214/section/2287

Hunt 1: Create a KQL query to hunt for "Lateral Tool Transfer" to C:\Users\Public. Enter the content of the user.name field in the document that is related to a transferred tool that starts with "r" as your answer.

Hunt 2: Create a KQL query to hunt for "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder". Enter the content of the registry.value field in the document that is related to the first registry-based persistence action as your answer.

Hunt 3: Create a KQL query to hunt for "PowerShell Remoting for Lateral Movement". Enter the content of the winlog.user.name field in the document that is related to PowerShell remoting-based lateral movement towards DC1.

# Labs

1. Enter your answer for Hunt 1.

message:"C:\Users\Public"
svc-sql1

2. Enter your answer for Hunt 2.

https://attack.mitre.org/techniques/T1547/001/
registry.path:"CurrentVersion\Run"
LgvHsviAUVTsIN

3. Enter your answer for Hunt 3.

event.code:4104 AND message:"DC1"
svc-sql1
