from desktop_cat import Cat
from desktop_cat.window import Window, run


cat = Cat("Whiskers")
window = Window(cat)
print(cat.render())

cat.mood = "angry"
print(cat.render())

cat.feed("fish")
print(cat.render())
cat.last_action = "idle"
print(cat.render())

cat.mood = "happy"
print(cat.render())

cat.say("Meow!")
window.say("Meow!")
run()
