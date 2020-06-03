import numpy as np

def rebin(xin, yin, ein, binwid, datatype='counts/mon'):

    xrequest = np.arange(min(xin) + binwid / 2, max(xin) - binwid / 2, binwid)

    xout = np.array([])
    yout = np.array([])
    eout = np.array([])

    for xcurr in xrequest:
        inds = (xin >= xcurr-binwid/2) & (xin <= xcurr+binwid/2)

        ycurr = yin[inds]
        ecurr = ein[inds]
        xout = np.hstack((xout, xcurr))
        yout = np.hstack((yout, np.mean(ycurr)))
        #print np.sqrt(np.sum(ecurr**2)) / ecurr.shape[0]
        eout = np.hstack((eout, np.sqrt(np.sum(ecurr**2)) / ecurr.shape[0]   ))

    return xout, yout, eout