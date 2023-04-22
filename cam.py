import cv as cv2
import urllib.request

url = "http://192.168.1.10:81/stream1"
stream = urllib.request.urlopen(url)

while True:
    bytes = b''
    while True:
        bytes += stream.read(1024)
        a = bytes.find(b'\xff\xd8')
        b = bytes.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes[a:b+2]
            bytes = bytes[b+2:]
            frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            cv2.imshow('ESP32-CAM Video Stream', frame)
            if cv2.waitKey(1) == 27:
                exit(0)