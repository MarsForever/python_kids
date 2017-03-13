import easygui

# name
#room id  28 
#street Main Street
#city  Akron
#province/region/state  Ohio
#postcode  12345

name = easygui.enterbox("Please enter your name (ex:John Snead):",)
room = easygui.enterbox("Please enter your room ID and Street (ex:28 Main Street:",)
city = easygui.enterbox("Please enter your city and province/region/state(ex:Akron Ohio):",)
postcode = easygui.enterbox("Please enter your postcode:(ex:123-0003):",)
easygui.msgbox("This is your information:"+"\n"
               + name +"\n"
               + room +"\n"
               + city +"\n"
               + postcode)
