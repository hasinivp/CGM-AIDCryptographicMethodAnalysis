from sensor import Sensor
from insulin_pump import InsulinPump
from communication_channel import CommunicationChannel

def main():
    test_sensor = Sensor(json_filepath = "sample_messages.json")
    test_insulin = InsulinPump()
    channel = CommunicationChannel()

    #send cgm public key
    channel.send(test_sensor.return_public_key())
    test_insulin.key_exchange(channel.receive())

    #sent aid public key
    channel.send(test_insulin.return_public_key())
    test_sensor.key_exchange((channel.receive()))

    print("Succesful key exchange")

if __name__ == "__main__":
    main()
