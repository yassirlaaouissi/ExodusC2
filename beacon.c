#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <rpcdce.h>

#pragma comment(lib, "ws2_32.lib")
#pragma comment(lib, "rpcrt4.lib")




void beacon_connect_to_server(char IP[16], int PORT){
    // INIT SOCKET = AF_INET (IPv4), SOCK_STREAM (Stream), IPPROTO_TCP (TCP)
    SOCKET s =  socket(AF_INET, SOCK_STREAM, IPPROTO_TCP); 
    
    // IP+PORT SPEC
    int iResult;
    int jResult;
    struct sockaddr_in clientService;
    clientService.sin_family = AF_INET;
    clientService.sin_addr.s_addr = inet_addr(IP);
    clientService.sin_port = htons(PORT);

    // Connect to server.
    iResult = connect(s, (SOCKADDR *) & clientService, sizeof (clientService));
    printf("%d", iResult);


    // Generate and send beacon metadata     
    //// Generate UUID
    int recvbuflen = 2048;
    UUID uuid;
    UuidCreate(&uuid);
    char stringified_UUID[128];
    UuidToString(&uuid, (RPC_CSTR*) stringified_UUID);
    char *sendbuf = stringified_UUID;
    char recvbuf[recvbuflen];

    //// Send metadata
    send(s, sendbuf, (int)strlen(sendbuf), 0); 
  
    
    
    // Receive until the peer closes the connection
    do {
        iResult = recv(s, recvbuf, recvbuflen, 0);
    } while( iResult > 0 );
    
    
    
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
        void beacon_connect_back(char IP[16], int PORT);
    }
    else if( argc > 3 ) {
        printf("Too many arguments supplied.\n");
    }
    else {
        printf("Two argument expected.\n");
    }
    return 0;
}