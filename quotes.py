import random

common_emotions = ["fear", "scared", "scary", "anger", "angry", "sadness", "sad", "trust", "mistrust", "courage",
                   "confidence", "kindness", "kind", "envy", "love", "happiness", "happy", "joy", "joyful"]

fear = ["A negative mind will never give you a positive life.",
        "What you are afraid to do is a clear indication of what you need to do.",
        "Never let your fear decide your future.", "There is no illusion greater than fear",
        "Fear is the brain's way of saying there is something important for you to overcome.",
        "Fear is temporary. Regret lasts forever."]
scared = ["A negative mind will never give you a positive life.",
          "What you are afraid to do is a clear indication of what you need to do.",
          "Never let your fear decide your future.", "There is no illusion greater than fear.",
          "Fear is the brain's way of saying there is something important for you to overcome.",
          "Fear is temporary. Regret lasts forever."]
scary = ["A negative mind will never give you a positive life.",
         "What you are afraid to do is a clear indication of what you need to do.",
         "Never let your fear decide your future.", "There is no illusion greater than fear.",
         "Fear is the brain's way of saying there is something important for you to overcome.",
         "Fear is temporary. Regret lasts forever."]
anger = ["Anger is one letter short of 'danger'.", "A quick temper will make a fool of you soon enough.",
         "He who angers you, conquers you.", "When anger rises, think of the consequences.",
         "Don't be angry with people who don't have the capacity to change."]
angry = ["Anger is one letter short of 'danger'.", "A quick temper will make a fool of you soon enough.",
         "He who angers you, conquers you.", "When anger rises, think of the consequences.",
         "Don't be angry with people who don't have the capacity to change."]
sadness = ["A negative mind will never give you a positive life.",
           "Don't focus on the things that steal your joy; count the many things that make you happy.",
           "First, accept sadness. Realize that without losing, winning isn't so great.",
           "Let smiles overshine sadness.", "Smiling has always been easier than explaining why you're sad."]
sad = ["A negative mind will never give you a positive life.",
       "Don't focus on the things that steal your joy; count the many things that make you happy.",
       "First, accept sadness. Realize that without losing, winning isn't so great.", "Let smiles overshine sadness.",
       "Smiling has always been easier than explaining why you're sad."]
trust = ["To be trusted is more of a compliment than being loved.", "Actions speak louder than words.",
         "Loyalty is one of the most important things in the world.", "Trust is earned when actions meet words."]
mistrust = ["To be trusted is more of a compliment than being loved.", "Actions speak louder than words.",
            "Loyalty is one of the most important things in the world.", "Trust is earned when actions meet words."]
courage = [
    "Courage is not the absence of fear, but rather the judgement that something else is more important than fear.",
    "Courage is like a muscle; it is strengthened through use.",
    "Courage doesn't mean you don't get afraid, courage means you don't let fear stop you."]
confidence = [
    "Courage is not the absence of fear, but rather the judgement that something else is more important than fear.",
    "Courage is like a muscle; it is strengthened through use.",
    "Courage doesn't mean you don't get afraid, courage means you don't let fear stop you.",
    "The more you love your decisions, the less you need others to love them."]
kindness = ["Love is wanting more for someone than they want for themselves.", "Tears are words the heart can't say.",
            "One kind word can change someone's entire day.", "We rise by lifting others.",
            "Don't wait for someone to be friendly, show them how."]
kind = ["Love is wanting more for someone than they want for themselves.", "Tears are words the heart can't say.",
        "One kind word can change someone's entire day.", "We rise by lifting others.",
        "Don't wait for someone to be friendly, show them how."]
envy = ["Only a few can support your success without envy.",
        "The more you love your decisions, the less you need others to love them.",
        "Envy is the most stupid of vices, for there is no single advantage to be gained from it.",
        "Happiness is found when you stop comparing yourself to others."]
love = ["Love is wanting more for someone than they want for themselves.", "Tears are words the heart can't say.",
        "Loyalty is one of the most important things in the world.", "Love never fails.",
        "Love liberates, it doesn't bind."]
happiness = ["Let smiles overshine sadness.",
             "When you're happy you enjoy the music, but when you're sad you understand the lyrics.",
             "Sometimes happiness is a feeling; sometimes it's a decision.",
             "The happier you are, the more beautiful you become.",
             "Don't focus on the things that steal your joy; count the many things that make you happy.",
             "Joy is the kind of happiness that doesn't depend on what happens."]
