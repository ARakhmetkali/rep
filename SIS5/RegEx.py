import re

# task 1
pattern1 = re.compile(r"ab*")
# task 2
pattern2 = re.compile(r"ab{2,3}")
# task 3
pattern3 = re.compile(r"[a-z]+\_")
# task 4
pattern4 = re.compile(r"[A-Z]{1}[a-z]+")
# task 5
pattern5 = re.compile(r"a.+b\Z")
# task 6
pattern6 = re.compile(r"[ ,.]")


# task 7
def snake_to_camel(text):
    camelcase = ""
    pattern = re.compile(r"[_]")
    words = pattern.split(text)
    for i, word in enumerate(words):
        if i != 0:
            camelcase += word.capitalize()
        else:
            camelcase += word
    return camelcase


# task 8
def modify(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:
            res += " " + word
        else:
            res += word
    return res


# task 9
def spaces(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:
            res += " " + word
        else:
            res += word
    return res


# task 10
def camel_to_snake(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i == 0:
            res += word.casefold()
        else:
            res += "_" + word.casefold()
    return res


# Conclusion
def main():
    print("Task 1")
    print(pattern1.search("fabsjdhasjkldk"))

    print("Task 2")
    print(pattern2.search("gjdasdlkajsabbb"))

    print("Task 3")
    print(pattern3.findall("fdskjdaskl_ fdsjkdjdsk_ lklklk_"))

    print("Task 4")
    print(pattern4.findall("First Gangster Immortus"))

    print("Task 5")
    print(pattern5.search("kingpin123"))
    print(pattern5.search("kslkdas"))
    print(pattern5.search("siumachineron7"))

    print("Task 6")
    text = "sandnas,askdklsada..fsdlskdlf finfgsdas,. asvb"
    print(pattern6.sub(":", text))

    print("Task 7")
    print(snake_to_camel("hello_world"))

    print("Task 8")
    print(modify("OneTwoYT"))

    print("Task 9")
    print(spaces("SpaceAndGalaxyIDK"))

    print("Task 10")
    print(camel_to_snake("CamelToSnake"))


if __name__ == "__main__":
    main()