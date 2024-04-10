import paho.mqtt.client as mqtt
import random
import time
#######
broker_add="iotdomobeta.cloud.shiftr.io"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set("iotdomobeta","hZREkxrENS6cTeSw")
print("Conectando al broker")
client.connect(broker_add)


lat=10.3928525
long=-75.4623964

##### SENSOR GPS
while True:
    location=str(lat)+":"+str(long)
    client.publish("Samir_C/cuartoN1/Location",location,qos=0,retain=False)
    time.sleep(5)
    lat=lat+0.0001
    long=long+0.001
    client.loop()