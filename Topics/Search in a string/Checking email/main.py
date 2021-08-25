def check_email(string):
    if (" " in string) or ("@" not in string) or ("@." in string) or (".@" in string):
        return False
    else:
        poz1 = string.find("@")
        poz2 = string.find(".", poz1)
        return bool(poz2 > poz1)
