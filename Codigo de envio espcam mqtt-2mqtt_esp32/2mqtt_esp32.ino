/*
 Basic ESP32 MQTT example
 This sketch demonstrates the capabilities of the pubsub library in combination
 with the ESP8266 board/library.
 It connects to an MQTT server then:
  - publishes "hello world" to the topic "outTopic" every two seconds
  - subscribes to the topic "inTopic", printing out any messages
    it receives. NB - it assumes the received payloads are strings not binary
  - If the first character of the topic "inTopic" is an 1, switch ON the ESP Led,
    else switch it off
 It will reconnect to the server if the connection is lost using a blocking
 reconnect function. See the 'mqtt_reconnect_nonblocking' example for how to
 achieve the same result without blocking the main loop.
 To install the ESP32 board, (using Arduino 1.6.4+):
  - Add the following 3rd party board manager under "File -> Preferences -> Additional Boards Manager URLs":
       http://arduino.esp8266.com/stable/package_esp8266com_index.json
  - Open the "Tools -> Board -> Board Manager" and click install for the ESP32"
  - Select your ESP8266 in "Tools -> Board"

  Ejemplo básico de MQTT para ESP32
Este sketch demuestra las capacidades de la biblioteca "pubsub" en combinación con la placa y biblioteca ESP32. Se conecta a un servidor MQTT y luego realiza las siguientes acciones:
  - Publica "hello world" en el tema "outTopic" cada dos segundos.
  - Se suscribe al tema "inTopic" e imprime cualquier mensaje que reciba. Nota: asume que los datos recibidos son cadenas de texto, no binarios.
  - Si el primer carácter del tema "inTopic" es un 1, enciende el LED del ESP. Si es otro valor, apaga el LED.
  
El programa se volverá a conectar al servidor si la conexión se pierde utilizando una función de reconexión bloqueante. Consulta el ejemplo 'mqtt_reconnect_nonblocking' para ver cómo lograr el mismo resultado sin bloquear el bucle principal.

Para instalar la placa ESP32 (usando Arduino 1.6.4+):
  - Agrega el siguiente enlace del administrador de placas de terceros en "Archivo -> Preferencias -> URLs adicionales del administrador de placas":
       http://arduino.esp8266.com/stable/package_esp8266com_index.json
  - Abre "Herramientas -> Placa -> Administrador de Placas" y haz clic en "Instalar" para ESP8266.
  - Selecciona tu ESP8266 en "Herramientas -> Placa".
*/

#include <WiFi.h>
#include <PubSubClient.h>
#define BUILTIN_LED 2

// Update these with values suitable for your network.

const char* ssid = "xxxxxxxx";
const char* password = "xxxxxxx";
const char* mqtt_server = "broker.emqx.io";

WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE	(50)
char msg[MSG_BUFFER_SIZE];
int value = 0;

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(BUILTIN_LED, LOW);   
    // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is active low on the ESP-01)
  } else {
    digitalWrite(BUILTIN_LED, HIGH);  
    // Turn the LED off by making the voltage HIGH
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("inTopic");
      delay(500);
    }
    
    else{
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay (5000); } 
    

     
    
 
  }
}

void setup() {
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  unsigned long now = millis();
  if (now - lastMsg > 60000) {
    lastMsg = now;
    ++value;
    snprintf (msg, MSG_BUFFER_SIZE, "hello world #%ld", value);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("outTopic", msg);
  }
 

}
