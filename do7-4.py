import easygui

tries = 0
guess = 0
password = 12
five = 5
easygui.msgbox("""You can enter 6 times password.""")

while guess != password and tries < 6:
    guess = easygui.integerbox("Please enter password:")
    if not guess : break
    if guess != password:
        easygui.msgbox("It is not right password!")
        easygui.msgbox("You have "+str(five -tries)+ " chances")
    tries = tries + 1


if guess == password:
    easygui.msgbox("You are in")
else:
    easygui.msgbox("Password is not right !!!")
    
