"""test"""
def main(blood):
    """long"""
    blood_table = [["A", ["AA", "AO"]], ["B", ["BB", "BO"]], ["AB", ["AB"]], ["O", ["OO"]]]
    brute_force = ""
    if blood[-1] == "?":
        blood_data = [i for i in blood_table if i[0]+"+" in blood or i[0]+"-" in blood]
        print(" ".join(blood).replace("?", blood_print(blood_cal(blood_data, blood[0], blood[1]))))
    elif blood[1] == "?":
        brute_force = find_blood(blood_table, blood)
        if brute_force != []:
            return print(" ".join(blood).replace("?", blood_print(brute_force)))
        print(" ".join(blood).replace("?", "IMPOSSIBLE"))
    elif blood[0] == "?":
        blood[0], blood[1] = blood[1], blood[0]
        brute_force = find_blood(blood_table, blood)
        blood[1], blood[0] = blood[0], blood[1]
        if brute_force != []:
            return print(" ".join(blood).replace("?", blood_print(brute_force)))
        print(" ".join(blood).replace("?", "IMPOSSIBLE"))
 
def blood_cal(blood_data, father, mother):
    """very long"""
    father_data = rh_types([i[1] for i in blood_data if i[0] == father[:-1]], father[-1])
    mother_data = rh_types([i[1] for i in blood_data if i[0] == mother[:-1]], mother[-1])
    return mix_blood(father_data, mother_data)
def rh_types(blood_data, types):
    """very very very longgggg"""
    rh_type = ["++", "+-", "-+", "--"]
    new_blood_data = []
    for blood_pack in blood_data:
        for blood_pair in blood_pack:
            if types == "+":
                new_blood_data += [[blood_pair[0]+rh_type[0][0], blood_pair[1]+rh_type[0][1]]]
                new_blood_data += [[blood_pair[0]+rh_type[1][0], blood_pair[1]+rh_type[1][1]]]
                new_blood_data += [[blood_pair[0]+rh_type[2][0], blood_pair[1]+rh_type[2][1]]]
            else:
                new_blood_data += [[blood_pair[0]+rh_type[3][0], blood_pair[1]+rh_type[3][1]]]
    return new_blood_data
 
 
def mix_blood(father, mother):
    """very very long"""
    blood_table = [["A", ["AA", "AO"]], ["B", ["BB", "BO"]], ["AB", ["AB"]], ["O", ["OO"]]]
    blood_mix_data = set()
    blood_result = []
    blood_template = []
    for i in father:
        for j in mother:
            blood_mix_data.add(("".join(sorted(list(i[0]+j[0])))))
            blood_mix_data.add(("".join(sorted(list(i[0]+j[1])))))
            blood_mix_data.add(("".join(sorted(list(i[1]+j[0])))))
            blood_mix_data.add(("".join(sorted(list(i[1]+j[1])))))
    for i in blood_mix_data:
        if i[:2] == "--":
            for j in blood_table:
                if i[2:] in j[1]:
                    blood_result.append(j[0]+"-")
                    break
        else:
            for j in blood_table:
                if i[2:] in j[1]:
                    blood_result.append(j[0]+"+")
    blood_template += ["A+"]*("A+" in blood_result)+["A-"]*("A-" in blood_result)
    blood_template += ["B+"]*("B+" in blood_result)+["B-"]*("B-" in blood_result)
    blood_template += ["AB+"]*("AB+" in blood_result)+["AB-"]*("AB-" in blood_result)
    blood_template += ["O+"]*("O+" in blood_result)+["O-"]*("O-" in blood_result)
    return blood_template
def blood_print(data, blood_ans=""):
    """very very very long"""
    for i in data:
        blood_ans += i+" "
    return "{"+blood_ans[:-1]+"}"
def find_blood(blood_table, blood):
    """very very very very long"""
    brute_force = []
    for j in blood_table:
        blood_data = [i for i in blood_table if i[0]+"+" in blood[:2] or i[0]+"-"\
        in blood[:2] or j[0] == i[0]]
        chk1 = blood[2] in blood_cal(blood_data, blood[0], j[0]+"+")
        chk2 = blood[2] in blood_cal(blood_data, blood[0], j[0]+"-")
        brute_force += [j[0]+"+"]*chk1+[j[0]+"-"]*chk2
    return brute_force
main(input().split())
