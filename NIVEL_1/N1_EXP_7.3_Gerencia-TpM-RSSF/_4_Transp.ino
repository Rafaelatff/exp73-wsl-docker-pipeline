int contador_temporario = 0;

void Transp_initialize()  // Função de inicialização da camada de Transporte
{
  pkt_counter_up= 0; //Inicializa o contador de pacotes 
}

void Transp_receive()   // Função de recepção de pacote da Camada de Transporte
{
  byte12 = Pacote_RX[12];
  byte13 = Pacote_RX[13];
  byte14 = Pacote_RX[14];
  byte15 = Pacote_RX[15];
  contador_temporario++;
  // if(contador_temporario > 250 && contador_temporario <= 260) return;
  // if(byte13 > 10 && byte13 <= 20) return;
  App_receive();//Chama a função de recepção da camada de Aplicação
}

void Transp_send()// Função de envio de pacote da Camada de Transporte
{ 
  pkt_counter_up = pkt_counter_up +1;
  byte14 = pkt_counter_up/256;  // MSB do contador de pacotes
  byte15 = pkt_counter_up%256;  // LSB do contador de pacotes
  Pacote_TX[12] = byte12;  //Byte 0 do cabeçalho de Transporte recebe o byte mais significativo do contador de pacotes (divisão intieira por 256)
  Pacote_TX[13] = byte13;  //Byte 1 do cabeçalho de Transporte recebe o byte menos significativo do contador de pacotes  (Resto da divisão por 256)
  Pacote_TX[14] = byte14;
  Pacote_TX[15] = byte15;
  // if(contador_temporario > 260 && contador_temporario <= 270) return;
  // if (byte13 > 60 && byte13<=70) return;
  
  Net_send();  //Chama a função de envio da Camada de Rede
}
