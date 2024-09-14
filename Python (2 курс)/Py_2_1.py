def f1(digit):
    # your code here #1 max digit
    digit = str(digit)
    return max(digit)

if __name__ == "__main__":
    assert f1(1) == 1
    assert f1(51) == 5
    assert f1(632) == 6
    assert f1(11) == 1
    assert f1(10000) == 1
    print("1) Done!")


def f2(text):
    # your code here #2 first word
    return ""

if __name__ == "__main__":
    assert f2("Hello world") == "Hello"
    assert f2("a word") == "a"
    assert f2("online compiler and debugger") == "online"
    assert f2("Hi") == "Hi"
    print("2) Done!")


def f3(text, start, end):
    # your code here #3 between start and end
    return ""

if __name__ == "__main__":
    assert f3("What is >orange<", ">", "<") == "orange"
    assert f3("What is [orange]", "[", "]") == "orange"
    assert f3("What is ><", ">", "<") == ""
    assert f3("[an orange]", "[", "]") == "an orange"
    print("3) Done!")


def f4(word, first, second):
    # your code here #4 is after
    return False

if __name__ == "__main__":
    assert f4("world", "w", "o") == True
    assert f4("world", "w", "r") == False
    assert f4("world", "l", "o") == False
    assert f4("orange", "n", "g") == True
    assert f4("", "n", "g") == False
    assert f4("list", "l", "l") == False
    assert f4("world", "d", "w") == False
    print("4) Done!")


def f5(n):
    # your code here #5 end zeros
    return 0

if __name__ == "__main__":
    assert f5(0) == 1
    assert f5(1) == 0
    assert f5(10) == 1
    assert f5(101) == 0
    assert f5(245) == 0
    assert f5(100100) == 2
    print("5) Done!")
