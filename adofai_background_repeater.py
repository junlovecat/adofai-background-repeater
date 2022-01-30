def linear(x):return x
def inoutcubic(x):return 4*x*x*x if x<0.5 else 1-pow(-2*x+2,3)/2
def incubic(x):return x*x*x
def outcubic(x):return 1-pow(1-x,3)
from os import system
import numpy
print('Adofai background repeater v1.0.0')
filename=input('맵 이름(ex. main.adofai): ')
floor=int(input('타일 번호(ex. 123): '))
bgImage=input('배경 이름(ex. BG.png): ')
imageColor=input('사진 색깔(ex. ffffff): ')
onscaledsize=list(map(int,input('이전 크기, 이후 크기(ex. 150 75): ').split()))
angle=int(input('영향 각도 수: '))
ease=input('변화율 (linear, inoutcubic, incubic, outcubic): ')
easing=linear if ease=='linear' else inoutcubic if ease=='inoutcubic' else incubic if ease=='incubic' else outcubic if ease=='outcubic' else inoutcubic
easinglist=list(reversed(numpy.arange(0,1,1/angle))) if onscaledsize[0]>onscaledsize[1] else list(numpy.arange(0,1,1/angle))
text='\t\t'
if onscaledsize[0]>onscaledsize[1]:
    for x in range(len(easinglist)):
        text=text+f'{{ "floor": {floor}, "eventType": "CustomBackground", "color": "000000", "bgImage": "{bgImage}", "imageColor": "{imageColor}", "parallax": [100, 100], "bgDisplayMode": "Unscaled", "lockRot": "Disabled", "loopBG": "Disabled", "unscaledSize": {onscaledsize[1]+easing(easinglist[x])*(onscaledsize[0]-onscaledsize[1])}, "angleOffset": {x}, "eventTag": "" }},'
elif onscaledsize[1]>onscaledsize[0]:
    for x in range(len(easinglist)):
        text=text+f'{{ "floor": {floor}, "eventType": "CustomBackground", "color": "000000", "bgImage": "{bgImage}", "imageColor": "{imageColor}", "parallax": [100, 100], "bgDisplayMode": "Unscaled", "lockRot": "Disabled", "loopBG": "Disabled", "unscaledSize": {onscaledsize[0]+easing(easinglist[x])*(onscaledsize[1]-onscaledsize[0])}, "angleOffset": {x}, "eventTag": "" }},'
text=text[:-1]
file=[]
f=open(filename,'rt',encoding='utf-8')
while True:
    line=f.readline()
    if not line:break
    else:file.append(line)
for x in range(0,2):del file[-1]
file[-1]=file[-1][:-1]+',\n'
file.append(text)
file.append(']}')
f.close()
g=open('DONE.adofai','w',encoding='utf-8')
g.write(''.join(file))
g.close()
print('Open DONE.adofai for output')
system('pause')