# Threat Hunting with the Elastic Stack

https://academy.hackthebox.com/module/214/section/2285

## Hunting for Stuxbot

Persistence

All persistence mechanisms utilized to date have involved an EXE file deposited on the disk.

Lateral Movement

So far, we have identified two distinct methods for lateral movement:

    Leveraging the original, Microsoft-signed PsExec
    Using WinRM

Indicators of Compromise (IOCs)

The following provides a comprehensive inventory of all identified IOCs to this point.

OneNote File:

    https://transfer.sh/get/kNxU7/invoice.one
    https://mega.io/dl9o1Dz/invoice.one

Staging Entity (PowerShell Script):

    https://pastebin.com/raw/AvHtdKb2
    https://pastebin.com/raw/gj58DKz

Command and Control (C&C) Nodes:

    91.90.213.14:443
    103.248.70.64:443
    141.98.6.59:443

Cryptographic Hashes of Involved Files (SHA256):

    226A723FFB4A91D9950A8B266167C5B354AB0DB1DC225578494917FE53867EF2
    C346077DAD0342592DB753FE2AB36D2F9F1C76E55CF8556FE5CDA92897E99C7E
    018D37CBD3878258C29DB3BC3F2988B6AE688843801B9ABC28E6151141AB66D4
