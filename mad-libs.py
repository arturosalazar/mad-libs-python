# A Mad Libs Game where the computer prompts the user for words
# Those words are inserted into blanks to make a fun story

adj1 = input("Adjective: ").lower()
adj2 = input("Adjective: ").lower()
type_of_bird = input("Type of Bird: ").lower()
room_in_house = input("Room in a house: ").lower()
verb_past_tense1 = input("Verb(past tense): ").lower()
verb1 = input("Verb: ").lower()
relative_name = input("Relative's Name: ").title()
noun1 = input("Noun: ").lower()
liquid = input("Liquid: ").lower()
verb_end_w_ing1 = input("Verb ending with -ing: ").lower()
body_part = input("Part of body (pluarl): ").lower()
plural_noun = input("Plural noun: ").lower()
verb_end_w_ing2 = input("Verb ending with -ing: ").lower()
noun2 = input("Noun: ").lower()

madlib = f"It was a {adj1}, cold November day. I woke \
up to the {adj2} smell of {type_of_bird} roasting in \
the {room_in_house} downstairs. I {verb_past_tense1} down \
the stairs to see if I could help {verb1} the dinner. \
My mom said. 'See if {relative_name} needs a fresh {noun1}' \
So I carried a tray of glasses full of {liquid} into the \
{verb_end_w_ing1} room. When I got there, I couldn't \
believe my {body_part}! There were {plural_noun} {verb_end_w_ing2} \
on the {noun2}!"

print(madlib)