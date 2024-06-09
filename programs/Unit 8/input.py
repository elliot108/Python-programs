import dbm

org_dic = dbm.open('org_dic','c')

org_dic ={'Millie Bobby Brown':'Eleven or Jane Hopper',
'Finn Wolfhard' : 'Mike Wheeler',
'Noah Schnapp' : 'Will Byer',
'Sadie Sink' : 'Max',
'Gaten Matarazzo' : 'Dustin Henderson',
'Caleb Mclaughlin' : 'Lucas Sinclair',
'Joe Keeten' : 'Steve Harrington',
} 

for key in org_dic:
    print(key,':', org_dic[key])
print()
