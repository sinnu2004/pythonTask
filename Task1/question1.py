# # Print the following strings in the format shown below.
# Given Strings: "Data" "Science" "Mentorship" "Program" "By" "CWS"
# Expected Output: Data-Science-Mentorship-Program-started-By-CWS
# Concept: Separator (sep) and End (end) parameters in the print() function.


my_list = ["Data", "Science","Mentorship","Program","By","CWS"]

for i in range(0,len(my_list)):
    print(my_list[i],end="-")  # using separator and end parameter
