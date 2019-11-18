#!/usr/bin/env python3

"""String Flips.

Create a function that takes a string as the first argument,
and a (string) specification as a second argument. If the 
specification is "word", return a string with each word
reversed while maintaining their original order. If the
specification is "sentence", reverse the order of the words
in the string, while keeping the words intact.

Source:
https://edabit.com/challenge/JsLu5qWsJtuJuBZT4
"""


def flip(txt: str, spec: str) -> str:
    """Flip the string, based on the word or sentence."""
    if spec.lower() == 'word':
        return " ".join(["".join(reversed(word)) for word in txt.split(' ')])
    if spec.lower() == 'sentence':
        return " ".join(txt.split(' ')[::-1])
    raise ValueError(
        f"The spec value '{spec}' is invalid. The spec argument needs to be 'word' or 'sentence'.")


def main():
    """Run sample flip functions. Do not import."""
    txt1 = "There's never enough time to do all the nothing you want"
    txt2 = "I have all these great genes but they're recessive"
    txt3 = "I like maxims that don't encourage behavior modification"

    assert flip('Hello', 'word') == 'olleH'
    assert flip('Hello', 'sentence'), 'Hello'
    assert flip(
        txt1, 'word') == "s'erehT reven hguone emit ot od lla eht gnihton uoy tnaw"
    assert flip(
        txt1, 'sentence') == "want you nothing the all do to time enough never There's"
    assert flip(
        txt2, 'word') == "I evah lla eseht taerg seneg tub er'yeht evissecer"
    assert flip(
        txt2, 'sentence') == "recessive they're but genes great these all have I"
    assert flip(
        txt3, 'word') == "I ekil smixam taht t'nod egaruocne roivaheb noitacifidom"
    assert flip(
        txt3, 'sentence') == "modification behavior encourage don't that maxims like I"
    print('Passed.')


if __name__ == "__main__":
    main()
