#dimiourgia latin(sinartisi)
def latin(num):
    #lista ari8mwn
        ari8moi = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    #lista latinikon ari8mwn
        latin = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        i = 0
        res = ""
        while num > 0:
            for j in range(num//ari8moi[i]):
                res += latin[i]
                num -= ari8moi[i]
            i += 1
        print (res)
n=raw_input('grapse enan thetiko arithmo(an den einai thetikos den tha ginei tipota!!!): ')
n=int(n)
if n<=0:
    print("prepei na einai 8etikos")
elif  n>0 and n<4000:
  latin(n)
elif n>=4000:
  p = n/1000;
  print "-",latin(p)
