#!/usr/bin/env python3

#creating  sample lists
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
proto.insert(2, "Cowabunga") # inserts "Cowabunga: into index 2 
protoa.pop() # removes last item in list
print(proto)
print(protoa)
