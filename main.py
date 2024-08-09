def calendar(year: int, month: int):
    days_of_the_month = 0
    start_index = 0

    start_year = 2024
    selected_year = year

    leap_year_quantity_modified = (selected_year - 2021) // 4
    leap_year_quantity = (selected_year - 2020) // 4

    is_leap_year = selected_year % 4 == 0

    week_days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

    start_day_calc_modified = (leap_year_quantity_modified + (selected_year - start_year)) % len(week_days)
    start_day_calc = (leap_year_quantity + (selected_year - start_year)) % len(week_days)

    selected_month = month

    if selected_month == 1:
        days_of_the_month = 32
        start_index = start_day_calc_modified % len(week_days)
    elif selected_month == 2:
        days_of_the_month = 30 if is_leap_year else 29
        start_index = (start_day_calc_modified - 4) % len(week_days)
    elif selected_month == 3:
        days_of_the_month = 32
        start_index = (start_day_calc - 4) % len(week_days)
    elif selected_month == 4:
        days_of_the_month = 31
        start_index = (start_day_calc - 1) % len(week_days)
    elif selected_month == 5:
        days_of_the_month = 32
        start_index = (start_day_calc + 1) % len(week_days)
    elif selected_month == 6:
        days_of_the_month = 31
        start_index = (start_day_calc - 3) % len(week_days)
    elif selected_month == 7:
        days_of_the_month = 32
        start_index = (start_day_calc - 1) % len(week_days)
    elif selected_month == 8:
        days_of_the_month = 32
        start_index = (start_day_calc + 2) % len(week_days)
    elif selected_month == 9:
        days_of_the_month = 31
        start_index = (start_day_calc - 2) % len(week_days)
    elif selected_month == 10:
        days_of_the_month = 32
        start_index = start_day_calc % len(week_days)
    elif selected_month == 11:
        days_of_the_month = 31
        start_index = (start_day_calc + 3) % len(week_days)
    elif selected_month == 12:
        days_of_the_month = 32
        start_index = (start_day_calc + 5) % len(week_days)

    month_days = list(range(1, days_of_the_month))

    # Criando a lista de dias da semana a partir do index definido
    great_week_days = week_days[start_index:] + week_days[:start_index]

    # Repetindo os dias da semana conforme necessário para cobrir todos os dias do mês
    great_week_days = great_week_days * ((len(month_days) // len(week_days)) + 1)

    # Cortando a lista para ter o mesmo tamanho que month_days
    great_week_days = great_week_days[:len(month_days)]

    # Unindo dias da semana com os dias do mês
    month_and_week_days = list(zip(great_week_days, month_days))

    # print(f'Leap Year Quantity: {leap_year_quantity} | ', f'Is Leap Year?: {is_bissexto} | ',
    #       f'Year selected: {selected_year} | ', f'Init day: {start_index} | ',
    #       f'Month selected: {selected_month}'
    # print(month_and_week_days)

    return month_and_week_days
