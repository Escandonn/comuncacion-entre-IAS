class Agente:
    def __init__(self, nombre, rol, client):
        self.nombre = nombre
        self.rol = rol
        self.client = client

    def responder(self, mensaje):
        return self.client.chat(self.rol, mensaje)