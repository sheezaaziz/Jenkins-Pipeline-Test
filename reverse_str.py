def reverse(str):
    reversed = ''
    for i in range(len(str) -1, -1, -1):
        reversed += str[i];
    return reversed;

print(reverse('Greetings!'));
