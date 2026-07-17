#Mediates communication between CGM/AID data

class CommunicationChannel:
    def _init_(self):
        self.packet = None

    def send(self, packet):
        self.packet = packet

    def receive(self):
        packet = self.packet
        self.packet = None
        return packet
