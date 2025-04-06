#ifndef _BIBLIOTECAS_H  // As duas primeiras linhas servem como forma de proteção do arquivo de Headers
#define _BIBLIOTECAS_H  // As duas primeiras linhas servem como forma de proteção do arquivo de Headers
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
WiFiUDP Udp;

// ====== Variável pra exibição periódica dos IP
unsigned long tempo_ip;

// ====== Cria buffer de leitura do Socket
char packetBuffer[UDP_TX_PACKET_MAX_SIZE + 1]; // Buffer de leitura do socket
// ====== Cria pacote de recepção de 52 bytes  
byte Pacote_RX[52]; // Pacote de recepção (array de 52 bytes)
// ====== Cria pacote de transmissão de 52 bytes
byte Pacote_TX[52]; // Pacote de transmissão (array de 52 bytes)

// ======= DEFINIÇÃO DOS BYTES PARA RECEBER E ENVIAR PACOTES
// Bytes da camada Física
int byte0,byte1,byte2,byte3;
// Bytes da camada MAC
int byte4,byte5,byte6,byte7;
// Bytes da camada de rede
int byte8,byte9,byte10,byte11;
// Bytes da camada de transporte
int byte12,byte13,byte14,byte15;

// ====== Variáveis da camada física
bool TX_ledblink = true; // Variável booleana para determinar se o led vermelho deve piscar na recepção
bool RX_ledblink = true; // Variável booleana para determinar se o led verde deve piscar na transmissão
int RSSI_dl;  // RSSI de DownLink
int LQI_dl;   // LQI de DownLink
int RSSI_ul;  // RSSI de UpLink
int LQI_ul;   // LQI de UpLink
float RSSI_dBm_dl;  //RSSI de Downlink em dBm
float RSSI_dBm_ul;  //RSSI de Uplink em dBm

// ====== Variáveis da camada de acesso ao meio
int Contador_mac; // Contador da Camada MAC

// ====== Variáveis da camada de rede
byte My_address;  // Meu endereço
byte Orig_address; // Endereço de Origem
byte Dest_address;  // Endereço de destino

// ======= Variáveis da camada de Transporte
int pkt_counter_up;  // Contador de pacotes transmitido pelo sensor
int pkt_counter_down; // Contador de pacotes recebidos pelo sensor

// ====== Variáveis da camada de aplicação
// Bytes da camada de aplicação transmissão
// ADC 0
int byte16,byte17,byte18;
// ADC 1
int byte19,byte20,byte21;
// ADC 2
int byte22,byte23,byte24;
// ADC 3
int byte25,byte26,byte27;
// ADC 4
int byte28,byte29,byte30;
// ADC 5
int byte31,byte32,byte33;
// DIGITAL 0
int byte34,byte35,byte36;

// VARIÁVEL LUMINOSIDADE
int luminosidade;

// DIGITAL 1
int byte37,byte38,byte39;
// DIGITAL 2
int byte40,byte41,byte42;
// DIGITAL 3
int byte43,byte44,byte45;
// DIGITAL 4
int byte46,byte47,byte48;
// DIGITAL 5
int byte49,byte50,byte51;

#define LED_verde D4  // Define que o Led verde está no Pino D1 da PK2
#define LED_amarelo D7  // Define que o Led amarelo está no Pino D2 da PK2
#define LED_vermelho D3 // Define que o Led vermelho está no Pino d3 da PK2
#define Buzzer D5 // Define buzzer no Pino D5 da PK1


byte LED_verde_status;  // Status do LED Verde
byte LED_amarelo_status;  // Status do LED Amarelo
byte LED_vermelho_status; // Status do LED Vermelho


#endif  // _BIBLIOTECAS_H

/*
SIGNIFICADO DOS BYTES DO PACOTE DE DESCIDA
byte0
byte1
byte2
byte3
byte4
byte5
byte6
byte7
byte8
byte9
byte10
byte11
byte12
byte13
byte14
byte15
byte16
byte17
byte18
byte19
byte20
byte21
byte22
byte23
byte24
byte25
byte25
byte26
byte27
byte28
byte29
byte30
byte31
byte32
byte33
byte34
byte35
byte36
byte37
byte38
byte39
byte41
byte42
byte43
byte44
byte45
byte46
byte47
byte49
byte49
byte50
byte51
 */
