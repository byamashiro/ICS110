from spacepy import pycdf
cdf = pycdf.CDF('wi_h0_wav_20120307_v01.cdf')

print(cdf['Epoch'][...])