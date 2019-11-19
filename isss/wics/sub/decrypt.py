text="""
Li jvy imx cxyi rs ilkxy,
li jvy imx jrtyi rs ilkxy,
li jvy imx vwx rs jlyfrk,
li jvy imx vwx rs srrplymexyy,
li jvy imx xbrgm rs cxplxs,
li jvy imx xbrgm rs legtxfdpliq,
li jvy imx yxvyre rs Jlwmi,
li jvy imx yxvyre rs Nvtzexyy,
li jvy imx ybtlew rs mrbx,
li jvy imx jleixt rs fxybvlt,
jx mvf xhxtqimlew cxsrtx dy,
jx mvf erimlew cxsrtx dy,
jx jxtx vpp wrlew fltxgi ir Yxvhxe,
jx jxtx vpp wrlew fltxgi imx rimxt jvq--
le ymrti, imx bxtlrf jvy yr svt plzx imx btxyxei bxtlrf, imvi yrkx rs
liy erlylxyi vdimrtlilxy leylyixf re liy cxlew txgxlhxf, srt wrrf rt srt
xhlp, le imx ydbxtpvilhx fxwtxx rs grkbvtlyre repq.

dispvw{ydckvtlex_glbmxt}
"""

dif = ord("L") - ord("W")
print(dif)
dif1 = ord("i") - ord("e")
print(dif1)
difs = [11,4]
x = 0
for i in text:
    #print("x" + str(x))
    print(chr(ord(i) + difs[x]),end='')
    x+=1
    if x >= len(difs):
        x=0
