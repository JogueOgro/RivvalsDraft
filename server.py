from flask import Flask, render_template, request, redirect, url_for, flash
import shelve

app = Flask(__name__)
app.secret_key = 'rivvals'

jogadores = [
    {'nome': 'Maitê Polydoro', 'nick': 'Mayfolk', 'power': 3, 'tags': [], 'wins': []},
    {'nome': 'Henrique Miguel Gomes dos Anjos', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Marlon Gracietti de Amorim', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Andressa Bernardes Bock', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'André Roberto Milanez', 'nick': 'O CEO', 'power': 4, 'tags': [], 'wins': []},
    {'nome': 'Jemima Fonseca Luz', 'nick': '', 'power': 3.6, 'tags': [], 'wins': []},
    {'nome': 'Lucas Costa de Oliveira Alves', 'nick': 'Ai Chaves!', 'power': 4.8, 'tags': [], 'wins': []},
    {'nome': 'Felipe dos Santos Sena Pereira', 'nick': 'Seninha', 'power': 4.8, 'tags': [], 'wins': []},
    {'nome': 'Guilherme Fabrin Franco', 'nick': '', 'power': 2, 'tags': [], 'wins': []},
    {'nome': 'Bruno Raniery Freire Lima', 'nick': 'Raniery', 'power': 3.5, 'tags': [], 'wins': []},
    {'nome': 'Leonan Rodrigues Ferreira', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Caio Henrique dos Santos Caldas', 'nick': '', 'power': 3, 'tags': [], 'wins': []},
    {'nome': 'Leonardo Santos', 'nick': 'Leozzera', 'power': 3, 'tags': [], 'wins': ['mj']},
    {'nome': 'Nathan de Freitas Duarte', 'nick': '', 'power': 4.1, 'tags': [], 'wins': ['mj']},
    {'nome': 'Andre Augusto Costa Dionisio', 'nick': '', 'power': 4.3, 'tags': [], 'wins': []},
    {'nome': 'Giuliano de Carvalho Florestano', 'nick': '', 'power': 3, 'tags': [], 'wins': []},
    {'nome': 'Jessé Oliveira de Freitas', 'nick': 'O CTO', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Glauco Mordente', 'nick': '', 'power': 3, 'tags': [], 'wins': []},
    {'nome': 'Paula Elvira Picchi Mendes', 'nick': 'Paulinha', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Carlos Almeida', 'nick': '', 'power': 3.9, 'tags': [], 'wins': []},
    {'nome': 'Douglas Costa', 'nick': '', 'power': 2, 'tags': [], 'wins': []},
    {'nome': 'Glaicon da Silva Reis', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Carlos Eduardo Biaseto', 'nick': 'Cadu', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Rodrigo Urbano', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Fred Medeiros', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Patricia Goncalves Teixeira', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Leandro Cavalheri', 'nick': '', 'power': 4, 'tags': [], 'wins': []},
    {'nome': 'Caio Aparecido Rodrigues do Prado', 'nick': '', 'power': 2, 'tags': [], 'wins': []},
    {'nome': 'Nuno Francisco Nazaré Gonçalves Simão', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Pedro Henrique de Souza Alexandre', 'nick': '', 'power': 4.1, 'tags': [], 'wins': []},
    {'nome': 'Pamela Leite da Silva', 'nick': '', 'power': 3.5, 'tags': [], 'wins': []},
    {'nome': 'Rafael Marinho dos Santos', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Narcisio Zeferino Cardoso Junior', 'nick': '', 'power': 3, 'tags': [], 'wins': []},
    {'nome': 'Mariana Thomaz Rodrigues', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Beatriz Costa de Cerqueira', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Ana Paula de Campos Oliveira', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Marcelo Pinheiro', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Bruno Gonzalez Rodrigues', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Kelvy Correa Nascimento Chagas', 'nick': '', 'power': 3.5, 'tags': [], 'wins': []},
    {'nome': 'Cristian Silva Macedo', 'nick': '', 'power': 4, 'tags': [], 'wins': []},
    {'nome': 'Rafael dos Santos Cardoso', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Rafael Costa', 'nick': '', 'power': 2, 'tags': [], 'wins': []},
    {'nome': 'Heitor Gandolfi Cardillo', 'nick': '', 'power': 2, 'tags': [], 'wins': []},
    {'nome': 'Kelly Santos', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Mirle Francielle Alves Ferraz', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Felipe Reiter De Albuquerque', 'nick': '', 'power': 4.8, 'tags': [], 'wins': []},
    {'nome': 'Camila de Almeida Spinelli', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Plinio Marcos Rocha Junior', 'nick': '', 'power': 3.8, 'tags': [], 'wins': []},
    {'nome': 'Bruno Silva Correa', 'nick': '', 'power': 4, 'tags': [], 'wins': []},
    {'nome': 'Thiago Rosinhole', 'nick': 'O Artista das Estrelas', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Jean Carlos Pereira Justino', 'nick': '', 'power': 3.5, 'tags': [], 'wins': []},
    {'nome': 'Henrique Sabella Munoz', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Thiago Ribeiro', 'nick': '', 'power': 2, 'tags': [], 'wins': []},
    {'nome': 'Marcos Vinicius Alves Costa', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Mateus Lazzari', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Stephany Callegari', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Jose Ferraiol Neto', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Ezequiel Cardoso da Silva', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Geisian dos Santos Reis', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Breno de Santana Maran', 'nick': 'Baby Shark', 'power': 2, 'tags': [], 'wins': []},
    {'nome': 'Lívia Genovez Braga', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Alfonso Henrique Haskel', 'nick': 'Tá de Haskel', 'power': 4.3, 'tags': [], 'wins': []},
    {'nome': 'Hiro Augusto Lima Sakuno', 'nick': '', 'power': 4.8, 'tags': [], 'wins': []},
    {'nome': 'Thales Silva', 'nick': 'Thaleco', 'power': 4, 'tags': [], 'wins': []},
    {'nome': 'Rafael de Oliveira Gomes da Silva', 'nick': '', 'power': 6, 'tags': [], 'wins': []},
    {'nome': 'Natan Amorim', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Kaique Fernandes da Silva', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Antonio Cosmo da Silva Neto', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Matheus de Andrade Nicacio Pereira', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Felipe Dutra de Carvalho', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Raniel Pedro Gomes', 'nick': '', 'power': 4.6, 'tags': [], 'wins': []},
    {'nome': 'Rogger Goncalves do Amaral', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Matheus Mello', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Diego Mendonça', 'nick': '', 'power': 4.1, 'tags': [], 'wins': []},
    {'nome': 'Bruno Ferreira Rodrigues', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Antonio Mateus Sousa de Oliveira', 'nick': '', 'power': 3, 'tags': [], 'wins': []},
    {'nome': 'William Aldevino dos Santos', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Christian Ferreira da Silva', 'nick': '', 'power': 5.8, 'tags': [], 'wins': []},
    {'nome': 'Gabriel Pellizzer Caetano', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Matheus Augusto Galeti', 'nick': '', 'power': 3, 'tags': [], 'wins': []},
    {'nome': 'Jonas Felipe Dos Santos', 'nick': 'Joninhas', 'power': 3, 'tags': [], 'wins': []},
    {'nome': 'Fernanda Lira Magalhães', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Tatiana Kaori Abe', 'nick': 'Kaori', 'power': 2, 'tags': [], 'wins': []},
    {'nome': 'Diego Calciolari Gordiano', 'nick': '', 'power': 3.7, 'tags': [], 'wins': []},
    {'nome': 'Anderson Correia da Costa', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Lucas Fegueredo', 'nick': '', 'power': 3.6, 'tags': [], 'wins': []},
    {'nome': 'Fabiano Rodrigues Lima', 'nick': '', 'power': 3, 'tags': [], 'wins': []},
    {'nome': 'Jamylle Thaís Barrense Magalhães', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Israel Fernandes Pereira', 'nick': 'Zanarkand', 'power': 2, 'tags': [], 'wins': ['mj2', 'med']},
    {'nome': 'Thays Roberta do Prado Ribeiro', 'nick': '', 'power': 4.2, 'tags': [], 'wins': []},
    {'nome': 'Renan Santos', 'nick': '', 'power': 4, 'tags': [], 'wins': ['mj2']},
    {'nome': 'Armando Luiz Bretas Neto', 'nick': 'Tretas', 'power': 4.2, 'tags': [], 'wins': ['mj']},
    {'nome': 'Artur Lansoni', 'nick': 'Alien', 'power': 4.3, 'tags': [], 'wins': ['mj']},
    {'nome': 'Pedro Leme', 'nick': 'Peroleme', 'power': 5.5, 'tags': [], 'wins': ['mj', 'mj', 'med']},
    {'nome': 'Pamela de Miranda Pereira', 'nick': 'Pam', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Gustavo Barros', 'nick': 'Gu Barros', 'power': 4, 'tags': [], 'wins': ['mj2']},
    {'nome': 'Caio Vieira Antunes', 'nick': '', 'power': 4, 'tags': [], 'wins': ['mj']},
    {'nome': 'Matheus Luigi Milan Domingues', 'nick': 'Sundays', 'power': 4.6, 'tags': [], 'wins': ['mj']},
    {'nome': 'Renan Calanca Campregher', 'nick': 'É o Bria', 'power': 5.2, 'tags': [], 'wins': ['mj', 'mj']},
    {'nome': 'Erik Calçada', 'nick': 'Calçadão', 'power': 5.5, 'tags': [], 'wins': ['mj']},

    # INATIVOS
    # {'nome': 'Gabriel Rodrigues', 'nick': 'Rodriguinho', 'power': 5, 'tags': [], 'wins': ['mj']},
    # {'nome': 'Marcos Costa', 'nick': 'Costinha', 'power': 5, 'tags': [], 'wins': ['mj']},
    # {'nome': 'Cristian', 'nick': 'Cris', 'power': 5, 'tags': [], 'wins': ['med']},
    # {'nome': 'Renan Deposito', 'nick': 'Materiais de Construção', 'power': 5, 'tags': [], 'wins': ['mj', 'mj']},
    # {'nome': 'Michael Santos', 'nick': '', 'power': 5, 'tags': [], 'wins': ['mj']},
    # {'nome': 'Igor Arena', 'nick': 'de Gladiadores', 'power': 5, 'tags': [], 'wins': ['mj']},
    # {'nome': 'Marco Túlio', 'nick': 'Maravilha', 'power': 5, 'tags': [], 'wins': ['mj']},
    # {'nome': 'Rebeca', 'nick': '', 'power': 5, 'tags': [], 'wins': ['med']},
    # {'nome': 'Ygor', 'nick': 'Capybara', 'power': 5, 'tags': ['dev', 'ambev'], 'wins': ['mj', 'mj']},
    # {'nome': 'Jessica', 'nick': '', 'power': 5, 'tags': ['dev', 'ticket'], 'wins': ['mj']},
    # {'nome': 'Ana Marin', 'nick': 'Golpinho', 'power': 3, 'tags': ['dev', 'azul'], 'wins': []},
    # {'nome': 'Renan Hideki', 'nick': 'Hideki', 'power': 5, 'tags': ['dev', 'ticket'], 'wins': ['mj']},
]

rodada = 0
passo = 1
max_power = 12

shelve_file = shelve.open('rivvals')
shelve_file['rodada'] = rodada
shelve_file['passo'] = passo


@app.route('/')
def index():
    return render_template('index.html', titulo='Draft Settings')


@app.route('/process_form', methods=['GET', 'POST'])
def process_form():
    global jogadores, rodada
    shelve_file['jogo'] = request.form['jogo']
    times = request.form['times']
    shelve_file['n_times'] = times
    p_times = request.form['p_times']
    shelve_file['p_times'] = p_times
    jogadores.sort(reverse=True, key=get_power)

    if request.form['cleverbox']:
        for n in range(1, int(times) + 1):
            time = []
            time.append(jogadores.pop(int(times)-n))
            time[0]['nome'] = time[0]['nome'] + ' (c)'
            shelve_file[str(n)] = time
            shelve_file['power_'+str(n)] = time[0]['power']
        rodada = 1
    else:
        for n in range(1, int(times) + 1):
            shelve_file[str(n)] = []
            shelve_file['power_'+str(n)] = 0
    return redirect(url_for('draft'))


@app.route('/process_next', methods=['GET', 'POST'])
def process_next():
    global passo, rodada, jogadores
    sel = request.form['selected_name']
    if sel == '':
        flash('Selecione um player da lista de escolhas!', 'error')
        return redirect(url_for('draft'))
    for index, jogador in enumerate(jogadores):
        if jogador['nome'] == sel:
            time = shelve_file[str(passo)]
            power = shelve_file['power_'+str(passo)]
            power = float(power) + float(jogador['power'])
            shelve_file['power_' + str(passo)] = power
            time.append(jogadores.pop(index))
            if len(time) == 1:
                time[0]['nome'] = time[0]['nome']+' (c)'
            shelve_file[str(passo)] = time

    flash('Player ' + sel + ' selecionado para time ' + str(passo), 'alert')

    if jogadores == []:
        return redirect(url_for('final'))
    if str(passo) == shelve_file['n_times']:
        rodada += 1
        passo = 1
    else:
        passo += 1
    return redirect(url_for('draft'))


@app.route('/draft', methods=['GET', 'POST'])
def draft():
    global rodada, passo, jogadores
    jogo = shelve_file['jogo']
    n_times = shelve_file['n_times']
    settings = {'jogo': jogo, 'times': n_times}
    time = shelve_file[str(passo)]
    pag_titulo = jogo + ' Rivvals Draft - ' + n_times + ' Equipes'
    jogadores_filtrados = filtrar_jogadores(time, jogadores)
    return render_template('lista.html', titulo=pag_titulo, jogadores=jogadores_filtrados[:10], settings=settings, time=time,
                           rodada=rodada, passo=passo)


@app.route('/final')
def final():
    times = []
    for n in range(1, int(shelve_file['n_times']) + 1):
        times.append(shelve_file[str(n)])
    pag_titulo = "Relatório Final"
    powers = []
    n_times = shelve_file['n_times']
    for n in range(1, int(n_times) + 1):
        powers.append(shelve_file['power_'+str(n)])
    # shelve_file.close()
    return render_template('final.html', titulo=pag_titulo, times=times, powers=powers)


def filtrar_jogadores(time, jogadores):
    global rodada, passo, max_power
    if time == []:
        return jogadores
    avoid_tags = []
    for player in time:
        avoid_tags.extend(player['tags'])

    # any(item in List1 for item in List2) - checa se qualquer item da List1 consta em List2
    filtrados = []
    for player in jogadores:
        if any(item in player['tags'] for item in avoid_tags) == False:
            filtrados.append(player)

    power = shelve_file['power_' + str(passo)]
    # Se tiver batendo no poder máximo só pode escolher jogador de força 1 por rodada
    if max_power - float(power) <= 4:
        filtrados = [
            jogador for jogador in filtrados
            if jogador['power'] == 1
        ]

    if filtrados == []:
        return jogadores
    else:
        return filtrados


def get_power(jogador):
    return float(jogador['power'])


app.run(debug=True)
