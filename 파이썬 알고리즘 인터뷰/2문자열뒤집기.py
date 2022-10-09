def reverseString(self, s: list[str]) -> None:
    s.reverse()
    s[:] = s[::-1]