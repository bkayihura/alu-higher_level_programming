#!/bin/bash

# 1. Create Task 0
cat << 'EOF' > 0-run
#!/bin/bash
python3 "$PYFILE"
EOF

# 2. Create Task 1
cat << 'EOF' > 1-run_inline
#!/bin/bash
python3 -c "$PYCODE"
EOF

# 3. Create Task 2
cat << 'EOF' > 2-print.py
#!/usr/bin/python3
print("Programming is like building a multilingual puzzle")
EOF

# 4. Create Task 3
cat << 'EOF' > 3-print_number.py
#!/usr/bin/python3
number = 98
print(f"{number} Battery street")
EOF

# 5. Create Task 4
cat << 'EOF' > 4-print_float.py
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
EOF

# 6. Create Task 5
cat << 'EOF' > 5-print_string.py
#!/usr/bin/python3
str = "Holberton School"
print(str * 3)
print(str[:9])
EOF

# 7. Create Task 6
cat << 'EOF' > 6-concat.py
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 = "Welcome to " + str1 + " " + str2 + "!"
print(str1)
EOF

# 8. Create Task 7
cat << 'EOF' > 7-edges.py
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
EOF

# 9. Create Task 8
cat << 'EOF' > 8-concat_edges.py
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
str = str[39:67] + str[106:112] + str[:6]
print(str)
EOF

# 10. Create Task 9
cat << 'EOF' > 9-easter_egg.py
#!/usr/bin/python3
import this
EOF

# Make all files executable
chmod +x 0-run 1-run_inline 2-print.py 3-print_number.py 4-print_float.py 5-print_string.py 6-concat.py 7-edges.py 8-concat_edges.py 9-easter_egg.py

echo "✅ All files created and permissions granted successfully!"

# Git Workflow Automation
echo "Pushing changes to GitHub..."
git add 0-run 1-run_inline 2-print.py 3-print_number.py 4-print_float.py 5-print_string.py 6-concat.py 7-edges.py 8-concat_edges.py 9-easter_egg.py
git commit -m "Complete Python Hello World tasks 0 through 9"
git push

echo "🚀 Everything is up to date on GitHub!"
