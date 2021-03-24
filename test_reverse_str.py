def reverse(str):
    reversed = ''
    for i in range(len(str) -1, -1, -1):
        reversed += str[i];
    return reversed;

def test_reverse_true():
    greeting = 'Hello';
    reverse_greeting = reverse(greeting);
    assert reverse_greeting == 'olleH';
