from parse_module import *
import hashlib
import links

if (__name__ == "__main__"):
    import test_parse
    test_parse.TestParse()

    voyager_page = get_page(links.VOYAGER)
    rfc_page = get_page(links.RFC_1149)
    unicode_page = get_page(links.UNICODE)
    bitcoin_page = get_page(links.BITCOIN)
    icbn_page = get_page(links.ICBN)

    voyager_flag = parse_voyager_page(voyager_page)
    rfc_flag = parse_rfc_page(rfc_page)
    brain_emoji_flag = parse_unicode_page(unicode_page)
    bitcoin_flag = parse_bitcoin_page(bitcoin_page)
    icbn_flag = parse_icbn_page(icbn_page)

    flag = "FLAG{" + voyager_flag + "-" + rfc_flag + "-" + brain_emoji_flag + "-" + bitcoin_flag + "-" + icbn_flag + "}"

    hash_object = hashlib.sha256()
    hash_object.update(flag.encode("utf-8"))
    print(hash_object.hexdigest())

