def override(l1, l2):
    override_list = l1 + l2
    for idx1, i in enumerate(l1):
        for idx2, j in enumerate(l2):
            if i[0] == j[0]:
                override_list.remove(i)   
    return sorted(override_list)