#LIST OF CARS AND PRICES FOR A COMPANY


cars=('toyota matrix','toyota avalon','honda accord','honda cr-v','kia sportage',
      'kia optima','hyundai sonata','hyundai accent','hyundai genesis','hyundai tucsun',
      'nissan navara','nissan frontier','nissan altima','nissan pathfinder','toyota corolla',
      'toyota camry','honda civic','honda accord','honda pilot','honda odyssey',
      'audi a6','audi a4','porche cayenne','jeep compass','tesla model x','tesla model s',
      'lamorghhini venono','bugatti chiron','bmw','ferrari superfast')

#the cars with their corresponding prizes
CarsWithPrices={'toyota matrix':6800,'toyota avalon':8700,'honda cr-v':6500,'kia sportage':9000,
      'kia optima':3400,'hyundai sonata':8700,'hyundai accent':9500,'hyundai genesis':8300,'hyundai tucsun':7500,
      'nissan navara':5400,'nissan frontier':8700,'nissan altima':9000,'nissan pathfinder':8700,'toyota corolla':9400,
      'toyota camry':5700,'honda civic':8400,'honda accord':6700,'honda pilot':9100,'honda odyssey':8300,
      'audi a6':8300,'audi a4':7400,'porche cayenne':8500,'jeep compass':9400,'tesla model x':11000,'tesla model s':15000,
      'lamorghhini venono':17000,'bugatti chiron':16500,'bmw':67009,'ferrari superfast':18000}

#BELOW SHOWS THE PROGRAMMING FOR THE SHOP
print('please this shows the types of cars we have, '+str(cars))

CarName=input("what brand of car do you want?: ")

if CarName in CarsWithPrices:
         print('we have this car. the price of '+CarName+' is $'+str(CarsWithPrices[CarName]))
while CarName not in cars:
    print(CarName=input('sorry we do not have this car: '))
    if input in cars:
        print(input('what brand do you want?: '))
format(CarName)