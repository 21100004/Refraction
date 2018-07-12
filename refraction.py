# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 20:00:28 2018

@author: Irfan Javed
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath

def makeInterface(interLen, refIndex1, refIndex2, inside = False):
    cm = plt.get_cmap("Blues")
    fig = plt.figure(figsize = (10, 10))
    ax = fig.gca()
    if refIndex1<refIndex2:
        ax.axvspan(0, interLen, ymin = 0.5, facecolor = cm(4))
        ax.axvspan(0, interLen, ymax = 0.5, facecolor = cm(40))
    elif refIndex1==refIndex2:
        ax.axvspan(0, interLen, ymin = 0.5, facecolor = cm(4))
        ax.axvspan(0, interLen, ymax = 0.5, facecolor = cm(4))
    else:
        ax.axvspan(0, interLen, ymin = 0.5, facecolor = cm(4))
        ax.axvspan(0, interLen, ymax = 0.5, facecolor = cm(40))
    ax.set_xlim(-interLen/10, interLen+interLen/10)
    ax.set_xlabel("$x/m$", fontsize = 12)
    ax.set_ylabel("$y/m$", fontsize = 12)
    ax.set_title("$Fig. 1$", fontsize = 20)
    ax.plot([0, interLen], [0, 0], color = u"#1f77b4", linestyle = "-")
    ax.plot([0], [0], "ok")
    if inside==False:
        midInter = (-interLen/10+interLen+interLen/10)/2
        ax.set_ylim(-6, 6)
        ax.arrow(midInter, -1, 0, 1, width = interLen/100, color = "k",
                  length_includes_head = True, head_length = 12/50)
        ax.arrow(0, -1, 0, 1, width = interLen/100, color = "k",
                  length_includes_head = True, head_length = 12/50)
        ax.text(midInter-interLen/20, -1.2, "$Interface$")
        ax.text(-interLen/32, -1.2, "$Origin$")
    return fig

def divideInterface(interLen, numPiece, refIndex1, refIndex2, inside = False,
                    sourceX = None, sourceY = None, photoX = None,
                    photoY = None):
    if numPiece>1000:
        raise ValueError("numPiece cannot be greater than 1000.")
    if numPiece<=0:
        raise ValueError("numPiece must be a positive integer.")
    if type(numPiece)==float:
        raise TypeError("numPiece must be a positive integer.")
    cm = plt.get_cmap("Blues")
    pieceLen = interLen/numPiece
    valX = np.zeros([1, numPiece+1])
    varX1 = 0
    varX2 = pieceLen/2
    font = 200/numPiece
    fig = makeInterface(interLen, refIndex1, refIndex2, inside = True)
    ax = fig.gca()
    ax.set_title("$Fig. 2$", fontsize = 20)
    if inside==False:
        ax.set_ylim(-6, 6)
        for i in range(numPiece+1):
            if font>20 and i<numPiece:
                ax.text(varX2-pieceLen/5, -0.3, "$x_{"+str(i)+"}$",
                                                     fontsize = 20)
            elif 2.5<=font<=20 and i<numPiece:
                ax.text(varX2-pieceLen/5, -0.3, "$x_{"+str(i)+"}$",
                                                     fontsize = font)
            valX[0][i] = varX1
            varX1 += pieceLen
            if i<numPiece:
                varX2 += pieceLen
    else:
        ax.set_ylim(photoY-(sourceY-photoY)/5, sourceY+(sourceY-photoY)/5)
        medFrac = -(photoY-(sourceY-photoY)/5)/(sourceY-photoY+(2/5)
        *(sourceY-photoY))
        if refIndex1<refIndex2:
            ax.axvspan(0, interLen, ymin = medFrac, facecolor = cm(4))
            ax.axvspan(0, interLen, ymax = medFrac, facecolor = cm(40))
        elif refIndex1==refIndex2:
            ax.axvspan(0, interLen, ymin = medFrac, facecolor = cm(4))
            ax.axvspan(0, interLen, ymax = medFrac, facecolor = cm(4))
        else:
            ax.axvspan(0, interLen, ymin = medFrac, facecolor = cm(40))
            ax.axvspan(0, interLen, ymax = medFrac, facecolor = cm(4))
        for i in range(numPiece+1):
            if font>20 and i<numPiece:
                ax.text(varX2-pieceLen/5, -0.025*(sourceY-photoY+(2/5)
                *(sourceY-photoY)), "$x_{"+str(i)+"}$", fontsize = 20)
            elif 2.5<=font<=20 and i<numPiece:
                ax.text(varX2-pieceLen/5, -0.025*(sourceY-photoY+(2/5)
                *(sourceY-photoY)), "$x_{"+str(i)+"}$", fontsize = font)
            valX[0][i] = varX1
            varX1 += pieceLen
            if i<numPiece:
                varX2 += pieceLen
    zeros = np.zeros([1, numPiece+1])
    ax.plot(valX[0], zeros[0], "|k")
    return fig

