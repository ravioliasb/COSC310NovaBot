import wolframalpha
client = wolframalpha.Client('9XGQT8-VJL3XVV877')

def wolframSearch(input):
    input_lower = input.lower()
    input_split = input_lower.split()
    ask_wolfram = ""
    ask = range(1,len(input_split))
    for i in ask:
        ask_wolfram = ask_wolfram + input_split[i] + ""
    try:
        ask_wolfram = client.query(ask_wolfram)
        answer = next(ask_wolfram.results).text
    except:
        answer = "Wolfram could not answer the query"

    return answer
