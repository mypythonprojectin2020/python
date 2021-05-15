def get_data(file):
    file = open(file)
    lines = file.readlines()
    file.close()
    return [line.strip() for line in lines]
    
def write_data(file_name, score):
    f = open(file_name, "w")
    f.write(score)
    f.close()
