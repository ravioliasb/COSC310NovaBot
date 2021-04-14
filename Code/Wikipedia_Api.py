import wikipedia
import warnings

warnings.catch_warnings()
warnings.simplefilter("ignore")


def wikiSearch(input_):  # Takes user input and tries to find it on Wikipedia
    input_lower = input_.lower()
    input_split = input_lower.split()
    ask_wiki = ""
    ask = range(1, len(input_split))
    for i in ask:
        ask_wiki = ask_wiki + input_split[i] + ""
    try:
        ask_wiki = wikipedia.summary(ask_wiki)
    except:
        ask_wiki = "Wikipedia could not provide a summary"

    return ask_wiki
