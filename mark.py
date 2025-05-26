def react_to_mark(subject, mark):
    if mark == 100:
        print(f"{subject}: Perfect score! 🎉")
    elif mark == 90:
        print(f"{subject}: Excellent! 💯")
    elif mark == 70:
        print(f"{subject}: Good job! 👍")
    elif mark == 50:
        print(f"{subject}: Just decent. Keep improving! 🙂")
    elif mark < 35:
        print(f"{subject}: Failed ❌")
    else:
        print(f"{subject}: Mark is {mark}")

Tam=int(input("Enter a Tam Mark:"))
Eng=int(input("Enter a Eng Mark:"))
Mat=int(input("Enter a Mat Mark:"))
Phy=int(input("Enter a Phy Mark:"))
Chm=int(input("Enter a Chm Mark:"))
Com=int(input("Enter a Com Mark:"))

react_to_mark("Tam",Tam)
react_to_mark("Eng",Eng)
react_to_mark("Mat",Mat)
react_to_mark("Phy",Phy)
react_to_mark("Chm",Chm)
react_to_mark("Com",Com)


if Tam>=35 and Eng >= 35 and Mat >= 35 and Phy >= 35 and Chm>= 35 and Com>=35:
 print("Pass ✅")
else:
  print( "You Are Fail ❌")
