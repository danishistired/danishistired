import glob
import re

# Find every headerXX.jpg
headers = sorted(
    glob.glob("header*.jpg"),
    key=lambda x: int(re.search(r'(\d+)', x).group())
)

if not headers:
    raise Exception("No header images found.")

# Read current position
try:
    with open(".header_state") as f:
        current = int(f.read().strip())
except:
    current = 0

next_index = (current + 1) % len(headers)

# Save next state
with open(".header_state", "w") as f:
    f.write(str(next_index))

# Update README
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = re.sub(
    r'header\d+\.jpg',
    headers[next_index],
    readme
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print(f"Switched to {headers[next_index]}")