import time

def memozex(val):

    ef_cache = {}
    
    if val in ef_cache:
        return ef_cache[val]
    print("computing...{}".format(val))
    time.sleep(1)
         
    result= val * val
    ef_cache[val] = result
    return result


print(memozex(4))
print(memozex(5))
print(memozex(4))
print(memozex(5))
