#python generator_device_1.py
#subscribe_device_all.py
import paho.mqtt.client as mqtt
import random
import time
#######
broker_add="eiaiot1scm.cloud.shiftr.io"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set("eiaiot1scm","so8rVCM9TdkZjY0Q")
print("Conectando al broker")
client.connect(broker_add)



##### SUBSCRIBER CODE
def on_message(client, userdata, message):
    print("Lummens receiver: ", str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)


client.subscribe("#")
client.on_message=on_message
client.loop_forever()