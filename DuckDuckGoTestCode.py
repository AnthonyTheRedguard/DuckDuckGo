import requests

url_ddg = "https://api.duckduckgo.com"

resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
rsp_data = resp.json()
text = []

president_names = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Van Buren", "Harrison",
                   "Tyler",
                   "Polk", "Taylor",
                   "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield", "Arthur",
                   "Cleveland",
                   "Mckinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Truman",
                   "Eisenhower",
                   "Kennedy", "Nixon",
                   "Ford", "Carter", "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden"]

i = 0

while i < len(rsp_data["RelatedTopics"]):
    text.append(rsp_data["RelatedTopics"][i]["Text"])
    i += 1


def president_found(substring):
    for string in text:
        if substring in string:
            return True


def test_ddg0():
    assert president_found("Washington")
    assert president_found("Adams")
    assert president_found("Jefferson")
    assert president_found("Madison")
    assert president_found("Monroe")
    assert president_found("Jackson")
    assert president_found("Van Buren")
    assert president_found("Harrison")
    assert president_found("Tyler")
    assert president_found("Polk")
    assert president_found("Taylor")
    assert president_found("Fillmore")
    assert president_found("Pierce")
    assert president_found("Buchanan")
    assert president_found("Lincoln")
    assert president_found("Johnson")
    assert president_found("Grant")
    assert president_found("Hayes")
    assert president_found("Garfield")
    assert president_found("Arthur")
    assert president_found("Cleveland")
    assert president_found("Harrison")
    assert president_found("McKinley")
    assert president_found("Roosevelt")
    assert president_found("Taft")
    assert president_found("Wilson")
    assert president_found("Harding")
    assert president_found("Coolidge")
    assert president_found("Hoover")
    assert president_found("Truman")
    assert president_found("Eisenhower")
    assert president_found("Kennedy")
    assert president_found("Johnson")
    assert president_found("Nixon")
    assert president_found("Gerald Ford")
    assert president_found("Carter")
    assert president_found("Reagan")
    assert president_found("Bush")
    assert president_found("Clinton")
    assert president_found("Obama")
    assert president_found("Trump")
    assert president_found("Biden")
