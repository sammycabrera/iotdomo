import paho.mqtt.client as mqtt
import random
import time
#######
broker_add="eiaiot1scm.cloud.shiftr.io"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set("eiaiot1scm","so8rVCM9TdkZjY0Q")
print("Conectando al broker")
client.connect(broker_add)



##### SENSOR LUMENS
while True:
    lumens=random.randint(0,100)
    print("Lumens: ", lumens)
    client.publish("Samir_C/cuartoN1/lumens",lumens)
    time.sleep(5)
    client.loop()

