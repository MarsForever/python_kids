import easygui

centi = 0
Fahrenheit = 0

Fahrenheit =easygui.integerbox("""Please enter Fahreheit:""")
centi = 5/9 *(Fahrenheit -32)
easygui.msgbox("Degree centigrade is "+str(float(centi)))
