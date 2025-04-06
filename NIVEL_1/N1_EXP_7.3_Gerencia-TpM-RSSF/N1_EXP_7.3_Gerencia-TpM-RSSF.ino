
#include "Bibliotecas.h"

#ifndef STASSID

//+++++++COLOCAR A REDE WiFi QUE SERÁ UTILIZADA COM SSID E PASSWORD

#define ssid "ENGENHARIA"
#define password "29297139"
#endif
unsigned int localPort = 8888;     // Porta na qual o servidor ficará escutando
String newHostname = "SENSOR001";  // Nome do Host na rede

void setup() {
  Phy_initialize();     // Inicializa a camada Física
  Mac_initialize();     // Inicializa a camada de Controle de Acesso ao Meio
  Net_initialize();     // Inicializa a camada de Rede
  Transp_initialize();  // Inicializa a camada de Transporte
  App_initialize();     // Inicializa a camada de Aplicação
}

void loop() {
  Phy_receive();
}