def placeSAndP(interLen, numPiece, refIndex1, refIndex2, sourceX, sourceY,
               photoX, photoY):
    if sourceY<=0:
        raise ValueError("sourceY should be greater than zero.")
    if photoY>=10:
        raise ValueError("photoY should be less than zero.")
    if sourceX<0:
        raise ValueError("sourceX cannot be negative.")
    if sourceX>interLen:
        raise ValueError("sourceX cannot be greater than interLen.")
    if photoX<0:
        raise ValueError("photoX cannot be negative.")
    if photoX>interLen:
        raise ValueError("photoX cannot be greater than interLen.")
    fig = divideInterface(interLen, numPiece, refIndex1, refIndex2,
                          inside = True, sourceX = sourceX, sourceY = sourceY,
                          photoX = photoX, photoY = photoY)
    ax = fig.gca()
    ax.set_title("$Fig. 3$", fontsize = 20)
    ax.plot([sourceX], [sourceY], "*r", markersize = 15)
    ax.plot([photoX], [photoY], "hg", markersize = 15)
    ax.text(sourceX-(1/90)*(interLen+(1/5)*interLen), sourceY+(1/40)*(sourceY
            -photoY+(2/5)*(sourceY-photoY)), "$A$", fontsize = 20)
    ax.text(photoX-(1/90)*(interLen+(1/5)*interLen), photoY-(1/20)*(sourceY
            -photoY+(2/5)*(sourceY-photoY)), "$B$", fontsize = 20)
    return fig

def classicalPath(interLen, numPiece, refIndex1, refIndex2, sourceX, sourceY,
                  photoX, photoY):
    fig = placeSAndP(interLen, numPiece, refIndex1, refIndex2, sourceX,
                     sourceY, photoX, photoY)
    ax = fig.gca()
    ax.set_title("$Fig. 4$", fontsize = 20)
    if sourceX==photoX:
        ax.plot([sourceX, sourceY], [sourceX, 0], "r-")
        ax.plot([sourceX, photoX], [0, photoY], "r-")
        ax.annotate("", xy = (sourceX, sourceY/2), xytext = (sourceX, sourceY),
                    arrowprops = {"arrowstyle": "->", "ec": "r"}, size = 15,
                    ha = "center", va = "center")
        ax.annotate("", xy = (sourceX, photoY/2), xytext = (sourceX, 0),
                    arrowprops = {"arrowstyle": "->", "ec": "r"}, size = 15,
                    ha = "center", va = "center")
    else:
        if sourceX<photoX:
            low = sourceX
            high = photoX
        else:
            low = photoX
            high = sourceX
        mid = (low+high)/2
        dist1 = np.sqrt((mid-sourceX)**2+(sourceY)**2)
        dist2 = np.sqrt((mid-photoX)**2+(photoY)**2)
        while abs(refIndex1*np.sin(np.pi/2-np.arcsin(abs(sourceY/dist1)))
        -refIndex2*np.sin(np.pi/2-np.arcsin(abs(photoY/dist2))))>0.0000000001:
            if (refIndex1*np.sin(np.pi/2-np.arcsin(abs(sourceY/dist1)))
            >refIndex2*np.sin(np.pi/2-np.arcsin(abs(photoY/dist2)))):
                if sourceX<photoX:
                    high = mid
                elif sourceX>photoX:
                    low = mid
                mid = (low+high)/2
                dist1 = np.sqrt((mid-sourceX)**2+(sourceY)**2)
                dist2 = np.sqrt((mid-photoX)**2+(photoY)**2)
            elif (refIndex1*np.sin(np.pi/2-np.arcsin(abs(sourceY/dist1)))
            <refIndex2*np.sin(np.pi/2-np.arcsin(abs(photoY/dist2)))):
                if sourceX<photoX:
                    low = mid
                elif sourceX>photoX:
                    high = mid
                mid = (low+high)/2
                dist1 = np.sqrt((mid-sourceX)**2+(sourceY)**2)
                dist2 = np.sqrt((mid-photoX)**2+(photoY)**2)
        refPointX = mid
        ax.plot([sourceX, refPointX], [sourceY, 0], "r-")
        ax.plot([refPointX, photoX], [0, photoY], "r-")
        ax.annotate("", xy = ((sourceX+refPointX)/2, sourceY/2), xytext =
                    (sourceX, sourceY), arrowprops =
                    {"arrowstyle": "->", "ec": "r"}, size = 15, ha = "center",
                    va = "center")
        ax.annotate("", xy = ((refPointX+photoX)/2, photoY/2), xytext =
                    (refPointX, 0), arrowprops =
                    {"arrowstyle": "->", "ec": "r"}, size = 15, ha = "center",
                    va = "center")
    return fig

