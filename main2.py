print("Enter your marks for persentage:")

math = int(input("Math :"))
eng = int(input("English :"))
sci = int(input("Science :"))
soc = int(input("social studies :"))

sum = math+eng+sci+soc

print("sum of math+eng+sci+soc")

perc = (sum/400)*100

print(end="Persentage marks: ")

print(perc)