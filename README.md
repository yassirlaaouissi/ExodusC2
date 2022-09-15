# ExodusC2
This Command and Control PoC is made to cross the red sea of blue teaming solutions. ExodusC2 is not to be confused with the mobile malware strain called Exodus, and no I am not christian though I like the biblical reference. Operating from a client-server model, it evades at least most commercial EDR solutions. Beacons in ExodusC2 leverage from integration of ScareCrow, a famous EDR bypassing tool for C2 agents. The ability to implement your own covert channel and beacon config is a big plus to try and evade network detection. 

Also attempts will be made to evade syscall recording from an amazing tool based on dtrace. The tool is called dgenerate, made by Jonas Lyk: https://github.com/jonaslyk/temp, big love to that danish lad <3

<p align="center">
  <img src="https://user-images.githubusercontent.com/59022605/190503049-a4ba6757-de2d-4b15-ac09-627b6b9297b8.png" data-canonical-src="https://user-images.githubusercontent.com/59022605/190503049-a4ba6757-de2d-4b15-ac09-627b6b9297b8.png" height="600" />
</p>

<p align="center">
Amazing picture made by some dude with Midjourney
</p>

## Features
- Fully CLI, fancy GUI is for plebs and marketing anyways xD
- Made in C 
- Sneaky evasion tech like scarecrow has, because its cool and all that 😎
- Can use direct syscalls to bypass user-land EDR/AV hooking
- Some kind of magic to stop syscalls related to beacon being reported back to user-mode
- Built in covert channels:
  - TCP, HTTP, HTTP2, HTTP3, DNS, ICMP, FTP, IMAP, MAPI, DNS over HTTPS (DoH), SMB and anything you can make yourself.
- Windows agent
  - Might make Linux and OSX agents later
- Ed25519 for the client-server authentication 
- Beacon activity logging
- Custom beacon profiles
- Proxy awareness
- Packing with **Something**, because fuck you thats why


## Readables
- https://adamsvoboda.net/evading-edr-with-scarecrow/
- https://www.youtube.com/watch?v=x4wauJZPnKg&t=286s

## Setup
You either compile or download compiled version

## Server
### Windows
`ExodusC2_server.exe`

## Beacon

## EDR Evasion

### Evading syscall recording dgenerate

## Make your own covert channel

## But's and if's
Not this is no bulletproof one-stop-shop. You could probably find bugs in this PoC, if not many ways to detect this. This is just an effort to see how far I can get trying to evade stuff I know exist. But I dont know everything that exists, so I am relying on community feedback here. Find a way to do it better, say so. Or keep it a secret.... 

Up to you gentlepeople



