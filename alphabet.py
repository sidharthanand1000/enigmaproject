class Alphabet:

    # Represents the String chars in alphabet.
    _chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # A new alphabet containing CHARS.
    def __init__(self, chars):
        self._char = char

    # Returns the size of the alphabet.
    def size(self):
        return 26

    # Returns true if CH is in this alphabet.
    def contains(self, ch):
        i = 0
        while i <= Alphabet.size() - i:
            if self._chars[i] == ch:
                return true


    # Returns character number INDEX in the alphabet. where 0 <= INDEX < size().
    def toChar(self, index):
        if index < len(_chars) and index >= 0:
            return _chars[index]

    # Returns the index of character CH which must be in the alphabet. This is the inverse of toChar().
    def toInt(self, ch):
        i = 0
        while len(self._chars):
            if self._chars[i] != ch:
                return self._chars.index(i)
            i += 1
        raise Exception("This character isn't in the alphabet")