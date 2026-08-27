import json, os

# Read yesterday's page to extract the script framework
with open("每日缠论_20260826.html", "r", encoding="utf-8") as f:
    yday = f.read()

# Extract the CSS and script framework
css_start = yday.index("<style>")
css_end = yday.index("</style>") + 7
css = yday[css_start:css_end]

# Extract the JS pipeline (functions)
script_start = yday.index('const API=')
script_end = yday.index('async function load()')
pipeline = yday[script_start:script_end]

print("CSS extracted:", len(css), "chars")
print("Pipeline extracted:", len(pipeline), "chars")
print("OK")
