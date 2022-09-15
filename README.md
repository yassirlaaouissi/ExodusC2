# ExodusC2
This Command and Control PoC is made to cross the red sea of blue teaming solutions. ExodusC2 is not to be confused with the mobile malware strain called Exodus, and no I am not christian though I like the biblical reference. Operating from a client-server model, from kernel mode on the victim it evades at least most commercial EDR solutions. The ability to implement your own covert channel is a big plus to try and evade network detection.

<p align="center">
  <img src="https://user-images.githubusercontent.com/59022605/190503049-a4ba6757-de2d-4b15-ac09-627b6b9297b8.png" data-canonical-src="https://user-images.githubusercontent.com/59022605/190503049-a4ba6757-de2d-4b15-ac09-627b6b9297b8.png" height="600" />
</p>

<p align="center">
Amazing picture made by some dude with Midjourney
</p>

## Features
- Fully CLI, fancy GUI is for plebs and marketing anyways xD
- Made in C
- Kernel mode beacons 
- Built in covert channels:
  - TCP, HTTP, HTTP2, HTTP3, DNS, ICMP, FTP, IMAP, MAPI, DNS over HTTPS (DoH), SMB and anything you can make yourself.
- Windows and Linux agent
- Ed25519 for the client-server authentication 
- Beacon activity logging
- Custom profiles on serverside, including stuff like jitter
- Proxy awareness


## Setup

## Make your own covert channel

## But's and if's
Not this is no bulletproof one-stop-shop. You could probably find bugs in this PoC, if not many ways to detect this. This is just an effort to see how far I can get trying to evade stuff I know exist. But I dont know everything that exists, so I am relying on community feedback here. Find a way to do it better, say so. Or keep it a secret.... 

Up to you gentlepeople



