import requests


def main():

    # Lista de perguntas com um prompt para validação da mensagem. Como é uma campo aberto, o usuário pode digitar
    # qualquer coisa e não estar condizente com a pergunta. Pra tentar minimizar possíveis erros, estamos usando a
    # própria API do claude pra validar o retorno do usuário.
    # Foi usada uma temperature mediana para casos de erro de digitação e falta de acentos
    # E o modelo usado foi o haiku que é o com resposta mais rápida
    questions = {
        "1️⃣  Qual é o seu animal favorito?": ClaudeRequestValidation(
            model="claude-3-5-haiku-latest",
            temperature=0.5,
            content="Eu quero que você aja como um analista de testes, sendo técnico e sucinto. Eu vou prover a "
                    "resposta de um usuário e quero você valide se a resposta é válida para a pergunta. O tipo de "
                    "validação que quero que faça é sobre o contexto verificando se o animal favotito informado pelo "
                    "usuário é realmente um animal. Validação de maiusculas e minusculas não devem ser levadas em "
                    "consideração. Seu papel é retornar a palavra 'true' se a resposta do usuário for válida. Ou "
                    "retornar a palavra 'false', se a resposta do usuário for inválida. Em caso de dúvida, "
                    "retornar 'false'. Seja rigoroso para retornar apenas essas duas palavras sem nenhum texto "
                    "adicional.",
            max_tokens=8
        ),
        "2️⃣  Qual é o continente, país ou cidade dos sonhos para visitar?": ClaudeRequestValidation(
            model="claude-3-5-haiku-latest",
            temperature=0.5,
            content="Eu quero que você aja como um analista de testes, sendo técnico e sucinto. Eu vou prover a "
                    "resposta de um usuário e quero você valide se a resposta é válida para a pergunta. O tipo de "
                    "validação que quero que faça é sobre o contexto verificando se o lugar informado pelo usuário é "
                    "realmente um continente, país ou cidade. Validação de maiusculas e minusculas não devem ser "
                    "levadas em consideração. Seu papel é retornar a palavra 'true' se a resposta do usuário for "
                    "válida. Ou retornar a palavra 'false', se a resposta do usuário for inválida. Em caso de dúvida, "
                    "retornar 'false'. Seja rigoroso para retornar apenas essas duas palavras sem nenhum texto "
                    "adicional.",
            max_tokens=8
        ),
        "3️⃣  Qual é a sua comida favorita?": ClaudeRequestValidation(
            model="claude-3-5-haiku-latest",
            temperature=0.5,
            content="Eu quero que você aja como um analista de testes, sendo técnico e sucinto. Eu vou prover a "
                    "resposta de um usuário e quero você valide se a resposta é válida para a pergunta. O tipo de "
                    "validação que quero que faça é sobre o contexto verificando se a comida informada pelo usuário é "
                    "realmente uma comida. Validação de maiusculas e minusculas não devem ser levadas em "
                    "consideração. Seu papel é retornar a palavra 'true' se a resposta do usuário for válida. Ou "
                    "retornar a palavra 'false', se a resposta do usuário for inválida. Em caso de dúvida, "
                    "retornar 'false'. Seja rigoroso para retornar apenas essas duas palavras sem nenhum texto "
                    "adicional.",
            max_tokens=8
        ),
        "4️⃣  Qual é a sua cor favorita?": ClaudeRequestValidation(
            model="claude-3-5-haiku-latest",
            temperature=0.5,
            content="Eu quero que você aja como um analista de testes, sendo técnico e sucinto. Eu vou prover a "
                    "resposta de um usuário e quero você valide se a resposta é válida para a pergunta. O tipo de "
                    "validação que quero que faça é sobre o contexto verificando se a cor informada pelo usuário é "
                    "realmente uma cor. Validação de maiusculas e minusculas não devem ser levadas em consideração. "
                    "Seu papel é retornar a palavra 'true' se a resposta do usuário for válida. Ou retornar a palavra "
                    "'false', se a resposta do usuário for inválida. Em caso de dúvida, retornar 'false'. Seja "
                    "rigoroso para retornar apenas essas duas palavras sem nenhum texto adicional.",
            max_tokens=8
        ),
        "5️⃣  Qual é o seu superpoder imaginário favorito?": ClaudeRequestValidation(
            model="claude-3-5-haiku-latest",
            temperature=0.5,
            content="Eu quero que você aja como um analista de testes, sendo técnico e sucinto. Eu vou prover a "
                    "resposta de um usuário e quero você valide se a resposta é válida para a pergunta. O tipo de "
                    "validação que quero que faça é sobre o contexto verificando se o superpoder informado pelo "
                    "usuário é realmente um superpoder. Validação de maiusculas e minusculas não devem ser levadas em "
                    "consideração. Seu papel é retornar a palavra 'true' se a resposta do usuário for válida. Ou "
                    "retornar a palavra 'false', se a resposta do usuário for inválida. Em caso de dúvida, "
                    "retornar 'false'. Seja rigoroso para retornar apenas essas duas palavras sem nenhum texto "
                    "adicional.",
            max_tokens=8
        ),
    }

    responses = {}
    print("\n✨✨✨ Prepare-se para uma experiência única! ✨✨✨\n")
    print("Sou um contador de histórias extremamente criativo 📖✨")
    print("Com apenas 5 perguntas, vou transformar suas respostas em uma história incrível e personalizada 🎭📚")
    print("Mal posso esperar para ver onde sua imaginação vai nos levar! 🚀🌟")

    # Aqui, fiz um retry para casos em que o usuário informasse algo "inválido". Pra não ficar em um loop,
    # só estou fazendo o prompt uma fez para o usuário em casos de resposta incompatível com a pergunta
    for question, validation in questions.items():
        retries = 1
        while retries >= 0:
            retries -= 1
            user_input = input(f"\n{question} ").strip()
            question_sanitized = question.split("️⃣")[1].strip() if "️⃣" in question else question

            if is_valid(question, user_input, validation):
                responses[question_sanitized] = user_input
                retries = -1
            elif retries < 0:
                responses[question_sanitized] = user_input
            else:
                print("Ops! Parece que a resposta não está no formato que eu esperava. 🤔")
                print(
                    "Você pode tentar novamente? Vou precisar de uma resposta mais clara para criar a história "
                    "perfeita para você. 😊")

    print("\n\nÓtimo! 🎉")
    print("Com suas respostas em mãos, estou criando uma história incrível, feita sob medida para você! 🖋️✨")
    print("Prepare-se para embarcar em uma aventura única que vai surpreender e encantar. 🚀🌟\n")
    print("Só mais um momento… a mágica está acontecendo! 💎📖\n")

    generate_story(responses)


