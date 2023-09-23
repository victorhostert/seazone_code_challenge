# SEAZONE CODE CHALLENGE

### Desenvolvido por Victor William Hostert

---
## 🧪 Tecnologias utilizadas neste projeto

Este projeto foi desenvolvido utilizando:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [SQLite3](https://www.sqlite.org/index.html)


## 🚀 Como executar

O primeiro passo é ter o Git instalado no seu PC. Se você ainda não baixou, pode fazê-lo [com este link](https://git-scm.com/downloads). Para verificar se você tem git, use o seguinte comando:

```bash
$ git --version # Se você tiver git, o número da versão deverá aparecer no seu console
```

Clone o projeto utilizando a url HTTPS, em uma pasta de sua preferência, clicando em "clone" na página do repositório, selecionando a opção HTTPS e utilizando o seguinte comando:

```bash
$ git clone <URL HTTPS>
```

Alternativamente, você pode baixar o repositório em .zip

Em sua máquina local, certifique-se de ter [PIP](https://pip.pypa.io/en/stable/installation/) funcionando e instale as bibliotecas especificadas no arquivo ```requirements.txt```, usando o seguinte comando:

```bash
$ pip install -r requirements.txt
```

Agora, para acessar o projeto, basta digitar os seguintes comandos em seu console:

```bash
$ python manage.py migrate
$ python manage.py runserver
```

Como se trata apenas de uma API, você encontrará os endpoints disponíveis [nesta url](http://localhost:8000/api/v1/)

Os endpoints disponíveis são:

```bash
{
    "anuncio": "http://localhost:8000/api/v1/anuncio/",
    "imovel": "http://localhost:8000/api/v1/imovel/",
    "reserva": "http://localhost:8000/api/v1/reserva/",
}
```

Caso queira rodar os testes, o comando é:

```bash
$ python manage.py test
```