#!/usr/bin/env python
import os,sys
#--matplotlib
import matplotlib
matplotlib.use('Agg')
import pylab  as py
import lhapdf

import pandas as pd
import numpy as np


#--from fitpack
from tools.tools import load,save,checkdir,lprint
from tools.config import conf,load_config
from qcdlib import aux,eweak


def errors(idx):

    conf['aux'] = aux.AUX()
    conf['eweak'] = eweak.EWEAK()
    data = pd.read_excel('expdata/1001.xlsx')
    data = data.to_dict(orient='list')
    target=data['target'][0]
    l    = len(data['value'])
    X    = np.array(data['X'])
    Q2   = np.array(data['Q2'])
    Xup  = np.array(data['Xup'])
    Xdo  = np.array(data['Xdo'])
    Q2up = np.array(data['Q2up'])
    Q2do = np.array(data['Q2do'])

    RS = data['RS'][0]
    S  = RS**2

    M2 = conf['aux'].M2

    if target=='d': M2 = 4*M2

    rho2 = 1 + 4*X**2*M2/Q2

    y=(Q2/2/X)/((S-M2)/2)

    #--luminosity (assume 100 fb-1)
    lum = 100

    dx  = Xup  - Xdo
    dQ2 = Q2up - Q2do

    bins = dx*dQ2

    YP = y**2*(rho2+1)/2 - 2*y +2
    YM = 1-(1-y)**2

    GF = conf['aux'].GF

    sin2w = np.array([conf['eweak'].get_sin2w(q2) for q2 in Q2])
    alpha = np.array([conf['eweak'].get_alpha(q2) for q2 in Q2])

    gA = -0.5
    gV = -0.5 + 2*sin2w

    tabname = 'JAM4EIC_%s'%target

    stf = lhapdf.mkPDF(tabname,0)

    #--get structure functions
    F2g  = np.array([stf.xfxQ2(900,x[i],q2[i]) for i in range(l)])
    FLg  = np.array([stf.xfxQ2(901,x[i],q2[i]) for i in range(l)])
    F2gZ = np.array([stf.xfxQ2(902,x[i],q2[i]) for i in range(l)])
    FLgZ = np.array([stf.xfxQ2(903,x[i],q2[i]) for i in range(l)])
    F3gZ = np.array([stf.xfxQ2(904,x[i],q2[i]) for i in range(l)])

    #--might need negative sign
    C  = GF*Q2/(2*np.sqrt(2)*np.pi*alpha)
  
    C1 = 2*np.pi*alpha**2/(x*y*Q2)

    T1g  = YP*F2g  - y**2*FLg
    T1gZ = YP*F2gZ - y**2*FLgZ

    T2 = x*YM*F3gZ

    sigR = C1*(T1g + C*(gV-gA)*(T1gZ - T2))
    sigL = C1*(T1g + C*(gV+gA)*(T1gZ + T2))

    NR = lum*sigR
    NL = lum*sigL

    C = 4/(NR+NL)**4

    syst2 = 4*() 

    



if __name__ == "__main__":

    idx=1000
    errors(idx)

















