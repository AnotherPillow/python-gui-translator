import codes
def main(OptionMenu,window,wdd,wdd_options,all_codes_v,common_drop_down,which_drop_down):
    option = which_drop_down.get()
    if option == "All countries' ISO 639-1 codes":
        acd = OptionMenu(window, all_codes_v, *codes.all())
        acd.pack()
    elif option == "Common countries' ISO 639-1 codes":
        cld = OptionMenu(window, common_drop_down, *codes.common())
        cld.pack()