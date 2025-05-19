finalnumbers=[0]
actualvalue=0
output="0,"
totalintegers= int(input("Times the number inreases"))

def on_forever():
    global actualvalue
    actualvalue+=1
    finalnumbers.append(actualvalue)
for i in range(totalintegers):
    on_forever()
    output=str(output)+str(finalnumbers[actualvalue])

print(output)