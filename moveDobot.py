import DobotDllType as dType
from DobotDllType import PTPMode, JC, DobotConnect

api = dType.load()

ret = dType.ConnectDobot(api, "", 115200)[0]
if not ret == DobotConnect.DobotConnect_NoError:
    print("Could not connect to DOBOT")
    exit()

dType.SetCmdTimeout(api, 3000)
dType.SetQueuedCmdClear(api)
dType.SetQueuedCmdStartExec(api)

deviceName = "DOBOT Magician"
dType.SetDeviceName(api, deviceName)

dType.SetJOGJointParams(api, 50, 50, 50, 50, 50, 50, 50, 50, True)
dType.SetJOGCoordinateParams(api, 50, 50, 50, 50, 50, 50, 50, 50, True)
dType.SetJOGCommonParams(api, 100, 100, True)
dType.SetPTPJointParams(api, 100, 100, 100, 100, 100, 100, 100, 100, True)
dType.SetPTPCoordinateParams(api, 255, 255, 255, 255, True)
dType.SetPTPJumpParams(api, 20, 100, True)
dType.SetPTPCommonParams(api, 30, 30, True)
dType.SetHOMEParams(api, 200, 0, 0, 0, True) #ホームのx,y,z, joint4の角度


while(True):
    mode = input("Please choose mode['q' is quiting operation]: ")

    if mode == 'm': #サーボモーターを試しで動かす
        dType.SetIOMultiplexingEx(api, 7, 2, 1)
        dType.SetIOPWMEx(api,8 , 50, 7, 1)

    if mode == 'h':
        dType.SetHOMECmdEx(api, 0, True)#ホームポジションに復帰

    if mode == 'c':
        dType.SetPTPCmdEx(api, PTPMode.PTPMOVLXYZMode, 200, 100, 0, 0, True)#PTPで移動先のx,y,z, joint4の角度

    if mode == '1':
        dType.SetPTPCmdEx(api, PTPMode.PTPMOVLXYZMode, 200, 100, 0, 0, True)#PTPで移動先のx,y,z, joint4の角度

    if mode == '2':
        dType.SetPTPCmdEx(api, PTPMode.PTPMOVLXYZMode, 0, 200, 100, 0, True)#PTPで移動先のx,y,z, joint4の角度

    if mode == '3':
        dType.SetPTPCmdEx(api, PTPMode.PTPMOVLXYZMode, 100, 0, 200, 0, True)#PTPで移動先のx,y,z, joint4の角度

    if mode == 'a':
        dType.SetJOGCmd(api, False, JC.JogAPPressed, True)
        dType.dSleep(100)
    
    if mode == 'd':
        dType.SetJOGCmd(api, False, JC.JogANPressed, True)
        dType.dSleep(100)
    
    if mode == 'w':
        dType.SetJOGCmd(api, False, JC.JogBPPressed, True)
        dType.dSleep(100)
    
    if mode == 's':
        dType.SetJOGCmd(api, False, JC.JogBNPressed, True)
        dType.dSleep(100)

    if mode == 'z':
        dType.SetJOGCmd(api, False, JC.JogANPressed, True)
        dType.dSleep(100)

    if mode == 'q':
        break

dType.SetQueuedCmdStopExec(api)
dType.DisconnectDobot(api)



'''dType.SetHOMECmdEx(api, 0, True)#ホームポジションに復帰
dType.SetPTPCmdEx(api, PTPMode.PTPMOVLXYZMode, 200, 100, 0, 0, True)#PTPで移動先のx,y,z, joint4の角度
dType.setJOGCmd(api, False, JC.JogAPPressed, True) #x方向に増加
dType.setJOGCmd(api, False, JC.JogANPressed, True) #x方向に減少
dType.setJOGCmd(api, False, JC.JogBPPressed, True) #y方向に増加
dType.setJOGCmd(api, False, JC.JogBNPressed, True) #y方向に減少
dType.setJOGCmd(api, False, JC.JogCPPressed, True) #z方向に増加
dType.setJOGCmd(api, False, JC.JogCNPressed, True) #z方向に減少
dType.setJOGCmd(api, False, JC.JogDPPressed, True) #R方向に増加
dType.setJOGCmd(api, False, JC.JogDNPressed, True) #R方向に減少
dType.SetIOMultiplexingEx(api, IOポート, 出力形式, isQueued)
dType.SetIOPWMEx(api, IOポート, PWM周波数, デューティ比, isQueued)
'''
