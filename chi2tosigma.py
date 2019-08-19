# https://arxiv.org/pdf/1305.5150v2.pdf

from scipy import special as spec
import math
import numpy as np
import matplotlib.pyplot as plt

def chi2tosigma(chi2):
  numerator = 1-np.exp(-chi2/2)
  denominator = 1+np.exp(-chi2/2)
  return math.sqrt(2)*spec.erfinv(numerator/denominator)

def sigmatochi2(ns):
  numerator = 1-spec.erf(ns/math.sqrt(2))
  denominator = 1+spec.erf(ns/math.sqrt(2))
  return -2*np.log(numerator/denominator)

print(math.sqrt(sigmatochi2(5)))

chi2s = np.linspace(1,50,50)

plt.plot(chi2s,chi2tosigma(chi2s))
plt.show()
plt.close("all")

ss = np.linspace(1,7)

plt.plot(ss,sigmatochi2(ss))
plt.show()
