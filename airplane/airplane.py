"""code goes here"""

class AirPlane:

    def __init__(self, type, model):
        self.__type = type
        self.__model = model
        self.__kph = 0

    # Metodo getter
    @property
    def type(self):
        return self.__type

    @property
    def model(self):
        return self.__model

    def speed_up(self, kph):
        self.__kph += kph
        return "Airplane has accelerated " + str(self.__kph) + " kph."

    def brake(self, value): #******************
        if self.__kph != 0:
            self.__kph -= value
        # if self.__kph == 0:
        #     return "Airplane has decelerated " + str(value) + " kph."
        # else: # != de 0
        #     self.__kph -= value
        return "Airplane has decelerated " + str(value) + " kph."

    def shut_down(self):
        self.__kph
        return "Let's shut down to " + str(self.__kph) + "!"

    def current_speed(self): # Argumento posicional requerido ??
        return "Airplane goes " + str(self.__kph) + " kph."
