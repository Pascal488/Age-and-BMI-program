#These lines here it's a program that excute your age in number and
#Body mass index(BMI) also give out some different status overview in each.
name = input("What is your name: ");
b = int(input("Enter your birth year: "));
a = 2020
bulo = (a - b)
print ('Hey {} your age is {}'.format(name, bulo))
if bulo == 20:
    print('Your in earl TWENTIES')
elif bulo < 20:
    print("Your in teenage")
elif bulo == 30:
	print('Your in earl thirties')
elif bulo == 40:
	print('Your in an elder')
elif bulo > 60 and bulo == 60:
	print('Oooh your a really elder')
elif bulo > 80:
	print("Yaani umekalibia kufa")

n = input("Enter your Father's name please: ")
c = int(input("Enter his birth year: "))
s = a
kuji = (s - c)
if kuji == 20:
    print('He is in  his earl TWENTIES!marvorous')
elif kuji < 20:
    print("Awesome does this true")
elif kuji == 30:
	print('He is in his earl thirties')
elif kuji == 40:
	print('His in an elder')
elif kuji > 60 and bulo == 60:
	print('Oooh he is a really elder')
elif kuji > 80:
	print("Baba yako amekalibia kufa")

z = input("Enter his weight in kilogram ")
k = input("Enter his height in meter ")
loi = (int(z) / int(k)) ** 2
q = str(loi)
print('Hey {} your Father named as {} his age is {}'.format(name, n, kuji,))
if loi < 25:
    print("{}:  It is a BMI of your Father so he is not over weight".format(q))
else:
	print("{}:  It is a BMI of your father so your father now is overweight and this is not good for health".format(q))

