def tiraAcento(string):
    return string.encode("ascii", "ignore").decode("utf8").casefold()

def anagrama(string):
    string = tiraAcento(string.upper())
    reverse = string[::-1]
    print(string,reverse)
    if string == reverse:
        return True
    return False

print(anagrama("america"))