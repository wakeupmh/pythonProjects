import json

with open('PeriodicTable.json') as data_file:
    data = json.load(data_file)
opt = input('Write the symbol of an element:\n')
pt = data['elements']
for i in pt:
    if(i['symbol'] == opt):
        amass = i['atomic_mass']
        prot = int(i['number'])
        neut = int(amass) - prot
        elec = prot
        n = i['name']
        p = i['phase']
        c = i['category']
        d = i['discovered_by']
        de = i['density']
        ap = i['appearance']
        print("The element is {}\nYour natural phase is {}\nYour category is {}\nIt's discovered by {}\nYour atomic mass is {}\nIt has {} electrons,{} protons,{} neutrons\n".format(n,p,c,d,amass,elec,prot,neut))
        if(ap == None):
            print("Your density is {}g/L".format(de))
        else:
            print("Your density is {}g/L, and your apparence is like {}".format(de, ap))