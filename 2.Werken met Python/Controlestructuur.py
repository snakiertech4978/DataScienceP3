def zouk (element, lijst):
    if len(lijst)==0:
        return False
    else:
        for d in lijst:
            if d == element:
                return True
        return False

for i in range(0,10):

