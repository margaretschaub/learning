# #task 1 add all dict values
#
# toys = {"robot": "$40.0", "car":"$25","ironman":"$12"}
#
# new_list = list(toys.values())
#
# new_list = [i.replace("$","") for i in new_list] # or list(toys.values())[0][1:]
# print(new_list)
#
# print(eval(new_list[0])+eval(new_list[1])+eval(new_list[2]))
# #desired output = 77


#task 2 use comparison operators in a list
#
# questions = [10 != 4, 50 == 50, 90 == 10, "c" in ("a","b","c"), 100 != 100]
# # ! =
# # ==
# # in
# desired output True, True, False, True, False
#
# print(questions)


#task 3
# films = {"k1":"blade runner 2049", "k2":"matrix", "k3":"terminator"}
# print(len(films["k1"])>len(films["k3"])>len(films["k2"]))


#task 4: update dictionary
# life_stages = {0:"embryo", 1:"fetus", 2:"baby",3:"infant", 4:"teen"}
# #desired output: add 5: adult, 6:big kid
#
# mid_life = {5: "adult", 6:"big kid"}
# life_stages.update(mid_life)
# print(life_stages)


# #tast 5 add  all values from list
# nest1 = [(1,2,3),{"k1":[8,1,300,2,77],"k2":[10,20,30]},["a","500","c"]]
# #sorted(), eval desired output 833.0 (add 3,300,30,500)
# k1 = sorted(nest1[1]["k1"])[-1]
# k2 = nest1[1]["k2"][-1]
# print(float((nest1[0][2]) + k1 + k2 + eval(nest1[2][1])))

