from dictionaryGen import getFlagDictionary
from reasoner import scasp_query

text1 = """I forgot to cook you dinner, not sorry. You're fucking shit. 
            We're going to the party without you. I am going to attack you.
            You never listen you never listen you never listen. 
            You live on circleBlue street, george."""

text2 = """Not sure why you posted that picture, it’s not your best. You should probably think about sticking to what you’re good at instead of trying too hard.
 Just some advice, take it or leave it.""Not sure why you posted that picture, it’s not your best.You should probably think about sticking to what you’re good 
 at instead of trying too hard. Just some advice, take it or leave it."""

text3 = """Honestly, you’re just embarrassing yourself with this stuff. It’s like you don’t even know how bad you look right now. 
Maybe you should stop pretending and stick to something you can actually do well."""

text4 = """Wow, you are honestly the worst. Everything about you is so fake—your posts, your personality, everything.
 I can’t believe anyone even talks to you. Do everyone a favor and just disappear already."""

text5 = """You’re a complete waste of space. Nobody likes you, and they’re all just pretending. You should just give up on everything because 
you’re never going to amount to anything. The world would be better off without you."""


text6 = """Hey there! Just wanted to say I really admire your work—it’s always so creative and inspiring.
 Hope you’re having an amazing day! Let me know if there’s anything I can do to support you, I’m always cheering for you!"""

text7 = """Hey there! Just wanted to say that you’re absolutely amazing. You bring so much positivity
 and joy to everyone around you. Keep being the wonderful person you are!"""

text8 = """I really appreciate you! Your creativity and energy are so inspiring, and you always
 know how to make people smile. Thank you for being such a great friend."""

text9 = """Hope you’re having a fantastic day! Just wanted to remind you that you’re doing such 
a great job, and I’m so proud of everything you’re accomplishing."""

text10 = """You’ve been on my mind lately—I just wanted to say how much I admire your dedication.
 You’re capable of achieving anything you set your mind to, and I’m here cheering you on every step of the way!"""

text11 = """Hi! I wanted to check in and let you know that you’re appreciated more than you realize.
 Keep shining and doing your best, because you’re making a difference in ways you may not even see."""

meanList = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11]
for text in meanList:
    predicate = getFlagDictionary(text)
    # print(predicate)
    scasp_query(predicate)
print("Done")

