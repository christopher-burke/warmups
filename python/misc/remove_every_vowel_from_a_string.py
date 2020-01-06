#!/usr/bin/env python3

"""Remove Every Vowel from a String.

Create a function that takes a string and returns a new string with all vowels removed.

Source:
https://edabit.com/challenge/MvgCxPkSgtQ8hQjwx
"""

import re


def assert_equals(func_result, result):
    """Assert equal the func_result with the desired result."""
    assert func_result == result, f"'{func_result}' does not match '{result}'."


def remove_vowels(txt):
    """Remove every vowel from string txt."""
    return re.sub(r'[a|e|i|o|u|A|E|I|O|U]', '', txt)


def main():
    """Run sample remove_vowels functions. Do not import."""
    assert_equals(remove_vowels("If Obama resigns from office NOW, thereby doing a great service to the country - I will give him free lifetime golf at any one of my courses!"),
                  "f bm rsgns frm ffc NW, thrby dng  grt srvc t th cntry -  wll gv hm fr lftm glf t ny n f my crss!")
    assert_equals(remove_vowels("This election is a total sham and a travesty. We are not a democracy!"),
                  "Ths lctn s  ttl shm nd  trvsty. W r nt  dmcrcy!")
    assert_equals(remove_vowels(
        "I have never seen a thin person drinking Diet Coke."), " hv nvr sn  thn prsn drnkng Dt Ck.")
    assert_equals(remove_vowels("Everybody wants me to talk about Robert Pattinson and not Brian Williams - I guess people just don't care about Brian!"),
                  "vrybdy wnts m t tlk bt Rbrt Pttnsn nd nt Brn Wllms -  gss ppl jst dn't cr bt Brn!")
    assert_equals(remove_vowels("Katy, what the hell were you thinking when you married loser Russell Brand. There is a guy who has got nothing going, a waste!"),
                  "Kty, wht th hll wr y thnkng whn y mrrd lsr Rssll Brnd. Thr s  gy wh hs gt nthng gng,  wst!")
    assert_equals(remove_vowels("Windmills are the greatest threat in the US to both bald and golden eagles. Media claims fictional 'global warming' is worse."),
                  "Wndmlls r th grtst thrt n th S t bth bld nd gldn gls. Md clms fctnl 'glbl wrmng' s wrs.")
    assert_equals(remove_vowels("Sorry losers and haters, but my I.Q. is one of the highest - and you all know it! Please don't feel so stupid or insecure, it's not your fault"),
                  "Srry lsrs nd htrs, bt my .Q. s n f th hghst - nd y ll knw t! Pls dn't fl s stpd r nscr, t's nt yr flt")
    assert_equals(remove_vowels("Happy Thanksgiving to all -- even the haters and losers!"),
                  "Hppy Thnksgvng t ll -- vn th htrs nd lsrs!")
    assert_equals(remove_vowels("Watch Kasich squirm --- if he is not truthful in his negative ads I will sue him just for fun!"),
                  "Wtch Ksch sqrm --- f h s nt trthfl n hs ngtv ds  wll s hm jst fr fn!")
    assert_equals(remove_vowels("Obama is, without question, the WORST EVER president. I predict he will now do something really bad and totally stupid to show manhood!"),
                  "bm s, wtht qstn, th WRST VR prsdnt.  prdct h wll nw d smthng rlly bd nd ttlly stpd t shw mnhd!")
    print('Passed.')


if __name__ == "__main__":
    main()
