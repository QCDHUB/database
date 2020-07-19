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


def errors(idx,new_idx):

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


    #--luminosity (assume 100 fb-1)
    lum = 100

    dx  = Xup  - Xdo
    dQ2 = Q2up - Q2do

    bins = dx*dQ2


    GF = conf['aux'].GF

    if target =='p': tabname = 'JAM4EIC_p'

    stf = lhapdf.mkPDF(tabname,0)

    #--integrate over bin
    #--get structure functions
    F2g  = lambda x,q2: stf.xfxQ2(900,x,q2)
    FLg  = lambda x,q2: stf.xfxQ2(901,x,q2)
    F2gZ = lambda x,q2: stf.xfxQ2(902,x,q2)
    FLgZ = lambda x,q2: stf.xfxQ2(903,x,q2)
    F3gZ = lambda x,q2: stf.xfxQ2(904,x,q2)

    rho2 = lambda x,q2: 1 + 4*x**2*M2/q2

    y=lambda x,q2: (q2/2/x)/((S-M2)/2)

    YP = lambda x,q2: y(x,q2)**2*(rho2(x,q2)+1)/2 - 2*y(x,q2) +2
    YM = lambda x,q2: 1-(1-y(x,q2))**2

    sin2w = lambda q2: conf['eweak'].get_sin2w(q2)
    alpha = lambda q2: conf['eweak'].get_alpha(q2)

    gA = -0.5
    gV = lambda q2: -0.5 + 2*sin2w(q2)

    C  = lambda q2: GF*q2/(2*np.sqrt(2)*np.pi*alpha(q2))
  
    C1 = lambda x,q2: 2*np.pi*alpha(q2)**2/(x*y(x,q2)*q2)

    T1g  = lambda x,q2: YP(x,q2)*F2g(x,q2)  - y(x,q2)**2*FLg(x,q2)
    T1gZ = lambda x,q2: YP(x,q2)*F2gZ(x,q2) - y(x,q2)**2*FLgZ(x,q2)

    T2 = lambda x,q2: x*YM(x,q2)*F3gZ(x,q2)

    _ddsigR = lambda x,q2: C1(x,q2)*(T1g(x,q2) + C(q2)*(gV(q2)-gA)*(T1gZ(x,q2) - T2(x,q2)))
    _ddsigL = lambda x,q2: C1(x,q2)*(T1g(x,q2) + C(q2)*(gV(q2)+gA)*(T1gZ(x,q2) + T2(x,q2)))

    z1,w1 = np.polynomial.legendre.leggauss(5)
    z2,w2 = np.polynomial.legendre.leggauss(5)

    ddsigR = np.zeros((len(X),len(z1),len(z2)))
    ddsigL = np.zeros((len(X),len(z1),len(z2)))
    for i in range(len(X)):
        _x   = 0.5*((Xup[i] -Xdo[i])*z1  + Xup[i]  + Xdo[i])
        _q2  = 0.5*((Q2up[i]-Q2do[i])*z2 + Q2up[i] + Q2do[i])
        xjac  = 0.5*(Xup[i]-Xdo[i])
        q2jac = 0.5*(Q2up[i]-Q2do[i])
        for j in range(len(_x)):
            for k in range(len(_q2)):
                ddsigR[i][j][k] = _ddsigR(_x[j],_q2[k])*xjac*q2jac
                ddsigL[i][j][k] = _ddsigL(_x[j],_q2[k])*xjac*q2jac
   
    #--integrate over Q2
    dsigR = np.sum(w2*ddsigR,axis=2) 
    dsigL = np.sum(w2*ddsigL,axis=2) 

    #--integrate over X
    sigR = np.sum(w1*dsigR,axis=1) 
    sigL = np.sum(w1*dsigL,axis=1) 

    #--multiply by bin
    #--get structure functions
    #F2g  = np.array([stf.xfxQ2(900,X[i],Q2[i]) for i in range(l)])
    #FLg  = np.array([stf.xfxQ2(901,X[i],Q2[i]) for i in range(l)])
    #F2gZ = np.array([stf.xfxQ2(902,X[i],Q2[i]) for i in range(l)])
    #FLgZ = np.array([stf.xfxQ2(903,X[i],Q2[i]) for i in range(l)])
    #F3gZ = np.array([stf.xfxQ2(904,X[i],Q2[i]) for i in range(l)])

    #rho2 = 1 + 4*X**2*M2/Q2

    #y= (Q2/2/X)/((S-M2)/2)

    #YP =  y**2*(rho2+1)/2 - 2*y +2
    #YM =  1-(1-y)**2

    #sin2w = np.array([conf['eweak'].get_sin2w(q2) for q2 in Q2])
    #alpha = np.array([conf['eweak'].get_alpha(q2) for q2 in Q2])

    #gA = -0.5
    #gV = -0.5 + 2*sin2w

    #C  =  GF*Q2/(2*np.sqrt(2)*np.pi*alpha)
  
    #C1 =  2*np.pi*alpha**2/(X*y*Q2)*bins

    #T1g  = YP*F2g  - y**2*FLg
    #T1gZ = YP*F2gZ - y**2*FLgZ

    #T2 =  X*YM*F3gZ

    #sigR =  C1*(T1g + C*(gV-gA)*(T1gZ - T2))
    #sigL =  C1*(T1g + C*(gV+gA)*(T1gZ + T2))

    NR = lum*sigR
    NL = lum*sigL

    C = 4/(NR+NL)**4

    T1 = NL**2*np.sqrt(NR)
    T2 = NR**2*np.sqrt(NL)

    syst2 = C*(T1+T2)

    syst = np.sqrt(syst2)

    #--add syst errors and save new excel sheet
    data ['syst_u'] = syst
  
    print syst 
    df = pd.DataFrame(data)
    df.to_excel('expdata/%s.xlsx'%new_idx,index=False) 



if __name__ == "__main__":

    idx=1000
    new_idx = 2000
    errors(idx,new_idx)

















