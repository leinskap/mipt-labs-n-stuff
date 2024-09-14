import jetFunctions as jet
import matplotlib.pyplot as plt


########################################
# Run this script, enter h for help
# and moove the Pitot tube manually.
########################################


try:


    jet.initStepMotorGpio()




    n = 900
    #steps = 
    st = 1
    data = []
    jet.initSpiAdc()
    f = open("data_70.txt", 'w')
    for i in range(n):
        if i >= 100:
            cur_data = jet.getAdc()
            data.append(cur_data)
            
            print(cur_data)
        jet.stepBackward(st)

    data = data[::8]

    for x in data:
        f.write(str(x)+'\n')

    f.close()
    #plt.plot(data)
    #plt.show()
    jet.stepForward(n)





            

finally:
    jet.deinitStepMotorGpio()
    jet.deinitSpiAdc()