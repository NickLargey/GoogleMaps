from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt 
from statistics import mean
import time
from collections import Counter
import os, sys

from matplotlib import style
style.use("ggplot")

def createExamples():
    numberArrayExamples = open('poleArr.txt','a')
    numbersWeHave = range(1,19)
    for eachNum in numbersWeHave:
        imgFilePath = 'images/'+str(eachNum)+'.png'
        ei = Image.open(imgFilePath)
        eiar = np.array(ei)
        eiarl = str(eiar.tolist())

        lineToWrite = str(eachNum)+'::'+eiarl+'\n'
        numberArrayExamples.write(lineToWrite)

def threshold(imageArray):

    balanceAr = []
    newAr = imageArray
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)
    balance = mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            print(eachPix)
            if mean(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
             
    return newAr


for direct, _, file  in os.walk('C:\\Users\\nlargey\\Desktop\\QC scripts\\imgRec\\images'):
	for img in file:
		print(img)
		print(os.getcwd())
		i = Image.open('images\\' + str(img))
		iar = np.asarray(i)
		iar.setflags(write=1)
		threshold(iar)
		plt.imshow(iar)
		plt.show()
		time.sleep(5)
		plt.close()

createExamples()
whatNumIsThis(iar)
