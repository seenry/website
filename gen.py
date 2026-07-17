import re

def reg_id(tag):
    return rf'<{re.escape(tag)}>(.*?)</{re.escape(tag)}>'
    # return rf'!!{re.escape(tag)}\(((?:\\.|[^\\)])*)\)'

### Create Content String

lines = []
with open('./index.oe', 'r') as oe:
    for line in oe:
        if (line.strip()):
            lines.append(line[:-1])

html_string = ""

first_section = True
for line in lines:
    # handle section headers
    if (line[:2] == "# "):
        line = line[2:]
        if (not first_section):
            html_string = html_string + "</span>"
        else:
            first_section = False
        html_string = html_string + "<span class=\"block\"><h1>== " + line + " ==</h1>"

    # handle rest
    else:
        # handle email address
        line = re.split(r'(s.rhee@nyu.edu)', line)
        for i in range(len(line)):
            if (i%2 == 1):
                line[i] = "<em id=\"email-link\">" + "s.rhee@nyu.edu" + "</em>"
        line = "".join(line)

        # handle links
        line = re.split(reg_id("a"), line)
        for i in range(len(line)):
            if (i%2 == 1):
                line[i] = line[i].split(",")
                line[i] = "<a target=\"_blank\" href=\"" + line[i][1] + "\">" + line[i][0] + "</a>"
        line = "".join(line)

        html_string = html_string + "<p>" + line + "</p>"

html_string = html_string + "</span>"

### Insert Into Site Template

site_string = ""
with open("./idx.html", "r") as site:
    for line in site:
        site_string = site_string + line

site_string = re.split("!!!CONTENT_BLOCK!!!", site_string)
print(html_string.join(site_string))

