import random

def random_from_list(list):
    if(len(list)==0): return None
    return random.choice(list)

if __name__=="__main__":
    list = [1,2,3,4,5];
    print("list of {} return: {}".format(list,random_from_list(list)))
    print("emty list return {}".format (random_from_list([])))
