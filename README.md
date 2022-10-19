# ExodusC2
This Command and Control PoC is made to cross the red sea of blue teaming solutions. ExodusC2 is not to be confused with the mobile malware strain called Exodus, and no I am not christian though I like the biblical reference. Operating from a client-server model, it (intends to ) evade(s) at least most commercial EDR solutions. Beacons/clients in ExodusC2 leverage from functions of ScareCrow, a famous payload generation tool payloads that want to evade monitoring solutions. 

Also attempts will be made to evade syscall recording from an amazing tool based on dtrace. The tool is called dgenerate, made by Jonas Lyk: https://github.com/jonaslyk/temp, big love to that danish lad <3

<p align="center">
  <img src="https://user-images.githubusercontent.com/59022605/190503049-a4ba6757-de2d-4b15-ac09-627b6b9297b8.png" data-canonical-src="https://user-images.githubusercontent.com/59022605/190503049-a4ba6757-de2d-4b15-ac09-627b6b9297b8.png" height="600" />
</p>

<p align="center">
Amazing picture made by some dude with Midjourney
</p>

## Features
- Fully CLI, fancy GUI is for plebs and marketing anyways xD
- I like snakes so server and client will be python
- Ed25519 for the client-server authentication 

- Customizeable Windows client
  + Might make Linux and OSX clients later
  + Beacon activity logging
  + Packing with **Something**, because fuck you thats why
  + eBPF bypass to evade network monitoring capabilities
  + AMSI & ETW Patching
  + DLL Unhooking
  + NTAPI callback evasion

- File hosting server
  + Password based authentication
  + OTP/2FA is an option; BEWARE to have similiar timezones on client and server need to be configured correctly
  + Hosting over HTTP and HTTPs

- Built in covert channels:
  - TCP, HTTP, HTTP2, HTTP3, DNS, ICMP, FTP, IMAP, MAPI, DNS over HTTPS (DoH), SMB and anything you can make yourself.


## Setup
You either compile or download compiled version

## Server
### Windows
`ExodusC2_server.exe`

## Beacon

## EDR Evasion

## Make your own covert channel

## But's and if's
This isnt a bulletproof one-stop-shop. You could probably find bugs in this PoC, if not many ways to detect this. This is just an effort to see how far I can get trying to evade stuff I know exist. But I dont know everything that exists, so I am relying on community feedback here. Find a way to do it better, say so. Or keep it a secret.... 

Oh and this is for educational purposes only, I am not responsible for your bullshit in court.



