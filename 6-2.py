import easygui
flavor = easygui.enterbox ("What is your favorit language flavor?",
                           default = 'Python')
easygui.msgbox("You picked " + flavor)
