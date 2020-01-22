import requests

import shutil

def getimage(url, dest):
	resp = requests.get(url, stream=True)
	local_file = open(dest, 'wb')
	resp.raw.decode_content = True
	shutil.copyfileobj(resp.raw, local_file)
	del resp

#Regular Pokemon
pokelist = open("pokemon_list.txt", "r")
for line in pokelist:
	line = line.rstrip("\n\r")
	line = line.lower()
	if (line.strip("+").encode("ascii", errors="ignore").decode() == "sirfetchd"):
		imgname = "sirfetch’d"
	elif (line.strip("+").encode("ascii", errors="ignore").decode() == "mr.-mime"):
		imgname = "mr._mime"
	else:
		imgname = line.strip("+").encode("ascii", errors="ignore").decode()
	#Regular
	image_url = "https://projectpokemon.org/images/normal-sprite/" + imgname + ".gif"
	name = "pokemon_" + line.strip("+").replace(" ", "_").replace("-", "_").replace(".", "")
	name = name.encode("ascii", errors="ignore").decode()
	getimage(image_url, name + ".gif")

	#Shiny
	image_url = "https://projectpokemon.org/images/shiny-sprite/" + imgname + ".gif"
	name += "_shiny"
	getimage(image_url, name + ".gif")

	#Pokemon with alternate forms
	if (line[0] == "+"):
		formlist = open(line[1:] + ".txt", "r")
		for form in formlist:
			form = form.rstrip("\n\r")
			form = form.lower()

			#Regular
			image_url = "https://projectpokemon.org/images/normal-sprite/" + form + ".gif"
			subname = "pokemon_" + form.replace("-", "_")
			getimage(image_url, subname + ".gif")

			#Shiny
			image_url = "https://projectpokemon.org/images/shiny-sprite/" + form + ".gif"
			subname += "_shiny"
			getimage(image_url, subname + ".gif")
		formlist.close()
pokelist.close()

#Alola Pokemon
alolalist = open("alola_list.txt", "r")
for line in alolalist:
	line = line.rstrip("\n\r")
	line = line.lower()
	name = "pokemon_" + line.replace("-", "_").replace(".", "") + "_alola"
	line += "-alola"
	#Regular
	image_url = "https://projectpokemon.org/images/normal-sprite/" + line + ".gif"
	getimage(image_url, name + ".gif")

	#Shiny
	name += "_shiny"
	image_url = "https://projectpokemon.org/images/shiny-sprite/" + line + ".gif"
	getimage(image_url, name + ".gif")
alolalist.close()

#Galar Pokemon
galarlist = open("galar_list.txt", "r")
for line in galarlist:
	line = line.rstrip("\n\r")
	line = line.lower()
	name = "pokemon_" + line.replace("-", "_").replace(".", "") + "_galar"
	line += "-galar"
	#Regular
	image_url = "https://projectpokemon.org/images/normal-sprite/" + line + ".gif"
	getimage(image_url, name + ".gif")

	#Shiny
	name += "_shiny"
	image_url = "https://projectpokemon.org/images/shiny-sprite/" + line + ".gif"
	getimage(image_url, name + ".gif")
galarlist.close()

gigantamaxlist = open("gigantamax_list.txt", "r")
for line in gigantamaxlist:
	line = line.rstrip("\n\r")
	line = line.lower()
	name = "pokemon_" + line.replace("-", "_").replace(".", "") + "_gigantamax"
	line += "-gigantamax"
	#Regular
	image_url = "https://projectpokemon.org/images/normal-sprite/" + line + ".gif"
	getimage(image_url, name + ".gif")

	#Shiny
	name += "_shiny"
	image_url = "https://projectpokemon.org/images/shiny-sprite/" + line + ".gif"
	getimage(image_url, name + ".gif")
gigantamaxlist.close()

megalist = open("mega_list.txt", "r")
for line in megalist:
	line = line.rstrip("\n\r")
	line = line.lower()
	name = "pokemon_" + line.replace("-", "").replace(".", "") + "_mega"
	line += "-mega"
	#Regular
	image_url = "https://projectpokemon.org/images/normal-sprite/" + line + ".gif"
	getimage(image_url, name + ".gif")

	#Shiny
	name += "_shiny"
	image_url = "https://projectpokemon.org/images/shiny-sprite/" + line + ".gif"
	getimage(image_url, name + ".gif")
megalist.close()

megalistweird = open("mega_weird_list.txt")
for line in megalistweird:
	line = line.rstrip("\n\r")
	line = line.lower()
	name = "pokemon_" + line.replace("-", "_")
	#Regular
	image_url = "https://projectpokemon.org/images/normal-sprite/" + line + ".gif"
	getimage(image_url, name + ".gif")

	#Shiny
	name += "_shiny"
	image_url = "https://projectpokemon.org/images/shiny-sprite/" + line + ".gif"
	getimage(image_url, name + ".gif")
megalistweird.close()