import re


def check_login(password):
    password_checker = re.compile(r'^([a-z])(?=.*[\d].*)(?=.*[a-z].*)(?=.*[\-].*)(?=.*[\.].*)[0-9a-z.\-]{,20}([\w])$')
    return password_checker.match(password)


if __name__ == '__main__':
    print(bool(check_login('Addfs.-dfgd43q22aalalalllalal')))
    print(bool(check_login('a4545.-aa%')))
    print(bool(check_login('aAddfs.-dfgd43qqa')))
    print(bool(check_login('aaddfs.-dfgd43qqa')))


