import matplotlib.pyplot as plt
import matplotlib

# Measurements

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
# filename = "Industry.log"            # 4421
# filename = "Entity_Dataset_2k.log"   # 3429

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
# filename = "Entity_Dataset_2k.log"   # 93


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
# filename = "Entity_Dataset_2k.tx     # 181
#164

# char level and word level
plt.plot([46], [874], 'lightcoral',  marker="^", markersize=11, label="Apache") # Apache_2k
plt.plot([75], [2068], 'springgreen',  marker='v', markersize=11, label="BGL") # BGL_2k
plt.plot([56], [3599], 'mediumorchid',  marker='X', markersize=11, label="HDFS") # HDFS_2k
plt.plot([71], [1512], 'maroon',  marker='d', markersize=11, label="HealthApp") # HealthApp_2k
plt.plot([65], [510], 'goldenrod',  marker='.', markersize=11, label="HPC") # HPC_2k
plt.plot([90], [2981], 'darkorange',  marker='*', markersize=11, label="Mac") # Mac_2k
plt.plot([72], [1445], 'aquamarine',  marker='>', markersize=11, label="OpenStack") # OpenStack_2k
plt.plot([70], [1970], 'teal',  marker='o', markersize=11, label="Spark") # Spark_2k
plt.plot([82], [1206], 'olive',  marker='h', markersize=11, label="Windows") # Windows_2k
plt.plot([91], [3123], 'mediumturquoise',  marker='P', markersize=11, label="Combined") # Combined_2k
plt.plot([92], [4421], 'gold',  marker='8', markersize=11, label="Industry") # Industry_2k
plt.plot([93], [3429], 'royalblue',  marker='s', markersize=11, label="Entity") # Entity_2k

plt.axis([0, 100, 0, 4550])
plt.xlabel("Unique number of characters")
plt.ylabel("Unique number of words")
plt.legend(loc="upper left")
plt.savefig('entity_1.pdf')
plt.show()

# number of chars per line and words
plt.plot([9], [874], 'lightcoral',  marker="^", markersize=11, label="Apache") # Apache_2k
plt.plot([114], [2068], 'springgreen',  marker='v', markersize=11, label="BGL") # BGL_2k
plt.plot([59], [3599], 'mediumorchid',  marker='X', markersize=11, label="HDFS") # HDFS_2k
plt.plot([55], [1512], 'maroon',  marker='d', markersize=11, label="HealthApp") # HealthApp_2k
plt.plot([50], [510], 'goldenrod',  marker='.', markersize=11, label="HPC") # HPC_2k
plt.plot([186], [2981], 'darkorange',  marker='*', markersize=11, label="Mac") # Mac_2k
plt.plot([50], [1445], 'aquamarine',  marker='>', markersize=11, label="OpenStack") # OpenStack_2k
plt.plot([63], [1970], 'teal',  marker='o', markersize=11, label="Spark") # Spark_2k
plt.plot([66], [1206], 'olive',  marker='h', markersize=11, label="Windows") # Windows_2k
plt.plot([157], [3123], 'mediumturquoise',  marker='P', markersize=11, label="Combined") # Combined_Dataset_2k
plt.plot([181], [4421], 'gold',  marker='8', markersize=11, label="Industry") # Industry_2k
plt.plot([181], [3429], 'royalblue',  marker='s', markersize=11, label="Entity") # Entity_2k

plt.axis([0, 200, 0, 4550])
plt.xlabel("Unique number of log lines' character length")
plt.ylabel("Unique number of words")
plt.legend(loc="upper left")
plt.savefig('entity_2.pdf')
plt.show()

# number of chars per line and number
plt.plot([9], [46], 'lightcoral',  marker="^", markersize=11, label="Apache") # Apache_2k
plt.plot([114], [75], 'springgreen',  marker='v', markersize=11, label="BGL") # BGL_2k
plt.plot([59], [56], 'mediumorchid',  marker='X', markersize=11, label="HDFS") # HDFS_2k
plt.plot([55], [71], 'maroon',  marker='d', markersize=11, label="HealthApp") # HealthApp_2k
plt.plot([50], [65], 'goldenrod',  marker='.', markersize=11, label="HPC") # HPC_2k
plt.plot([186], [90], 'darkorange',  marker='*', markersize=11, label="Mac") # Mac_2k
plt.plot([50], [72], 'aquamarine',  marker='>', markersize=11, label="OpenStack") # OpenStack_2k
plt.plot([63], [70], 'teal',  marker='o', markersize=11, label="Spark") # Spark_2k
plt.plot([66], [82], 'olive',  marker='h', markersize=11, label="Windows") # Windows_2k
plt.plot([157], [91], 'mediumturquoise',  marker='P', markersize=11, label="Combined") # Combined_Dataset_2k
plt.plot([181], [92], 'gold',  marker='8', markersize=11, label="Industry") # Industry_2k
plt.plot([181], [93], 'royalblue',  marker='s', markersize=11, label="Entity") # Entity_2k

plt.axis([0, 200, 0, 100])
plt.xlabel("Unique number of log lines' character length")
plt.ylabel("Unique number of characters")
plt.legend(loc="lower right")
plt.savefig('entity_3.pdf')
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
print("words", filename, len(res.keys()))

res_chars = Counter(chars_for_histogram)
print("chars", filename, len(res_chars.keys()))

res_number_of_chars = Counter(num_of_chars_for_histogram)
print("numbers", filename, len(res_number_of_chars.keys()))

import collections
x = collections.Counter(listofnames)
l = range(len(x.keys()))
plt.bar(l, x.values(), align='center')
plt.xticks(l, x.keys())
plt.xticks(rotation=45)
