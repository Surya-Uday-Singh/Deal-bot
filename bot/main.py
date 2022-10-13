from bot.booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go('New York')
        bot.date_if_far(num_of_months_from_today=0)
        bot.date_selection(check_in='2022-10-15', check_out='2022-10-23')
        bot.num_of_travellers(adults=4, children=2, rooms=3)
        bot.age_of_children("4", "8")
        bot.search_btn()
        bot.filteration()
        bot.refresh()
        bot.results()

except Exception as e:
    if 'in PATH' in str(e):
        print("The Bot is facing some issues running from the CLI(Command Line Interface)\n")
        print("Please download Selenium and chrome driver if you haven't already\n "
              "Then add to PATh your Selenium Drivers \n"
              "Windows: \n"
              "          set PATH=%PATH%;C:path-to-your-folder\n"
              "\nLINUX:\n"
              "       PATH=$PATH:/path/to-your/folder/ \n")

    else:
        raise

