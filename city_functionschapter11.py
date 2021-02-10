def city_function(city,country,population=''):
	"""Display the location information."""
	if population:
		location = f"{city.title()}, {country.title()} - population {population}"
	else:
		location = f"{city.title()}, {country.title()}"	
	return location	
	