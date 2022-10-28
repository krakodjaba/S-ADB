import COLORS
banner = f"""{COLORS.REDL}
                                      _____              _____  ____  
                                     / ____|       /\   |  __ \|  _ \ 
                                    | (___ ______ /  \  | |  | | |_) |
                                     \___ \______/ /\ \ | |  | |  _ < 
                                     ____) |    / ____ \| |__| | |_) |
                                    |_____/    /_/    \_\_____/|____/ 
                                                                         by mav1
                                                                            [99] About
                                                """
def about():
    Telegram_group = ' Telegram Channel: @mav1_notes'
    Telegram_username = ' Author: @mavijj'
    About = ' S-ADB shell for Android-Debug-Bridge.'
    creds = ' This shell remake of Satana-Android-Debug-Bridge by bafomet666.\n\n'
    about_list = [About, Telegram_username, Telegram_group, creds]
    for i, data in enumerate(about_list):
        print(f' {COLORS.REDL}[{COLORS.FIOL}{i}{COLORS.REDL}]{COLORS.OKNL} {data}')
