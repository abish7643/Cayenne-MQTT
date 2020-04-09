import cayenne.client
import time
import sys
import Adafruit_DHT
import time
# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = ""
MQTT_PASSWORD  = ""
MQTT_CLIENT_ID = ""

# The callback for when a message is received from Cayenne.
def on_message(message):
  print("message received: " + str(message))
  # If there is an error processing the message return an error string, otherwise return nothing.

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883)

i=0
timestamp = 0

while True:
  client.loop()
  #if (time.time() > timestamp):
  humidity, temperature = Adafruit_DHT.read_retry(11, 4)
  #print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
  time.sleep(1)
  client.celsiusWrite(1, temperature)
  client.celsiusWrite(3, humidity)
    #client.percentWrite(2, i*10)
    #client.hectoPascalWrite(3, i+800)
    #timestamp = time.time()
    #i = i+1
