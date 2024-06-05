import numpy as np
import pyaudio
import struct
import cv2
import threading

RATE=44100        
bufsize = 32       

#鍵盤のGUI作成
ksx = 800
ksy = 200
keyboard = np.zeros([ksy,ksx,3])
keyboard[:,:,:] = 255
for i in range(15):
    cv2.rectangle(keyboard, (int(ksx/15*i), 0), (int(ksx/15*(i+1)),ksy), (0, 0, 0), 5)
for i in range(15):
    if i in {0,1,3,4,5,7,8,10,11,12}:
        cv2.rectangle(keyboard, (int(ksx/15*i + ksx/27 ), 0), (int(ksx/15*(i+1) + ksx/33),int(ksy/2)), (0, 0, 0), -1)
cv2.namedWindow("keyboard", cv2.WINDOW_NORMAL)

#マウス位置による鍵盤選択
keyon = 0
pitch = 440
highkeys = np.array([0,1,1,3,3,4,5,6,6,8,8,10,10,11, 12,13,13,15,15,16,17,18,18,20,20,22,22,23, 24,24])
lowkeys = np.array([0,2,4,5,7,9,11, 12,14,16,17,19,21,23, 24])
def mouse_event(event, x, y, flags, param):
    global keyon,pitch
    if event == cv2.EVENT_LBUTTONDOWN:
        keyon = 1
        if y >= ksy/2:
            note = lowkeys[int(15.0*x/ksx)]
        elif y < ksy/2:
            note = highkeys[int(30.0*x/ksx)]
        pitch = 440*(np.power(2,(note-9)/12))
    elif event == cv2.EVENT_LBUTTONUP :
        keyon = 0
cv2.setMouseCallback("keyboard", mouse_event)

#波形生成
x=np.arange(bufsize)
pos = 0
def synthesize():
    global pos
    #位相計算
    t = pitch * (x+pos) / RATE
    t = t - np.trunc(t)
    pos += bufsize

    wave = np.sin(2.0*np.pi*t)

    if keyon == 1:
        velosity = 1.0
    else:
        velosity = 0.0
    wave = velosity * wave

    return wave


#波形再生
playing = 1
def audioplay():
    print ("Start Streaming")
    p=pyaudio.PyAudio()
    stream=p.open(format = pyaudio.paInt16,
            channels = 1,
            rate = RATE,
            frames_per_buffer = bufsize,
            output = True)
    while stream.is_active():
        buf = synthesize()

        buf = (buf * 32768.0).astype(np.int16)#16ビット整数に変換
        buf = struct.pack("h" * len(buf), *buf)
        stream.write(buf)
        if playing == 0:
            break
    stream.stop_stream()
    stream.close()
    p.terminate()
    print ("Stop Streaming")

#画面描画
if __name__ == "__main__": 
    thread = threading.Thread(target=audioplay)
    thread.start()
    while (True):
        cv2.imshow("keyboard", keyboard) 
        k = cv2.waitKey(100) & 0xFF
        if k == ord('q'):
            playing = 0
            break

    cv2.destroyAllWindows()