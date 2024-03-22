# Introduction and Terminology

https://academy.hackthebox.com/module/176/section/1753

## Authentication in Windows Environments

LDAP is a protocol that systems in the network environment use to communicate with Active Directory. Domain Controller(s) run LDAP and constantly listen for requests from the network.

- Username/Password, stored or transmitted as password hashes (LM, NTLM, NetNTLMv1/NetNTLMv2).
- Kerberos tickets (Microsoft's implementation of the Kerberos protocol). Kerberos acts as a trusted third party, working with a domain controller (DC) to authenticate clients trying to access services. The Kerberos authentication workflow revolves around tickets that serve as cryptographic proof of identity that clients exchange between each other, services, and the DC.
- Authentication over LDAP. Authentication is allowed via the traditional username/password or user or computer certificates.

Key Distribution Center (KDC): a Kerberos service installed on a DC that creates tickets. Components of the KDC are the authentication server (AS) and the ticket-granting server (TGS).

Kerberos Tickets are tokens that serve as proof of identity (created by the KDC):

- TGT is proof that the client submitted valid user information to the KDC.
- TGS is created for each service the client (with a valid TGT) wants to access.

KDC key is an encryption key that proves the TGT is valid. AD creates the KDC key from the hashed password of the KRBTGT account, the first account created in an AD domain. Although it is a disabled user, KRBTGT has the vital purpose of storing secrets that are randomly generated keys in the form of password hashes. One may never know what the actual password value represents (even if we try to configure it to a known value, AD will automatically override it to a random one).

## Relevant Network Ports

    53: DNS.
    88: Kerberos.
    135: WMI/RPC.
    137-139 & 445: SMB.
    389 & 636: LDAP.
    3389: RDP
    5985 & 5896: PowerShell Remoting (WinRM)
