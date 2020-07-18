#!/usr/bin/env python
import os,sys
#--matplotlib
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import numpy as np

import pylab  as py

#--from tools
from tools.tools import load,save,checkdir,lprint


def plot():
    data = pd.read_excel('expdata/1001.xlsx')
    data = data.to_dict(orient='list')
    l    = len(data['value'])
  
    #--get fixed values for Q2
    Q2 = []
    for q2 in data['Q2']:
        if q2 in Q2: continue
        Q2.append(q2)
    X, val = {}, {}
    for j in range(len(Q2)):
        X[j], val[j] = [],[]
        for i in range(l):
            if data['Q2'][i] != Q2[j]: continue
            if data['X'][i] > 0.8: continue
            X[j]  .append(data['X'][i])
            val[j].append(data['value'][i])

    nrows, ncols = 1,1
    fig = py.figure(figsize=(ncols*8,nrows*6))
    ax11 = py.subplot(nrows,ncols,1)

    for j in range(len(Q2)):
        ax11.scatter(X[j],np.abs(val[j]),color='red',s=8)
   
    for ax in [ax11]:
        ax.semilogx()
        ax.semilogy()
        ax.set_xlim(2e-5,2.0)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=10)
      

    ax11.set_xlabel(r'$x$',size=20)      
    ax11.set_ylabel(r'$|A_{PV}|$',size=20)      
    ax11.set_ylim(1e-4,1)

    ax11.text(0.03,0.07,r'$Q^2=%s$'%np.round(Q2[0],1),transform=ax11.transAxes,size=12)
    ax11.text(0.03,0.17,r'$Q^2=%s$'%np.round(Q2[1],1),transform=ax11.transAxes,size=12)
    ax11.text(0.03,0.25,r'$Q^2=%s$'%np.round(Q2[2],1),transform=ax11.transAxes,size=12)
    ax11.text(0.03,0.38,r'$Q^2=%s$'%np.round(Q2[3],1),transform=ax11.transAxes,size=12)
    ax11.text(0.03,0.48,r'$Q^2=%s$'%np.round(Q2[4],1),transform=ax11.transAxes,size=12)
    ax11.text(0.03,0.58,r'$Q^2=%s$'%np.round(Q2[5],1),transform=ax11.transAxes,size=12)
    ax11.text(0.03,0.68,r'$Q^2=%s$'%np.round(Q2[6],1),transform=ax11.transAxes,size=12)
    ax11.text(0.03,0.78,r'$Q^2=%s$'%np.round(Q2[7],1),transform=ax11.transAxes,size=12)
    ax11.text(0.03,0.85,r'$Q^2=%s$'%np.round(Q2[8],1),transform=ax11.transAxes,size=12)
    ax11.text(0.03,0.93,r'$Q^2=%s$'%np.round(Q2[9],1),transform=ax11.transAxes,size=12)


    py.tight_layout()
    filename = 'test.png'
    py.savefig(filename)
    print('Saving figure to %s'%filename)
    py.clf()

if __name__ == "__main__":

    plot()

















