import re

datetime_regex = re.compile(r'(\d{4})[-\/](\d{2})[\/-](\d{2})(T(\d{2}):(\d{2}):(\d{2})Z)?')

def extract_date(date_string):
    match = re.search(datetime_regex, date_string)
    if match:
        return f"Year: {match.group(1)}, Month: {match.group(2)}, Date: {match.group(3)}, Hour {match.group(5)}, Minute: {match.group(6)} Second: {match.group(7)}"
    else:
        return "Not a match"


def main():
    dates = ["⦁	2014-08-18T13:03:25Z", "⦁	2014/08/18T13:03:25Z", "⦁	2014-08-18", "⦁	2014/08/18"]
    for date in dates:
        print(extract_date(date))

if __name__ == "__main__":
  main()
