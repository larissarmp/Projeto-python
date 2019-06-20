arq = open("file.txt","a")
arq.write("n/ novas funçoes")
arq.close()

arq = open("file.txt")
print(arq.readlines())
arq.close()