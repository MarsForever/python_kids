import easygui
flavor = easygui.buttonbox ("What is your favorit language flavor?",
                 choices = ['C language','Java','Python'])
easygui.msgbox("You picked " + flavor)
