a = "my.image.1.for.you.jpg"

Count = a.count(".")
X = 1

for i in range(a.count(".") ):
    result = a.find("." , X , len(a))
    print(result)
    X = result + 1
