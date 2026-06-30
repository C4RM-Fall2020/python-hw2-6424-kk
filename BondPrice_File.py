import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    periods = np.arange(1, m * ppy + 1)

    coupon = face * couponRate / ppy

    cashflows = np.full(m * ppy, coupon)
    cashflows[-1] = cashflows[-1] + face

    pv = (1 + y / ppy) ** (-periods)

    bondPrice = np.sum(cashflows * pv)

    return(bondPrice)
