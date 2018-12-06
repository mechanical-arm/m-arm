import logging, turtle

class Motor:
    def __init__(self, id):
        logging.info("motor %d connected" %id)
        self.id = id
        self.speed = 0
        self.name = "motor:"+str(id)

    def setSpeed(self, speed):
        logging.info("motor %d setSpeed: %d" %(self.id,speed))
        self.speed = speed

class Input:
    def __init__(self, id):
        logging.info("input %d connected" %id)
        self.id = id
        self.pressed = False
        self.name = "input:"+str(id)

    def state(self):
        return self.pressed

class Ultrasonic:
    def __init__(self, id):
        logging.info("ultrasonic %d connected" %id)
        self.id = id
        self.name = "ultrasonic:"+str(id)
        self._distance = 40

    def distance(self):
        return self._distance

class ftrobopy:
    def __init__(self,mode,port=65000):
        logging.basicConfig(level=logging.CRITICAL)
        logging.info("connection txt completed")
        self.d = dict()
        self._camera = False

    def play_sound(self, sound, repeat):
        for i in range(repeat):
            print("play sound %d" %sound)


    def cameraIsOnline(self):
        return self._camera

    def startCameraOnline(self):
        self._camera = True

    def getCameraFrame(self):
        return "frame, emulated"


    def motor(self, id):
        m = Motor(id)
        self.d[m.name] = m
        return m

    def input(self, id):
        i = Input(id)
        self.d[i.name] = i
        return i

    def ultrasonic(self, id):
        u = Ultrasonic(id)
        self.d[u.name] = u
        return u
