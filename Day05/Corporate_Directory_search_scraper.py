import re

directory = "Contact HR at 123-456-7890 or the helpdesk at (987) 654-3210. Direct line is 5558881234."

def scrape_directory_phones(directory_text):

    pattern =re.compile(r"("r"(\d{3})-(\d{3})-(\d{4})" # AAA-PPP-LLLL 
                        r"|"r"(\d3) (\d{3})-(\d{4})" # (AAA) PPP-LLLL
                        r"|"r"(\d{3})(\d{3})(\d{4})" # AAAPPPLLLLr
                        ")")

    records = []

    for match in pattern.finditer(directory_text):
        groups = match.groups()

        # Pick the groups that actually matched
        area_code = groups[0] or groups[3] or groups[6]
        prefix = groups[1] or groups[4] or groups[7]
        line_number = groups[2] or groups[5] or groups[8]

        records.append({
            "area_code": area_code,
            "prefix": prefix,
            "line_number": line_number,
            "formatted": f"({area_code}) {prefix}-{line_number}"
        })

    return records

print((scrape_directory_phones(directory)))
