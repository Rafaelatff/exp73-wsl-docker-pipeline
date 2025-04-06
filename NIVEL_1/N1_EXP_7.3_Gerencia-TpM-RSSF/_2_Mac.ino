void Mac_initialize()  // Função de inicialização da camada de Acesso ao Meio
{
  Contador_mac = 0;  //Inicializa o contador da MAC
}

//================ RECEBE O PACOTE DA CAMADA FÍSICA
void Mac_receive() {  // Função de recepção de pacote da Camada MAC

  //================ SUBIDA DO PACOTE PARA CAMDA DE REDE
  byte4 = Pacote_RX[4];  // Retira a informação da RSSI de Downlink do pacote recebido
  byte5 = Pacote_RX[5];
  byte6 = Pacote_RX[6];
  byte7 = Pacote_RX[7];


  Net_receive();  // chama a função de recepção da camada de Rede
}

//================
void Mac_send()  // Função de envio de pacote da Camada MAC
{

  Pacote_TX[4] = Contador_mac / 256;  //Byte 0 do cabeçalho de Transporte recebe o byte mais significativo do contador de pacotes (divisão intieira por 256)
  Pacote_TX[5] = Contador_mac % 256;  //Byte 1 do cabeçalho de Transporte recebe o byte menos significativo do contador de pacotes  (Resto da divisão por 256)
  Pacote_TX[6] = Pacote_RX[6];
  Pacote_TX[7] = Pacote_RX[7];

  if (Pacote_TX[34] == 1) {
    Phy_send();  //Chama a função de envio da Camada Física
  }
}