def is_valid(question, user_response, request_validation):
    if not user_response:
        return False
    content = f"{request_validation.content}. Pergunta feita: '{question}'. Resposta do usuário: '{user_response}'"
    claude_response = call_claude_api(request_validation.model, request_validation.temperature, content,
                                      request_validation.max_tokens)
    return claude_response and claude_response.content[0]['text'].lower() == "true"


def generate_story(responses):
    model = "claude-3-5-sonnet-latest"
    max_tokens = 2048
    temperature = 1.0
    content = ("Você é um contador de histórias extremamente criativo. "
               "Com apenas 5 perguntas, você deve transformar as respostas em uma história incrível e personalizada. "
               "Adicione emojis para tornar a história ainda mais envolvente. "
               "Baseando-se nas seguintes respostas, crie uma história única e interessante: " +
               " ".join([f"{key} {value}." for key, value in responses.items()]))

    claude_response = call_claude_api(model, temperature, content, max_tokens)
    story = " ".join(message['text'] for message in claude_response.content) if claude_response else \
        ("Ops! Parece que algo deu errado enquanto eu criava sua história. 😔 Mas não se preocupe, vamos tentar "
         "novamente! 🚀✨")
    print(story)


def call_claude_api(model, temperature, content, max_tokens):
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": "YOUR_API_KEY",
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    payload = {
        "model": model,
        "temperature": temperature,
        "messages": [{"role": "user", "content": content}],
        "max_tokens": max_tokens
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        return ClaudeMessagesResponse.from_response(response.json())
    except Exception as e:
        print(f"Error calling the API: {e}")
        return None


class ClaudeMessagesResponse:
    def __init__(self, id, type, role, model, content, usage):
        self.id = id
        self.type = type
        self.role = role
        self.model = model
        self.content = content
        self.usage = usage

    @staticmethod
    def from_response(json_response):
        return ClaudeMessagesResponse(
            id=json_response["id"],
            type=json_response["type"],
            role=json_response["role"],
            model=json_response["model"],
            content=json_response["content"],
            usage=json_response["usage"]
        )


class ClaudeRequestValidation:
    def __init__(self, model, temperature, content, max_tokens):
        self.model = model
        self.temperature = temperature
        self.content = content
        self.max_tokens = max_tokens


if __name__ == "__main__":
    main()
