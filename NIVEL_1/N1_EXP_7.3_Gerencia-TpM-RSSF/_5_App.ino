void App_initialize() // Função de inicialização da camada de Aplicação
{

  pinMode(LED_verde,OUTPUT);  // Define o pino do LED Verde como saída
  pinMode(LED_amarelo,OUTPUT);  // Define o pino do LED Amarelo como saída
  pinMode(LED_vermelho,OUTPUT); // Define o pino do LED Vermelho como saída
  pinMode(Buzzer,OUTPUT); // Define o pino do Buzzer como saída
  pinMode(A0,INPUT);
}

void App_receive()
{
  //======== RECEBE BYTES DE ACIONAMENTOS
  // === DIGITAL 0 - aciona LED verde
  byte34 = Pacote_RX[34]; // Retira do Pacote o Status do LED verde
  // == Ajusta o estado do algoritmo de piscagem do LED Verde
  
  digitalWrite(LED_verde , byte34);    // Liga ou desliga o LED verde de acordo com o status
  byte35 = Pacote_RX[35];
  byte36 = Pacote_RX[36];
  // === DIGITAL 1 - aciona LED amarelo
  byte37 = Pacote_RX[37];
  digitalWrite(LED_amarelo , byte37);    // Liga ou desliga o LED Amarelo de acordo com o status  
  byte38 = Pacote_RX[38];
  byte39 = Pacote_RX[39];
  // === DIGITAL 2 - aciona LED vermelho
  byte40 = Pacote_RX[40]; // Retira do Pacote o Status do LED vermelho
  // == Ajusta o estado do algoritmo de piscagem do LED Vermelho
  if(byte40){
    RX_ledblink = false;  //Configura o módulo para não piscar o LED vermelho quando recebe pacote na serial
  }
  else{
    RX_ledblink = true;  //Configura o módulo para piscar o LED vermelho quando recebe pacote na serial
  }  
  digitalWrite(LED_vermelho , byte40);    // Liga ou desliga o LED vermelho de acordo com o status
  
  // === Função que chama a camada de aplicação para transmissão
  App_send(); // Chama a função de envio da Camada de Aplicação
}

void App_send() // Função de envio da Camada de Aplicação
{
  luminosidade = analogRead(A0);

  Pacote_TX [17] =  (byte) (luminosidade/256); // Valor inteiro no byte 17
  Pacote_TX [18] =  (byte) (luminosidade%256); // Valor resto no byte 18
  
  // =================== PACOTE TX APLICAÇÃO STATUS
  // DIGITAL 0 - pacote der transmissão
  Pacote_TX [34] = byte34; // Primeiro campo de payload recebe o Status do LED verde
  Pacote_TX [35] = byte35;  
  Pacote_TX [36] = byte34;
  // DIGITAL 1 - pacote der transmissão
  Pacote_TX [37] = byte37; // Primeiro campo de payload recebe o Status do LED verde
  Pacote_TX [38] = byte38;  
  Pacote_TX [39] = byte39;
  // DIGITAL 2 - pacote der transmissão
  Pacote_TX [40] = byte40; // Primeiro campo de payload recebe o Status do LED verde
  Pacote_TX [41] = byte41;  
  Pacote_TX [42] = byte42;
  // DIGITAL 3 - pacote der transmissão
  Pacote_TX [43] = byte43; // Primeiro campo de payload recebe o Status do LED verde
  Pacote_TX [44] = byte44;  
  Pacote_TX [45] = byte45;  
  // DIGITAL 4 - pacote der transmissão
  Pacote_TX [46] = byte46; // Primeiro campo de payload recebe o Status do LED verde
  Pacote_TX [47] = byte47;  
  Pacote_TX [48] = byte48;  
  // DIGITAL 5 - pacote der transmissão
  Pacote_TX [49] = byte49; // Primeiro campo de payload recebe o Status do LED verde
  Pacote_TX [50] = byte50;  
  Pacote_TX [51] = byte51;  

  Transp_send(); //Chama a função de envio da Camada de Transporte
}
