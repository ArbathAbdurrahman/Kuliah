#include <ESP8266WiFi.h>
#include <UniversalTelegramBot.h>

#define WIFI_SSID "YourWiFiSSID"
#define WIFI_PASSWORD "YourWiFiPassword"
#define BOT_TOKEN "YourBotToken"

WiFiClientSecure client;
UniversalTelegramBot bot(BOT_TOKEN, client);

const int relay1Pin = D1;
const int relay2Pin = D2;
const int relay3Pin = D3;
const int relay4Pin = D4;

void setup() {
  pinMode(relay1Pin, OUTPUT);
  pinMode(relay2Pin, OUTPUT);
  pinMode(relay3Pin, OUTPUT);
  pinMode(relay4Pin, OUTPUT);

  Serial.begin(115200);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
    delay(2000);
    checkMessages() {
    if (bot.getUpdates(bot.last_message_received + 1)) {
        for (int i = 0; i < bot.updateCount(); i++) {
        String chat_id = String(bot.messages[i].chat_id);
        String text = bot.messages[i].text;

        if (text == "/relay1on") {
            digitalWrite(relay1Pin, HIGH);
            bot.sendMessage(chat_id, "Relay 1 turned ON");
        } else if (text == "/relay1off") {
            digitalWrite(relay1Pin, LOW);
            bot.sendMessage(chat_id, "Relay 1 turned OFF");
        } else if (text == "/relay2on") {
            digitalWrite(relay2Pin, HIGH);
            bot.sendMessage(chat_id, "Relay 2 turned ON");
        } else if (text == "/relay2off") {
            digitalWrite(relay2Pin, LOW);
            bot.sendMessage(chat_id, "Relay 2 turned OFF");
        } else if (text == "/relay3on") {
            digitalWrite(relay3Pin, HIGH);
            bot.sendMessage(chat_id, "Relay 3 turned ON");
        } else if (text == "/relay3off") {
            digitalWrite(relay3Pin, LOW);
            bot.sendMessage(chat_id, "Relay 3 turned OFF");
        } else if (text == "/relay4on") {
            digitalWrite(relay4Pin, HIGH);
            bot.sendMessage(chat_id, "Relay 4 turned ON");
        } else if (text == "/relay4off") {
            digitalWrite(relay4Pin, LOW);
            bot.sendMessage(chat_id, "Relay 4 turned OFF");
        }
        }
    }
  }
}

 if(lele.getNewMessage(pesan)){
    Serial.print("Ada pesan Masuk : ");
    Serial.println(pesan.text);
    if(pesan.text.equalsIgnoreCase("ONR1")){
      digitalWrite(relay1,HIGH);
      lele.sendMessage(pesan.sender.id,"Relay 1 Menyala");
    }
    else if(pesan.text.equalsIgnoreCase("OFFR1")){
      digitalWrite(relay1,LOW);
      lele.sendMessage(pesan.sender.id,"Relay 1 Padam");
    }
    else if(pesan.text.equalsIgnoreCase("ONR2")){
      digitalWrite(relay2,HIGH);
      lele.sendMessage(pesan.sender.id,"Relay 2 Menyala");
    }
    else if(pesan.text.equalsIgnoreCase("OFFR2")){
      digitalWrite(relay2,LOW);
      lele.sendMessage(pesan.sender.id,"Relay 2 Padam");
    }
 
    else if(pesan.text.equalsIgnoreCase("STATUS")){
      String status = String(srelay1 + srelay2);
      lele.sendMessage(pesan.sender.id,status);
    }
    else{
      String balas;
      balas="Maaf, perintahnya salah. Coba kirim ONR,OFFR,STATUS.";
      lele.sendMessage(pesan.sender.id,balas);
    }


#include "CTBot.h"
#include "Arduino.h"

TaskHandle_t Task1;

CTBot Arham;
const int relay1 = 18;
const int relay2 = 19;

void Task1code( void * Parameters ) {
  // infinite Loop
  for(;;) {
    digitalWrite(relay2, HIGH);  // Hidupkan Relay 2
    vTaskDelay(12 * 3600 * 1000 / portTICK_PERIOD_MS);  // Nyalakan Dinamo selama 2 detik
    digitalWrite(relay2, LOW);   // Matikan Relay 2
    vTaskDelay(12 * 3600 * 1000 / portTICK_PERIOD_MS);  // Matikan Dinamo Selama 4 jam - 2 detik
  }
}
void setup() {
  // Inisialisasi FreeRTOS
  xTaskCreatePinnedToCore(
    Task1code,   // Fungsi yang akan dijalankan oleh task
    "Task1",    // Nama task
    10000,       // Ukuran stack untuk task
    NULL,        // Parameter untuk task
    1,           // Prioritas task
    &Task1,     // Handle untuk task
    1);          /* pin task to core 1 */  
  Serial.begin(115200)
}
// Setting Relay NC 
  pinMode(relay1, OUTPUT); // Atur pin sebagai output relay 1
  digitalWrite(relay1,LOW);
  pinMode(relay2, OUTPUT); // Atur pin sebagai output relay 2
  digitalWrite(relay2,LOW);
  lele.wifiConnect("arhmath", "arham130404");
  lele.setTelegramToken("7211388867:AAEXoET-h5cAt4hIJ5STPg5Lh63QDgBH5lU");

void loop(){
  String srelay1 = String("Relay 1 = EROR\n");
  String srelay2 = String("Relay 2 = EROR\n");

  if (digitalRead(relay1) == HIGH ){
      srelay1 = "Lampu 1 Menyala\n";
  }
  else{
    srelay1 = "Lampu 1 Mati\n";
  }
  if (digitalRead(relay2) == HIGH ){
      srelay2 = "Lampu 2 Menyala\n";
  }
  else{
    srelay2 = "Lampu 2 Mati\n";
  }

  TBMessage pesan;
  if(arham.getNewMessage(pesan)){
    Serial.print("Ada pesan Masuk : ");
    Serial.println(pesan.text);
    if(pesan.text.equalsIgnoreCase("ONR1")){
      digitalWrite(relay1,HIGH);
      arham.sendMessage(pesan.sender.id,"Relay 1 Menyala");
    }
    else if(pesan.text.equalsIgnoreCase("OFFR1")){
      digitalWrite(relay1,LOW);
      arham.sendMessage(pesan.sender.id,"Relay 1 Padam");
    }
    else if(pesan.text.equalsIgnoreCase("ONR2")){
      digitalWrite(relay2,HIGH);
      arham.sendMessage(pesan.sender.id,"Relay 2 Menyala");
    }
    else if(pesan.text.equalsIgnoreCase("OFFR2")){
      digitalWrite(relay2,LOW);
      arham.sendMessage(pesan.sender.id,"Relay 2 Padam");
    }
 
    else if(pesan.text.equalsIgnoreCase("STATUS")){
      String status = String(srelay1 + srelay2);
      arham.sendMessage(pesan.sender.id,status);
    }
    else{
      String balas;
      balas="Maaf, perintahnya salah. Coba kirim ONR,OFFR,STATUS.";
      arham.sendMessage(pesan.sender.id,balas);
    }
}