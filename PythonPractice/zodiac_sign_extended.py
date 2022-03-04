def get_zodiac_sign(month_of_birth, day_of_birth): # please don't change
	# your code here should return a string back. For example: return "Scorpio"
    if "Dec" in month_of_birth.title():
        if day_of_birth < 22:
            return "Sagittarius"
        else:
            return "Capricorn"
    elif "Jan" in month_of_birth.title():
        if day_of_birth < 20:
            return "Capricorn"
        else:
            return "Aquarius"
    elif "Feb" in month_of_birth.title():
        if day_of_birth < 19:
            return "Aquarius"
        else:
            return "Pisces"
    elif "Mar" in month_of_birth.title():
        if day_of_birth < 21:
            return "Pisces"
        else:
            return "Aries"
    elif "Apr" in month_of_birth.title():
        if day_of_birth < 20:
            return "Aries\n Sun: Independent\n Moon: Inexhuastable\n Rising: Daredevil"
        else:
            return "Taurus"
    elif "May" in month_of_birth.title():
        if day_of_birth < 21:
            return "Taurus"
        else:
            return "Gemini"
    elif "Jun" in month_of_birth.title():
        if day_of_birth < 21:
            return "Gemini"
        else:
            return "Cancer"
    elif "Jul" in month_of_birth.title():
        if day_of_birth < 23:
            return "Cancer"
        else:
            return "Leo"
    elif "Aug" in month_of_birth.title():
        if day_of_birth < 23:
            return "Leo"
        else:
            return "Virgo"
    elif "Sep" in month_of_birth.title():
        if day_of_birth < 23:
            return "Virgo"
        else:
            return "Libra"
    elif "Oct" in month_of_birth.title():
        if day_of_birth < 23:
            return "Libra"
        else:
            return "Scorpio"
    elif "Nov" in month_of_birth.title():
        if day_of_birth < 22:
            return "Scorpio"
        else:
            return "Sagittarius"
        

if __name__ == "__main__":
    # Read from user here
    day_of_birth = int(input("What is the date of your birth? "))
    month_of_birth = input("What's your birth month? ")
    zodiac_sign = get_zodiac_sign(month_of_birth, day_of_birth)
    if zodiac_sign:
        print(f"Wow! Ccongrats, you're a {zodiac_sign}... so special cool")
    else:
        print("invalid response")