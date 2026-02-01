import win32com.client as win

speaker = win.Dispatch("sapi.spvoice")

name_list = ['luffy', 'zoro', 'robin']

for name in name_list:
    print("shout out boss " + name)
    speaker.speak(f"shout out to {name}")

print("shout out to everyone")

try:
    a = int(input('enter a number: '))
    print(a)
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print("number is inside else")
finally:
    print("finally")
