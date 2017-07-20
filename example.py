import uinames


if __name__ == "__main__":
    person = uinames.generate_random_identity()
    print "========== A Single Person =========="
    print "{} {} from {}".format(person.name, person.surname, person.region)

    people = uinames.generate_random_identities(4, "male", "canada", ext=True)
    print "========== Multiple People =========="
    for p in people.data:
        print "{} {} {} from {}, age {}".format(p.title, p.name, p.surname,
                                                p.region, p.age)
