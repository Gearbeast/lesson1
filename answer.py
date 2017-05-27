
def get_answer(question):
    answer = {
        "привет": "И тебе привет!",
        "как дела": "Лучше всех",
        "пока": "Увидимся",
        'hello': 'hi'
    }
    print(answer.get(question.lower()))


get_answer(input('Говори: '))