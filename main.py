from tags import *



def main():
    tags = get_tag_template("template\\tags.json")['tags']
    vars = get_tag_template("template\\vars.json")['vars']

    asd = dict(name="@Benon", switch_to="")
    create_tag(tags, asd)
    print(create_tag(tags, asd))
    create_abbreviation_from_file(tags, vars)

    while True:
        continue




if __name__ == "__main__":
    main()