import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    periods = np.arange(1, m * ppy + 1)

    coupon = face * couponRate / ppy

    cashflows = np.full(m * ppy, coupon)
    cashflows[-1] = cashflows[-1] + face

    pv = (1 + y / ppy) ** (-periods)

    pvcf = cashflows * pv

    weighted_pvcf = (periods / ppy) * pvcf

    bondDuration = np.sum(weighted_pvcf) / np.sum(pvcf)

    return(bondDuration)
