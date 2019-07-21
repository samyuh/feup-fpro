def flatten(alist):
    for idx, element in enumerate(alist):
        if type(element) is list:
            alist.remove(element)
            for item in element:
                alist.insert(idx, item)
                idx += 1
            return flatten(alist)   
    return alist

def file_finder(dirs, file_name):
    if file_name == dirs[0]:
        return
    
    if (file_name in dirs):
        directory = [(dirs[0]), (file_name)]
        return "/".join(directory)
    
    for sub_dirs in dirs:
        directory = [dirs[0],]         
        if type(sub_dirs) is list:
            local = file_finder(sub_dirs, file_name)
            directory += [(local),]
            if local != None:
                flatten(directory)
                return "/".join(directory)
            del directory[-1]