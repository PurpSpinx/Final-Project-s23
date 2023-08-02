from manager import Manager
m=Manager()
m.generate_password("google","gman",6)
m.generate_password("youtube","yman",6)

m.save()
print(m.load())