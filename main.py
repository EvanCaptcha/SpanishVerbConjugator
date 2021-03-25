import requests, json

def getConjugatedSection(v, t, pn):
    tn = {
        "1": "presentIndicative",
        "2": "preteritIndicative",
        "3": "imperfectIndicative",
        "4": "conditionalIndicative",
        "5": "futureIndicative",
        "6": "presentSubjunctive",
        "7": "imperfectSubjunctive",
        "8": "imperfectSubjunctive2",
        "9": "futureSubjunctive",
        "10": "imperative",
        "11": "negativeImperative",
        "12": "presentContinuous",
        "13": "preteritContinuous",
        "14": "imperfectContinuous",
        "15": "conditionalContinuous",
        "16": "futureContinuous",
        "17": "presentPerfect",
        "18": "preteritPerfect",
        "19": "pastPerfect",
        "20": "conditionalPerfect",
        "21": "futurePerfect",
        "22": "presentPerfectSubjunctive",
        "23": "pastPerfectSubjunctive",
        "24": "futurePerfectSubjunctive"

    }
    p = {
        "1": "yo",
        "2": "tú",
        "3": "él\u002Fella\u002FUd.",
        "4": "nosotros",
        "5": "ellos\u002Fellas\u002FUds."
    }
    tense = tn[t]
    pronoun = p[pn]

    jsonOg = requests.get(f"https://www.spanishdict.com/conjugate/{v}").text.split("window.SD_COMPONENT_DATA = ")[1].split(";")[0]
    j = json.loads(jsonOg)
    for w in j['verb']['paradigms'][tense]:
        if w['pronoun'] == pronoun:
            return w['word']


def getMultipleAns(list, t, pn):
    arr = list.split("\n")
    for a in arr:
        print(getConjugatedSection(a, str(t), str(pn)))
if __name__ == '__main__':
    tenses = '''1: presentIndicative
2: preteritIndicative
3: imperfectIndicative
4: conditionalIndicative
5: futureIndicative
6: presentSubjunctive
7: imperfectSubjunctive
8: imperfectSubjunctive2
9: futureSubjunctive
10: imperative
11: negativeImperative
12: presentContinuous
13: preteritContinuous
14: imperfectContinuous
15: conditionalContinuous
16: futureContinuous
17: presentPerfect
18: preteritPerfect
19: pastPerfect
20: conditionalPerfect
21: futurePerfect
22: presentPerfectSubjunctive
23: pastPerfectSubjunctive
24: futurePerfectSubjunctive'''
    print(tenses)
    t = input("What tense would you like to conjugate into?\n")
    pronouns = r'''1. yo
2. tú
3. él
4. nosotros
5. ellos
    '''
    print(pronouns)
    pn = input("Which pronoun?\n")
    list = '''Llegar
Tener
Ir
Servir
Creer
Almorzar
Venir
Dar
Pedir
Oír
Saber
Volver
Ser'''
    getMultipleAns(list, t, pn)