def QEDPath(interLen, numPiece, refIndex1, refIndex2, sourceX, sourceY, photoX,
             photoY):
    pieceLen = interLen/numPiece
    fig = classicalPath(interLen, numPiece, refIndex1, refIndex2, sourceX,
                        sourceY, photoX, photoY)
    ax = fig.gca()
    ax.set_title("$Fig. 5$", fontsize = 20)
    if numPiece<=80:
        midPointX1 = (sourceX+pieceLen/2)/2
        midPointX2 = (pieceLen/2+photoX)/2
        ax.annotate("", xy = (midPointX1, sourceY/2), xytext =
                    (sourceX, sourceY),
                    arrowprops = {"arrowstyle": "->", "ec": "k"}, size = 15,
                    ha = "center", va = "center")
        ax.annotate("", xy = (midPointX2, photoY/2), xytext =
                    (pieceLen/2, 0),
                    arrowprops = {"arrowstyle": "->", "ec": "k"}, size = 15,
                    ha = "center", va = "center")
    for i in range(0, numPiece):
        ax.plot([sourceX, pieceLen/2+i*pieceLen], [sourceY, 0], "-k")
        ax.plot([pieceLen/2+i*pieceLen, photoX], [0, photoY], "-k")
        if numPiece<=80:
            midPointX1 = (sourceX+pieceLen/2+i*pieceLen)/2
            midPointX2 = (pieceLen/2+i*pieceLen+photoX)/2
            ax.annotate("", xy = (midPointX1, sourceY/2), xytext =
                        (sourceX, sourceY),
                        arrowprops = {"arrowstyle": "->", "ec": "k"}, size = 15,
                        ha = "center", va = "center")
            ax.annotate("", xy = (midPointX2, photoY/2), xytext =
                        (pieceLen/2+i*pieceLen, 0),
                        arrowprops = {"arrowstyle": "->", "ec": "k"}, size = 15,
                        ha = "center", va = "center")

def createTimes(interLen, numPiece, refIndex1, refIndex2, sourceX, sourceY,
                photoX, photoY, speed):
    pieceLen = interLen/numPiece
    times = np.zeros([1, numPiece])
    for i in range(numPiece):
        times[0][i] = (np.sqrt((pieceLen/2+i*pieceLen-sourceX)**2+(sourceY**2))
        /(speed/refIndex1)+np.sqrt((pieceLen/2+i*pieceLen-photoX)**2
          +(photoY**2))/(speed/refIndex2))
    return times

def plotTimes(interLen, numPiece, times):
    pieceLen = interLen/numPiece
    length = np.zeros([1, numPiece])
    xTicksOld = np.zeros([1, numPiece+1])
    xTicksNew = []
    for i in range(numPiece):
        length[0][i] = pieceLen/2+i*pieceLen
    fig = plt.figure(figsize = (10, 10))
    ax = fig.gca()
    ax.set_xlabel("$Length/m$", fontsize = 12)
    ax.set_ylabel("$Time/s$", fontsize = 12)
    ax.set_title("$Fig. 6$", fontsize = 20)
    ax.plot(length[0], times[0], "ok-")
    for i in range(numPiece+1):
        xTicksOld[0][i] = i*pieceLen
        xTicksNew.append(round(i*pieceLen, 1))
    ax.set_xticks(xTicksOld[0])
    if numPiece<=25:
        ax.set_xticklabels(xTicksNew)
    else:
        ax.set_xticklabels([])

