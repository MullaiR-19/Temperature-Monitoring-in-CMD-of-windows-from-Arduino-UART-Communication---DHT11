import time
import serial
import keyboard as kb
import os
import winsound

fz = 440
        
def TempHum():
        print('\nPress and Hold "q" to exit!')
        time.sleep(2)
        os.system('color f0')
        while 1:
                time.sleep(2)
                os.system('cls')
                os.system('color f0')
                data = ser.readline()
                my_data = data.decode()
                 
                t_h = [int(i) for i in my_data.split() if i.isdigit()]
                print('Temperature: ',t_h[0],'ºC',"  Humidity: ",t_h[1],'%')
                if(t_h[0]>36 and t_h[0]!=255):
                        os.system('color CF')
                        print('High Temperature Dected!')
                        for i in range(5):
                                winsound.Beep(fz, 500)
                else:
                        os.system('color f0')
                        print('Normal Temperature!')
                if(t_h[1]<45):
                        os.system('color B0')
                        print('Low Humidity!!\nFill Tank now') 
                        for i in range(3):
                                winsound.Beep(fz, 200)
                                winsound.Beep(fz, 500)
                elif(t_h[1]>85 and t_h[0]!=255):
                        print('High Humidity')
                        winsound.Beep(fz, 2000)                        
                else:
                        os.system('color f0')
                        print('Normal Humidity')
                if kb.is_pressed('q'):
                        ser.close()
                        break
    
def Error():
        ser.close()
        print('COM Port 6 Error')


print('Temperature and Humidity Monitor')
'''print('Starting')
for i in range (12):
        time.sleep(0.2)
        print('.',end='')
print('')'''

if __name__ == "__main__":       
        try:
                ser = serial.Serial('COM6', 115200, timeout=1)
                print('\nCOM Port 6 Connected.....')
                TempHum()
        except:
                Error()
