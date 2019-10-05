# Вы - водитель грузовика с открытым кузовом. В кузове два груза:
# пианино и холодильник. Пианино необходимо доставить в институт, холодильник в общежитие.
# В каждое из этих мест ведет отдельная дорога, начинающаяся от перекрестка, на котором
# Вы стоите, других дорог в мире нет. Известно, что по дороге в институт есть мост, на котором действует ограничение
# максимальной допустимой массы автомобиля с грузом, а по дороге в общежитие есть туннель с ограничением высоты.
# Требуется определить, возможно ли доставить грузы или нет (разумеется, сгружать их, где попало, Вам запрещено).

# вес грузовика без груза, высота платформы кузова (на которой стоят грузы),
# вес пианино, высота пианино, вес холодильника, высота холодильника, максимальный
# допустимый вес на мосту, максимальная допустимая высота в туннеле

def transport(lorry_mass, platform_height, piano_mass, piano_height, fridge_mass, fridge_height, max_mass, max_height):
    # Случай, когда высота холодильника с платформой превышает высоту туннеля
    if fridge_height + platform_height > max_height:
        print("NO")
        return
    # Случай, когда масса грузовика с пианино превышает массу моста
    if piano_mass + lorry_mass > max_mass:
        print("NO")
        return
    if piano_height + platform_height > max_height:
        if lorry_mass + piano_mass + fridge_mass <= max_mass:
            print("YES")
            return
        else:
            print("NO")
            return
    print("YES")

lorry_mass = int(input())       #1
platform_height = int(input())  #1
piano_mass = int(input())       #5
piano_height = int(input())     #10
fridge_mass = int(input())      #5
fridge_height = int(input())    #7
max_mass = int(input())         #11
max_height = int(input())       #10

transport(lorry_mass, platform_height, piano_mass, piano_height, fridge_mass, fridge_height, max_mass, max_height)