SELECT city_data.year, city_data.avg_temp CITY_TEMP, global_data.avg_temp GLOBAL_TEMP FROM city_data 
INNER JOIN global_data ON city_data.year = global_data.year WHERE city = 'Miami'