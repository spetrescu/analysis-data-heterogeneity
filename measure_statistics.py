import matplotlib.pyplot as plt
import matplotlib

# word level
# filename = "Apache_2k.log"           # 874
# filename = "BGL_2k.log"              # 2068
# filename = "Combined_Dataset_2k.log" # 3123
# filename = "HDFS_2k.log"             # 3599
# filename = "HealthApp_2k.log"        # 1512
# filename = "HPC_2k.log"              # 510
# filename = "Mac_2k.log"              # 2981
# filename = "OpenStack_2k.log"        # 1445
# filename = "Spark_2k.log"            # 1970
# filename = "Windows_2k.log"          # 1206
# filename = "Industry_Dataset.log"    # 874

# char level
# filename = "Apache_2k.log"           # 46
# filename = "BGL_2k.log"              # 75
# filename = "Combined_Dataset_2k.log" # 91
# filename = "HDFS_2k.log"             # 56
# filename = "HealthApp_2k.log"        # 71
# filename = "HPC_2k.log"              # 65
# filename = "Mac_2k.log"              # 90
# filename = "OpenStack_2k.log"        # 72
# filename = "Spark_2k.log"            # 70
# filename = "Windows_2k.log"          # 82

# number of chars per line level
# filename = "Apache_2k.log"           # 9
# filename = "BGL_2k.log"              # 114
# filename = "Combined_Dataset_2k.log" # 157
# filename = "HDFS_2k.log"             # 59
# filename = "HealthApp_2k.log"        # 55
# filename = "HPC_2k.log"              # 50
# filename = "Mac_2k.log"              # 186
# filename = "OpenStack_2k.log"        # 50
# filename = "Spark_2k.log"            # 63
# filename = "Windows_2k.log"          # 66

# char level and word level
plt.plot([46], [874], 'purple',  marker=11, markersize=13, label="Apache_2k") # Apache_2k
plt.plot([75], [2068], 'blue',  marker=11, markersize=13, label="BGL_2k") # BGL_2k
plt.plot([91], [3123], 'orange',  marker=11, markersize=13, label="Combined_Dataset_2k") # Combined_Dataset_2k
plt.plot([56], [3599], 'green',  marker=11, markersize=13, label="HDFS_2k") # HDFS_2k
plt.plot([71], [1512], 'red',  marker=11, markersize=13, label="HealthApp_2k") # HealthApp_2k
plt.plot([65], [510], 'brown',  marker=11, markersize=13, label="HPC_2k") # HPC_2k
plt.plot([90], [2981], 'pink',  marker=11, markersize=13, label="Mac_2k") # Mac_2k
plt.plot([72], [1445], 'gray',  marker=11, markersize=13, label="OpenStack_2k") # OpenStack_2k
plt.plot([70], [1970], 'olive',  marker=11, markersize=13, label="Spark_2k") # Spark_2k
plt.plot([82], [1206], 'cyan',  marker=11, markersize=13, label="Windows_2k") # Windows_2k

plt.axis([0, 100, 0, 3650])
plt.xlabel("Number of unique characters")
plt.ylabel("Number of unique words")
plt.legend(loc="upper left")
plt.savefig('diagram_1.pgf')
plt.savefig('diagram_2.pdf')
plt.show()

# number of chars per line and words
plt.plot([9], [874], 'purple',  marker=11, markersize=13, label="Apache_2k") # Apache_2k
plt.plot([109], [2068], 'blue',  marker=11, markersize=13, label="BGL_2k") # BGL_2k
plt.plot([157], [3123], 'orange',  marker=11, markersize=13, label="Combined_Dataset_2k") # Combined_Dataset_2k
plt.plot([59], [3599], 'green',  marker=11, markersize=13, label="HDFS_2k") # HDFS_2k
plt.plot([55], [1512], 'red',  marker=11, markersize=13, label="HealthApp_2k") # HealthApp_2k
plt.plot([50], [510], 'brown',  marker=11, markersize=13, label="HPC_2k") # HPC_2k
plt.plot([186], [2981], 'pink',  marker=11, markersize=13, label="Mac_2k") # Mac_2k
plt.plot([50], [1445], 'gray',  marker=11, markersize=13, label="OpenStack_2k") # OpenStack_2k
plt.plot([63], [1970], 'olive',  marker=11, markersize=13, label="Spark_2k") # Spark_2k
plt.plot([66], [1206], 'cyan',  marker=11, markersize=13, label="Windows_2k") # Windows_2k

plt.axis([0, 200, 0, 3650])
plt.xlabel("Number of unique length log lines")
plt.ylabel("Number of unique words")
plt.legend(loc="lower right")
plt.savefig('uql_uqw.pdf')
plt.show()

# number of chars per line and number
plt.plot([9], [46], 'purple',  marker=11, markersize=13, label="Apache_2k") # Apache_2k
plt.plot([114], [75], 'blue',  marker=11, markersize=13, label="BGL_2k") # BGL_2k
plt.plot([157], [91], 'orange',  marker=11, markersize=13, label="Combined_Dataset_2k") # Combined_Dataset_2k
plt.plot([59], [56], 'green',  marker=11, markersize=13, label="HDFS_2k") # HDFS_2k
plt.plot([55], [71], 'red',  marker=11, markersize=13, label="HealthApp_2k") # HealthApp_2k
plt.plot([50], [65], 'brown',  marker=11, markersize=13, label="HPC_2k") # HPC_2k
plt.plot([186], [90], 'pink',  marker=11, markersize=13, label="Mac_2k") # Mac_2k
plt.plot([50], [72], 'gray',  marker=11, markersize=13, label="OpenStack_2k") # OpenStack_2k
plt.plot([63], [70], 'olive',  marker=11, markersize=13, label="Spark_2k") # Spark_2k
plt.plot([66], [82], 'cyan',  marker=11, markersize=13, label="Windows_2k") # Windows_2k

plt.axis([0, 200, 0, 100])
plt.xlabel("Number of unique length log lines")
plt.ylabel("Number of unique characters")
plt.legend(loc="lower right")
plt.savefig('chars_numbers.pdf')
plt.show()

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

all_words = []
all_chars = []
all_num_of_chars = []

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

for line in lines:
    words = line.split(" ")
    chars = list(line)
    number = len(line)
    all_words.append(words)
    all_chars.append(chars)
    all_num_of_chars.append(number)

words_for_histogram = []
chars_for_histogram = []
num_of_chars_for_histogram = []

for line in all_words:
    for word in line:
        words_for_histogram.append(word)

for line in all_chars:
    for char in line:
        chars_for_histogram.append(char)

for number in all_num_of_chars:
    num_of_chars_for_histogram.append(number)

listofnames = words_for_histogram

from collections import Counter
res = Counter(listofnames)
print(res)
print("words", filename, len(res.keys()))

res_chars = Counter(chars_for_histogram)
print(res_chars)
print("chars", filename, len(res_chars.keys()))

res_number_of_chars = Counter(num_of_chars_for_histogram)
print(res_number_of_chars)
print("numbers", filename, len(res_number_of_chars.keys()))

import collections
x = collections.Counter(listofnames)
l = range(len(x.keys()))
plt.bar(l, x.values(), align='center')
plt.xticks(l, x.keys())
plt.xticks(rotation=45)
# plt.show()


# listofnames = chars_for_histogram

# from collections import Counter
# res = Counter(listofnames)
# print(res)
# print(filename, len(res.keys()))

# import collections
# x = collections.Counter(listofnames)
# l = range(len(x.keys()))
# plt.bar(l, x.values(), align='center')
# plt.xticks(l, x.keys())
# plt.xticks(rotation=45)