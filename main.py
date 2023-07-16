def currentSpeed(bse_atk_spd, bns_atk_spd, lvl):
    crt_spd = bse_atk_spd * (1 * (bns_atk_spd * (lvl - 1)))
    crt_spd = round(crt_spd, 3)
    print("")
    print("The character's current attack speed is " + str(crt_spd) + ".")

baseAttackSpeed = float(input("Enter the base attack speed: "))
bonusAttackSpeed = float(input("Enter the bonus attack speed %: "))
level = int(input("Enter the character's current level: "))
convertedToDecimal = bonusAttackSpeed / 100
currentSpeed(baseAttackSpeed, convertedToDecimal, level)