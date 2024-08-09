days_of_the_month = 0
start_index = 0

start_year = 2024
selected_year = int(input('Escreva o ano: '))

bissextos_quantity_modified = (selected_year - 2021) // 4
bissextos_quantity = (selected_year - 2020) // 4

is_bissexto = selected_year % 4 == 0

week_days = ['seg', 'ter', 'qua', 'qui', 'sex', 'sáb', 'dom']

start_day_calc_modified = (bissextos_quantity_modified + (selected_year - start_year)) % len(week_days)
start_day_calc = (bissextos_quantity + (selected_year - start_year)) % len(week_days)

selected_month = int(input('Escreva o número do mês: '))

if selected_month == 1:
    days_of_the_month = 32
    start_index = start_day_calc_modified % len(week_days)
elif selected_month == 2:
    days_of_the_month = 30 if is_bissexto else 29
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

print(f'Quantidade de bissextos: {bissextos_quantity} | ', f'É bissexto?: {is_bissexto} | ',
      f'Ano selecionado: {selected_year} | ', f'Dia de início: {start_index} | ', f'Mês selecionado: {selected_month}')

month_days = list(range(1, days_of_the_month))

# Criando a lista de dias da semana a partir do index definido
great_week_days = week_days[start_index:] + week_days[:start_index]

# Repetindo os dias da semana conforme necessário para cobrir todos os dias do mês
great_week_days = great_week_days * ((len(month_days) // len(week_days)) + 1)

# Cortando a lista para ter o mesmo tamanho que month_days
great_week_days = great_week_days[:len(month_days)]

# Unindo dias da semana com os dias do mês
month_and_week_days = list(zip(great_week_days, month_days))

print(month_and_week_days)