def phasorsOnInterface(interLen, numPiece, times):
    pieceLen = interLen/numPiece
    lightFreq = None
    minInt = None
    for i in range(1, numPiece):
        if minInt==None or minInt>times[0][i]-times[0][i-1]:
            minInt = times[0][i]-times[0][i-1]
    lightFreq = (7.5/360)/minInt
    comp = np.zeros([1, numPiece], dtype = complex)
    x = np.zeros([1, numPiece])
    y = np.zeros([1, numPiece])
    reals = np.zeros([1, numPiece])
    imags = np.zeros([1, numPiece])
    z = 0
    fig = plt.figure(figsize = (10, 10))
    ax = fig.gca()
    for i in range(numPiece):
        comp[0][i] = (interLen/10)*cmath.exp(2*np.pi*lightFreq*times[0][i]*1j)
        reals[0][i] = ((interLen/10)*(cmath.exp(2*np.pi*lightFreq
             *times[0][i]*1j))).real
        imags[0][i] = ((interLen/10)*(cmath.exp(2*np.pi*lightFreq
             *times[0][i]*1j))).imag
        x[0][i] = pieceLen/2+i*pieceLen
        z += (interLen/10)*cmath.exp(2*np.pi*lightFreq*times[0][i]*1j)
    ax.set_xlim(-interLen/10, interLen+interLen/10)
    ax.set_ylim(-interLen/2-interLen/10, interLen/2+interLen/10)
    ax.set_xlabel("$x/m$", fontsize = 12)
    ax.set_ylabel("$y/m$", fontsize = 12)
    ax.set_title("$Fig. 7$", fontsize = 20)
    ax.plot([0, interLen], [0, 0], "-")
    ax.plot([0], [0], "ok")
    ax.quiver(x, y, reals, imags, angles = "xy", scale_units = "xy", scale = 1)
    return reals, imags, z

def addPhasors(numPiece, reals, imags, z, startInd, endInd):
    if startInd<0 or startInd>numPiece-1:
        raise ValueError("startInd must be between 0 and numPiece-1 inclusive.")
    if endInd<0 or endInd>numPiece-1:
        raise ValueError("endInd must be between 0 and numPiece-1 inclusive.")
    if startInd>=endInd:
        raise ValueError("startInd must be less than endInd.")
    if type(startInd)!=int:
        raise TypeError("startEnd must be a nonnegative integer.")
    if type(endInd)!=int:
        raise TypeError("endInd must be a nonnegative integer.")
    diff = endInd-startInd
    reals = reals[0][startInd: endInd+1]
    imags = imags[0][startInd: endInd+1]
    x = np.zeros([1, diff+1])
    y = np.zeros([1, diff+1])
    u = np.zeros([1, diff+1])
    v = np.zeros([1, diff+1])
    xRes = np.zeros([1, diff+2])
    yRes = np.zeros([1, diff+2])
    xResVar = 0
    yResVar = 0
    fig = plt.figure(figsize = [10, 10])
    ax = fig.gca()
    for i in range(diff+1):
        xResVar += reals[i]
        yResVar += imags[i]
        u[0][i] = reals[i]
        v[0][i] = imags[i]
        xRes[0][i+1] = xResVar
        yRes[0][i+1] = yResVar
    for i in range(diff):
        x[0][i+1] = xRes[0][i+1]
        y[0][i+1] = yRes[0][i+1]
    ax.set_xlim(xRes.min()-(xRes.max()-xRes.min())/10, xRes.max()
    +(xRes.max()-xRes.min())/10)
    ax.set_ylim(yRes.min()-(yRes.max()-yRes.min())/10, yRes.max()
    +(yRes.max()-yRes.min())/10)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.set_title("$Fig. 8$", fontsize = 20)
    ax.plot([0], [0], "ok")
    ax.plot(xRes[0][-1], yRes[0][-1], "ok")
    ax.quiver(x, y, u, v, angles = "xy", scale_units = "xy", scale = 1)
    ax.quiver([0], [0], xRes[0][-1], yRes[0][-1], color = ["r"],
               angles = "xy", scale_units = "xy", scale = 1)