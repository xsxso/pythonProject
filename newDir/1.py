

INPUT_FILE = "1.txt"
OUPUT_FILE = "2.txt"

with open(INPUT_FILE) as f:
    with open(OUPUT_FILE, "wt") as g:
        for line in f:
            words = line.split()  # list of words
            for w in words:
                w = w.upper()
                g.write(w + " ")
            g.write("\n")

print("End")

