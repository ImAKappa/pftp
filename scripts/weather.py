weather = "raining"
has_umbrella = False
my_fav_show = "ATLA"

print(f"The weather outside is {weather}")

if weather == "sunny" or (weather == "raining" and has_umbrella):
    print("I'm going for a nice walk outside")
else:
    print(f"Yeah, no, I'm staying inside and watching {my_fav_show} today")