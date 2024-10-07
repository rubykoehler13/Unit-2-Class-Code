user_name = input("What is your name? ")
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
date = (f"The date is {month}/{day}/{year}")

noun_1 = input("Please give me a noun! ")
noun_2 = input("Can I have another noun please? ")
noun_3 = input("Another one! ")
noun_4 = input("And another one! ")
noun_5 = input("Finally, one more noun please! ")

verb_1 = input("Can you tell me a verb? (In present perfect ('ing' ending)) ")
verb_2 = input("Can you give me another verb? (In past tense please!) ")
verb_3 = input("How about another verb? (In infinitive please!) ")
verb_4 = input("Another one please! (In the infinitive) ")
verb_5 = input("Another one! (Also infinitive!) ")
verb_6 = input("And last verb!!! (Past tense please!) ")

adj_1 = input("I'd love it if you gave me an adjective! ")
adj_2 = input("Another one would be great too! ")
adj_3 = input("One more! ")

adv_1 = input("We're almost done, can I please have an adverb? ")
adv_2 = input("And last but not least, another adverb please! ")

print(user_name.title())
print(date)
print(f"Once upon a time, there was a man who loved to go on hikes.\n"
      f"He always started his hikes by {verb_1},\n"
      f"and he always takes a {noun_1} with him.\n"
      f"He sometimes likes to hike on a {noun_2}, but not very {adv_1}.\n"
      f"One day, he {verb_2} and almost died!\n"
      f"But at that moment, a woman appeared. She had a {noun_3} on her face,\n"
      f"and they couldn't stop {verb_3}! The man was very {adj_1} by this situation, \n"
      f"so he started to {verb_3} and {verb_4}.\n"
      f"The woman started to {verb_3} as well, but also {verb_5}.\n"
      f"They both stopped, and the man helped her take the {noun_3} off her face quite {adv_2}.\n"
      f"She was very grateful for his help, so she gave him a {noun_4} but it tasted so {adj_2}!!!!\n"
      f"The man was a little disappointed by this, but he realized that he actually liked her a lot...\n"
      f"So, he invited her on his hike with him, and they even found a {noun_5} at the end of it!\n"
      f"He had such a great time, and thought that the woman was just absolutely {adj_3},\n"
      f"so they decided to get married!\n"
      f"They both {verb_6} {adv_2} and everyone thought they were crazy, but they lived happily every after.")