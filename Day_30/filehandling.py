'''try:
 print(10/0)
except ZeroDivisionError:
 print("Unable to divide a number with zero")
else:
 print("No Errors")
finally:
 print("End of the program")
'''
'''
try:
 d = {1:1,2:2,3:3}
 hashtag#print(d[4])hashtag#KeyError
 l=[1,2,3,4]
 hashtag#print(l[5])hashtag#IndexError
 hashtag#print('a'+7)hashtag#ValueError
 hashtag#a = int(input("Enter the amount:"))hashtag#TypeError
 print(n)hashtag#NameError
 print(10/0) 
except NameError:
 print("var is not define")
except TypeError:
 print("Enter the same data Type")
except ValueError:
 print("enter a proper value")
except IndexError:
 print("index outof range")
except KeyError:
 print("key is not present")
except ZeroDivisionError:
 print("Unable to divide a number with zero")
else:
 print("No Errors")
finally:
 print("End of the program")
'''
'''
 d = {1:1,2:2,3:3}
 print(d[4])hashtag#KeyError
 l=[1,2,3,4]
 print(l[5])hashtag#IndexError
 print('a'+7)hashtag#ValueError
 a = int(input("Enter the amount:"))hashtag#TypeError
 print(n)hashtag#NameError
 print(10/0) hashtag#ZerodivisionError
'''
'''
try:
 d = {1:1,2:2,3:3}
 print(d[4])hashtag#KeyError
 l=[1,2,3,4]
 print(l[5])hashtag#IndexError
 print('a'+7)hashtag#ValueError
 a = int(input("Enter the amount:"))hashtag#TypeError
 print(n)hashtag#NameError
 print(10/0) hashtag#ZerodivisionError
except(NameError,ValueError,TypeError,IndexError,KeyError,ZeroDivisionError)as e:
 print("Error Occured:",e)
else:
 print("No Errors")
finally:
 print("End of the program")

try:
 d = {1:1,2:2,3:3}
 print(d[4])hashtag#KeyError
 l=[1,2,3,4]
 print(l[5])hashtag#IndexError
 print('a'+7)hashtag#ValueError
 a = int(input("Enter the amount:"))hashtag#TypeError
 print(n)hashtag#NameError
 print(10/0) hashtag#ZerodivisionError
except Exception as e:
 print("Error Occured:",e)
else:
 print("No Errors")
finally:
 print("End of the program")

try:
 amount = int(input("Enter the Amount: "))
 if amount<0:
 raise Exception("Amount needs to be greater than 0")
except Exception as e:
 print("Error Occured:",e)
else:
 print("No Errors")
finally:
 print("End of the program")'''