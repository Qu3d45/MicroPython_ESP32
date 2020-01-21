import config_lora
from sx127x import SX127x
from controller_esp32 import ESP32Controller

from ssd1306_i2c import Display


def receive(lora):
    print("LoRa Receiver")

    display = Display()

    while True:
        ident = "LoRa Receiver"

        lora.receivedPacket()

        lora.blink_led()

        try:
            payload = lora.read_payload()

            display.show_text_wrap("{0}                   {1}                   RSSI: {2}".format(
                ident, payload.decode(), lora.packetRssi()), 2)
            #print("*** Received message ***\n{}".format(payload.decode()))

        except Exception as e:
            print(e)
        #display.show_text("RSSI: {}\n".format(lora.packetRssi()), 10, 10)
        #print("with RSSI: {}\n".format(lora.packetRssi))


controller = ESP32Controller()
lora = controller.add_transceiver(SX127x(name='LoRa'),
                                  pin_id_ss=ESP32Controller.PIN_ID_FOR_LORA_SS,
                                  pin_id_RxDone=ESP32Controller.PIN_ID_FOR_LORA_DIO0)

receive(lora)
