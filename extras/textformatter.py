
# f=open("text formatter.txt", "r")

# l=f.readlines()
# print(l)

# s="\n".join(l)
# print(s)
# f.close()

# f=open("out.txt", "w")
# f.write(s)
# f.close()


# f=open("text.txt", "r")

# l=f.readlines()
# for i in l:
#     i=i.replace("  ", "")
#     print(i.split("\t"))



# f.close()



x=[ ['BR1', 'Brazil\n'],
['EUN1', 'Europe Nordic & East\n'],
['EUW1', 'Europe West\n'],
['JP1', 'Japan\n'],
['KR', 'Republic of Korea\n'],
['LA1', 'Latin America North\n'],
['LA2', 'Latin America South\n'],
['NA1', 'North America\n'],
['OC1', 'Oceania\n'],
['TR1', 'Turkey\n'],
['RU', 'Russia\n'],
['PH2', 'The Philippines\n'],
['SG2', 'Singapore, Malaysia, & Indonesia\n'],
['TH2', 'Thailand\n'],
['TW2', 'Taiwan, Hong Kong, and Macao\n'],
['VN2', 'Vietnam\n']]

server={}
for i in x:
    i[1]=i[1].strip("\n")
    server[i[0].lower()]=i[1].lower()

for k,v in server.items():
    print(k,v)

print(server)