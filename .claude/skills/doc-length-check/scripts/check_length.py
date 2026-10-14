import re
import sys

path = sys.argv[1]
text = open(path).read()
body = re.sub(r"^---.*?---\n", "", text, flags=re.S)
clean = re.sub(r"[#*_`]", "", body)

print("chars:", len(clean))
print("words:", len(re.findall(r"\b\w+\b", body)))
print("em_dash_count:", body.count("—"))
