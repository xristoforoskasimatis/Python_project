import urllib2
import json
import datetime

def ari8moipaikti():
	while True:
		x = [""]*10
		y = raw_input("Dwse 10 arithous apo to 1 ews to 80 me komma anamesa \n")
		z= y.split(",")
		while True:
			if z[-1]=="":
				z.remove(z[-1])
			else:
				break
		if 	len(z)!=10:
			del x
			continue
		else:
			try:
				for k in range(len(z)):
					x[k] = int(z[k])
					if not(x[k] in range(1,81)):
						print "Numbers in [1,80]"
						del x
						break
					else:
						j = 0
						for l in range(len(x)):
							if x[l]==x[k]:
								j+=1
						if j>=2:
							print "Different numbers"
							del x
							break
				if len(x)==10:
					break
				else:
					del x
					continue
			except:
				continue
	return x
def fortDedomena(a):
		tora = a.strftime("%d-%m-%Y")
		url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json"%tora
		ait = urllib2.Request(url)
		ap = urllib2.urlopen(ait)
		ded= ap.read()
		ded = json.loads(ded)
		return ded
def Vres_Nikes(ded,a):
	nikes = 0
	for x in ded['draws']['draw']:
		ar = 0
		y= ded['draws']['draw'][a]['results']
		for z in range(10):
			if epiloges[z] in y:
				ar+=1
		if ar>4:
			nikes+=1
		a+=1
	return nikes
def imer(c):
	simera = c.day
	if c.hour in range(0,9):
		simera = simera -1
	return simera
def apothNikes(a):
	ded = fortDedomena(a)
	x = 0
	nikes = Vres_Nikes(ded,x)
	im_nikes.append(nikes)
	nik_mera.append(a.strftime("%d-%m-%Y"))

im_nikes = []
nik_mera = []
epiloges = ari8moipaikti()
c = datetime.datetime.now()
day = imer(c)
b = datetime.datetime(c.year, c.month, 1)
a= datetime.datetime(c.year, c.month, day)
while a>=b:
	apothNikes(a)
	a=a - datetime.timedelta(days=1)
lucky_day = im_nikes.index(max(im_nikes))
if max(im_nikes) != 0:
	print "Tha eixes tis perissoteres nikes:",nik_mera[lucky_day]
else:
		print "eisai poly atixos, den kerdises kamia fora"
