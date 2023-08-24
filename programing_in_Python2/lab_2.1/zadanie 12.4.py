def metr_to_km (meters):
    km=meters*0.001
    return km
hightOfFlight=int(input("Na jakiej wysokości lecimy? [w metrach]: "))
hightOfFlight=metr_to_km(hightOfFlight)
if hightOfFlight<5:
    print(hightOfFlight,"to za nisko")
else:
    print("„Na tej wysokości jesteś już bezpieczny")