import paho.mqtt.client as mqtt
import random
import time
#######
broker_add="iotdomobeta.cloud.shiftr.io"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set("iotdomobeta","hZREkxrENS6cTeSw")
print("Conectando al broker")
client.connect(broker_add)



##### SENSOR LUMENS
while True:
    temperatura=random.randint(0,100)
    print("temperatura: ", temperatura)
    client.publish("Samir_C/cuartoN1/temperature",temperatura)
    time.sleep(5)
    client.loop()