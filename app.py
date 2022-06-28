from translate import Translator
from tkinter import *
from showdropdowns import main as show_drop_downs


#translator= Translator(to_lang="en")
#translation = translator.translate("ayúdame")
#print(translation)

def get_text(window,User_input,all_codes_v,common_drop_down,which_drop_down,translated_text):
    text = User_input.get()
    option = which_drop_down.get()
    if option == "All countries' ISO 639-1 codes":
        option = "all"
    elif option == "Common countries' ISO 639-1 codes":
        option = "common"
    #get the option from the dropdown menu

    if option == "all":
        translator= Translator(to_lang=all_codes_v.get())
        translation = translator.translate(text)
        st_label.config(text="Translated text:")
        setTextInput(translation)
    elif option == "common":
        translator= Translator(to_lang=common_drop_down.get())
        translation = translator.translate(text)
        st_label.config(text="Translated text:")
        #make a single line of text in a widget
        setTextInput(translation)

    if text == "":
        print("Please enter text")

    User_input.delete(0,END)

window = Tk()
window.title("Translation")
window.geometry('500x400')
label = Label(window, text="Enter text to translate:")
label.pack()
User_input = Entry(window, width=50)
User_input.pack()


all_codes_v = StringVar()
all_codes_v.set("All language's ISO 639-1 codes") # default value

which_drop_down = StringVar()
which_drop_down.set("From which dropdown are you picking the language from.") # default value

common_drop_down = StringVar()
common_drop_down.set("Common/European languages' ISO 639-1 codes") # default value

wdd_options = [
    "All countries' ISO 639-1 codes",
    "Common countries' ISO 639-1 codes"
]


sometext = Label(window, text="Choose a language to translate to (ISO code):")
sometext.pack()
wdd = OptionMenu(window, which_drop_down, *wdd_options)
wdd.pack()
#add a button to hide the cld dropdown if wdd is set to option one
button2 = Button(window, text="Show drop down", command=lambda: show_drop_downs(OptionMenu,window,wdd,wdd_options,all_codes_v,common_drop_down,which_drop_down))
button2.pack()

#cld = OptionMenu(window, common_drop_down, *codes.common())
#cld.pack()
#acd = OptionMenu(window, all_codes_v, *codes.all())
#acd.pack()



button = Button(window, text="Translate", command=lambda: get_text(window,User_input,all_codes_v,common_drop_down,which_drop_down,translated_text))
button.pack()

st_label = Label( window , text = "" )
st_label.pack()
"""
translated_label = Text(window, height=1)
translated_label.insert(2.0, "")
translated_label.configure(bg=window.cget('bg'), relief="flat")
translated_label.configure(state="disabled")

translated_label.pack()
"""

def setTextInput(text):
    translated_text.delete(1.0,"end")
    translated_text.insert(1.0, text)

translated_text = Text(window, height=10)
translated_text.pack()

window.mainloop()