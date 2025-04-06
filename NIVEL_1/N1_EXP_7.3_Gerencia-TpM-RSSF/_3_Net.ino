void Net_initialize() // Função de inicialização da camada de Rede
{
  My_address = 1; // Define o endereço do sensor
  
}

// ====== FUNÇÃO RECEBE PAOCTE DA CAMDA DE REDE
void Net_receive()  // Função de recepção de pacote da Camada de Rede
{
  // Já fez a comparação com o meu endereço antes de começar a desencapsular o pacote.
  // o lugar natural seria aqui.
  
  byte8 = Pacote_RX[8];  // Endereço de Destino
  byte9 = Pacote_RX[9]; // Endereço de Origem    
  byte10 = Pacote_RX[10];
  byte11 = Pacote_RX[11];
  
  if (byte8 == My_address) // Faz uma verificação do endereço de destido antes de começar a desencapsular o pacote (existe crosslayer neste ponto)
     {
      Contador_mac = Contador_mac + 10; // Contador é incrementado em 10 a cada vez que um pacote passa pela função de recepção da Camada MAC
     
      Transp_receive(); //Chama a função de recepção da camada de Transporte
     }
}

// ====== ENVIA PACOTE CAMADA REDE
void Net_send()// Função de envio de pacote da Camada de Rede
{
  Pacote_TX[8] = byte10; // Inverte o endereço de origem e destino, colocando o endereço de origem do pacote recebido como destinatário
  Pacote_TX[9] = Pacote_RX[9];
  Pacote_TX[10] = My_address; // coloca o meu endereço como origem do pacote de TX
  Pacote_TX[11] = Pacote_RX[11];
  
  Mac_send();  //Chama a função de envio da Camada de Acesso ao Meio
}