happy = ["Let smiles overshine sadness.",
         "When you're happy you enjoy the music, but when you're sad you understand the lyrics.",
         "Sometimes happiness is a feeling; sometimes it's a decision.",
         "The happier you are, the more beautiful you become.",
         "Don't focus on the things that steal your joy; count the many things that make you happy.",
         "Joy is the kind of happiness that doesn't depend on what happens."]
joy = ["When you're happy you enjoy the music, but when you're sad you understand the lyrics.",
       "Sometimes happiness is a feeling; sometimes it's a decision.",
       "The happier you are, the more beautiful you become.",
       "Don't focus on the things that steal your joy; count the many things that make you happy.",
       "Joy is the kind of happiness that doesn't depend on what happens."]
joyful = ["When you're happy you enjoy the music, but when you're sad you understand the lyrics.",
          "Sometimes happiness is a feeling; sometimes it's a decision.",
          "The happier you are, the more beautiful you become.",
          "Don't focus on the things that steal your joy; count the many things that make you happy.",
          "Joy is the kind of happiness that doesn't depend on what happens."]

print "Hello!"
print "I am here solely for your moral support and guidance."
print "If you're ever feeling down, need inspiration, or just someone to talk to, you've come to the right place!"
print "Here are some common emotions that I can understand: "
print ", ".join(common_emotions) + "."
print "Try typing in whatever emotion you feel right now, for example,  " + str(
    common_emotions[random.randint(1, 9)]) + '.'
emotion = raw_input()
match = False
print "So you're feeling %s. " % emotion
if emotion in common_emotions:
    match = True
    while match is True:
        if emotion == "happiness":
            print str(happiness[random.randint(0, happiness.__len__() - 1)])
        elif emotion == "love":
            print str(love[random.randint(0, love.__len__() - 1)])
        elif emotion == "fear":
            print str(fear[random.randint(0, fear.__len__() - 1)])
        elif emotion == "scared":
            print str(scared[random.randint(0, scared.__len__() - 1)])
        elif emotion == "scary":
            print str(scary[random.randint(0, scary.__len__() - 1)])
        elif emotion == "anger":
            print str(anger[random.randint(0, anger.__len__() - 1)])
        elif emotion == "angry":
            print str(angry[random.randint(0, angry.__len__() - 1)])
        elif emotion == "sadness":
            print str(sadness[random.randint(0, sadness.__len__() - 1)])
        elif emotion == "sad":
            print str(sad[random.randint(0, sad.__len__() - 1)])
        elif emotion == "trust":
            print str(trust[random.randint(0, trust.__len__() - 1)])
        elif emotion == "mistrust":
            print str(mistrust[random.randint(0, mistrust.__len__() - 1)])
        elif emotion == "courage":
            print str(courage[random.randint(0, courage.__len__() - 1)])
        elif emotion == "confidence":
            print str(confidence[random.randint(0, confidence.__len__() - 1)])
        elif emotion == "kindness":
            print str(kindness[random.randint(0, kindness.__len__() - 1)])
        elif emotion == "kind":
            print str(kind[random.randint(0, kind.__len__() - 1)])
        elif emotion == "envy":
            print str(envy[random.randint(0, envy.__len__() - 1)])
        elif emotion == "happy":
            print str(happy[random.randint(0, happy.__len__() - 1)])
        elif emotion == "joy":
            print str(joy[random.randint(0, joy.__len__() - 1)])
        elif emotion == "joyful":
            print str(joyful[random.randint(0, joyful.__len__() - 1)])
        print "'EXIT' to exit. Otherwise, enter another emotion, for example, " + str(
    common_emotions[random.randint(1, 9)]) + '.'
        answer = raw_input()
        emotion = answer
        if answer == "EXIT":
            print "Goodbye! Thank You!"
            print "-Evan Kuykendall"
            break
        while answer not in common_emotions:
            print "Please enter a commonly used emotion, as shown above."
            match = False
            answer = raw_input()
            emotion = answer
        else:
            match = True
            print "So you're feeling %s. " % emotion
else:
    print "I can't understand your complex emotions! Please input something more comprehensible."
    emotion = raw_input()
