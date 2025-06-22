COLOUR_CODES = {"aliceblue":"#f0f8ff","amber":"#ffbf00","black":"#000000",
                "blond":"#faf0be","camel":"#c19a6b","darkgreen":"#006400",
                "ebony":"#555d50","eminence":"#6c3082","fawn":"#e5aa70","zomp":"#39a78e"}
colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()