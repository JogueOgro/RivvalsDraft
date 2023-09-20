from flask import Flask, render_template, request, redirect, url_for, flash
import shelve

app = Flask(__name__)
app.secret_key = 'rivvals'

jogadores = [
    {'nome': 'Maitê Polydoro', 'nick': 'Mayfolk', 'power': 3, 'tags': [], 'wins': []},
    {'nome': 'Henrique Miguel Gomes dos Anjos', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Marlon Gracietti de Amorim', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Andressa Bernardes Bock', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'André Roberto Milanez', 'nick': 'O CEO', 'power': 3.7, 'tags': [], 'wins': []},
    {'nome': 'Jemima Fonseca Luz', 'nick': '', 'power': 3.6, 'tags': [], 'wins': []},
    {'nome': 'Lucas Costa de Oliveira Alves', 'nick': 'Ai Chaves!', 'power': 4.3, 'tags': [], 'wins': []},
    {'nome': 'Felipe dos Santos Sena Pereira', 'nick': 'Senninha', 'power': 5.2, 'tags': [], 'wins': []},
    {'nome': 'Guilherme Fabrin Franco', 'nick': '', 'power': 2, 'tags': [], 'wins': []},
    {'nome': 'Bruno Raniery Freire Lima', 'nick': 'Raniery', 'power': 3.5, 'tags': [], 'wins': []},
    {'nome': 'Leonan Rodrigues Ferreira', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    {'nome': 'Caio Henrique dos Santos Caldas', 'nick': '', 'power': 3, 'tags': [], 'wins': []},
    {'nome': 'Leonardo Santos', 'nick': 'Leozzera', 'power': 3, 'tags': [], 'wins': ['mj']},
    {'nome': 'Nathan de Freitas Duarte', 'nick': '', 'power': 4.4, 'tags': [], 'wins': ['mj']},
    {'nome': 'Andre Augusto Costa Dionisio', 'nick': '', 'power': 4.6, 'tags': [], 'wins': []},
    {'nome': 'Giuliano de Carvalho Florestano', 'nick': '', 'power': 3, 'tags': [], 'wins': []},
    # {'nome': 'Jessé Oliveira de Freitas', 'nick': 'O CTO', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Glauco Mordente', 'nick': '', 'power': 3, 'tags': [], 'wins': []},
    # {'nome': 'Paula Elvira Picchi Mendes', 'nick': 'Paulinha', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Carlos Almeida', 'nick': '', 'power': 4, 'tags': [], 'wins': []},
    # {'nome': 'Douglas Costa', 'nick': '', 'power': 2, 'tags': [], 'wins': []},
    # {'nome': 'Glaicon da Silva Reis', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Carlos Eduardo Biaseto', 'nick': 'Cadu', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Rodrigo Urbano', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Fred Medeiros', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Patricia Goncalves Teixeira', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Leandro Cavalheri', 'nick': '', 'power': 3.8, 'tags': [], 'wins': []},
    # {'nome': 'Caio Aparecido Rodrigues do Prado', 'nick': '', 'power': 2, 'tags': [], 'wins': []},
    # {'nome': 'Nuno Francisco Nazaré Gonçalves Simão', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Pedro Henrique de Souza Alexandre', 'nick': '', 'power': 4.3, 'tags': [], 'wins': []},
    # {'nome': 'Pamela Leite da Silva', 'nick': '', 'power': 3.5, 'tags': [], 'wins': []},
    # {'nome': 'Rafael Marinho dos Santos', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Narcisio Zeferino Cardoso Junior', 'nick': '', 'power': 3, 'tags': [], 'wins': []},
    # {'nome': 'Mariana Thomaz Rodrigues', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Beatriz Costa de Cerqueira', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Ana Paula de Campos Oliveira', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Marcelo Pinheiro', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Bruno Gonzalez Rodrigues', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Kelvy Correa Nascimento Chagas', 'nick': '', 'power': 3.5, 'tags': [], 'wins': []},
    # {'nome': 'Cristian Silva Macedo', 'nick': 'Mais Cedo', 'power': 4.02, 'tags': [], 'wins': []},
    # {'nome': 'Rafael dos Santos Cardoso', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Rafael Costa', 'nick': '', 'power': 2, 'tags': [], 'wins': []},
    # {'nome': 'Heitor Gandolfi Cardillo', 'nick': '', 'power': 2, 'tags': [], 'wins': []},
    # {'nome': 'Kelly Santos', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Mirle Francielle Alves Ferraz', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Felipe Reiter De Albuquerque', 'nick': '', 'power': 5.1, 'tags': [], 'wins': []},
    # {'nome': 'Camila de Almeida Spinelli', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Plinio Marcos Rocha Junior', 'nick': '', 'power': 3.8, 'tags': [], 'wins': []},
    # {'nome': 'Bruno Silva Correa', 'nick': '', 'power': 4.1, 'tags': [], 'wins': []},
    # {'nome': 'Thiago Rosinhole', 'nick': 'O Artista das Estrelas', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Jean Carlos Pereira Justino', 'nick': '', 'power': 3.5, 'tags': [], 'wins': []},
    # {'nome': 'Henrique Sabella Munoz', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Thiago Ribeiro', 'nick': '', 'power': 2, 'tags': [], 'wins': []},
    # {'nome': 'Marcos Vinicius Alves Costa', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Mateus Lazzari', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Stephany Callegari', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Jose Ferraiol Neto', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Ezequiel Cardoso da Silva', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Geisian dos Santos Reis', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Breno de Santana Maran', 'nick': 'Baby Shark', 'power': 2, 'tags': [], 'wins': []},
    # {'nome': 'Lívia Genovez Braga', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Alfonso Henrique Haskel', 'nick': 'Tá de Haskel', 'power': 4.5, 'tags': [], 'wins': []},
    # {'nome': 'Hiro Augusto Lima Sakuno', 'nick': '', 'power': 5, 'tags': [], 'wins': []},
    # {'nome': 'Thales Silva', 'nick': 'Thaleco', 'power': 4.01, 'tags': [], 'wins': []},
    # {'nome': 'Rafael de Oliveira Gomes da Silva', 'nick': '', 'power': 6, 'tags': [], 'wins': []},
    # {'nome': 'Natan Amorim', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Kaique Fernandes da Silva', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Antonio Cosmo da Silva Neto', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Matheus de Andrade Nicacio Pereira', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Felipe Dutra de Carvalho', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Raniel Pedro Gomes', 'nick': '', 'power': 4.6, 'tags': [], 'wins': []},
    # {'nome': 'Rogger Goncalves do Amaral', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Matheus Mello', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Diego Mendonça', 'nick': '', 'power': 4.3, 'tags': [], 'wins': []},
    # {'nome': 'Bruno Ferreira Rodrigues', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Antonio Mateus Sousa de Oliveira', 'nick': '', 'power': 3, 'tags': [], 'wins': []},
    # {'nome': 'William Aldevino dos Santos', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Christian Ferreira da Silva', 'nick': '', 'power': 5.8, 'tags': [], 'wins': []},
    # {'nome': 'Gabriel Pellizzer Caetano', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Matheus Augusto Galeti', 'nick': '', 'power': 3, 'tags': [], 'wins': []},
    # {'nome': 'Jonas Felipe Dos Santos', 'nick': 'Joninhas', 'power': 3, 'tags': [], 'wins': []},
    # {'nome': 'Fernanda Lira Magalhães', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Tatiana Kaori Abe', 'nick': 'Kaori', 'power': 2, 'tags': [], 'wins': []},
    # {'nome': 'Diego Calciolari Gordiano', 'nick': '', 'power': 3.7, 'tags': [], 'wins': []},
    # {'nome': 'Anderson Correia da Costa', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Lucas Fegueredo', 'nick': '', 'power': 3.6, 'tags': [], 'wins': []},
    # {'nome': 'Fabiano Rodrigues Lima', 'nick': '', 'power': 3, 'tags': [], 'wins': []},
    # {'nome': 'Jamylle Thaís Barrense Magalhães', 'nick': '', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Israel Fernandes Pereira', 'nick': 'Zanarkand', 'power': 2, 'tags': [], 'wins': ['mj2', 'med']},
    # {'nome': 'Thays Roberta do Prado Ribeiro', 'nick': '', 'power': 4.4, 'tags': [], 'wins': []},
    # {'nome': 'Renan Santos', 'nick': '', 'power': 4.2, 'tags': [], 'wins': ['mj2']},
    # {'nome': 'Armando Luiz Bretas Neto', 'nick': 'Tretas', 'power': 4.5, 'tags': [], 'wins': ['mj']},
    # {'nome': 'Artur Lansoni', 'nick': 'Alien', 'power': 5, 'tags': [], 'wins': ['mj']},
    # {'nome': 'Pedro Leme', 'nick': 'Peroleme', 'power': 5.4, 'tags': [], 'wins': ['mj', 'mj', 'med']},
    # {'nome': 'Pamela de Miranda Pereira', 'nick': 'Pam', 'power': 1, 'tags': [], 'wins': []},
    # {'nome': 'Gustavo Barros', 'nick': 'Gu Barros', 'power': 3.9, 'tags': [], 'wins': ['mj2']},
    # {'nome': 'Caio Vieira Antunes', 'nick': '', 'power': 4.1, 'tags': [], 'wins': ['mj']},
    # {'nome': 'Matheus Luigi Milan Domingues', 'nick': 'Sundays', 'power': 4.2, 'tags': [], 'wins': ['mj']},
    # {'nome': 'Renan Calanca Campregher', 'nick': 'É o Bria', 'power': 5.3, 'tags': [], 'wins': ['mj', 'mj']},
    # {'nome': 'Erik Calçada', 'nick': 'Calçadão', 'power': 5.5, 'tags': [], 'wins': ['mj']},

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


@app.route('/')
def index():
    return render_template('index.html', titulo='Menu')

@app.route('/schedules_settings')
def schedules_settings():
    return render_template('schedules_settings.html', titulo='Schedules Settings')

@app.route('/generate_json')
def generate_json():
    shelve_file = shelve.open('rivvals', writeback=True)
    chosen = []
    try:
        schedules = shelve_file['schedules']
    except:
        schedules = []
    teams = shelve_file["teams"]
    for team in teams:
        for player in team:
            if schedules:
                for schedule in schedules:
                    if schedule['player'] == player['nome']:
                        player['schedule'] = schedule['schedule']
            chosen.append(player)
    chosen.sort(key=alphabetical)
    shelve_file['chosen'] = chosen
    shelve_file.close()
    return render_template('generate_json.html', jogadores=chosen, titulo='Gerar Json')

@app.route('/load_json')
def load_json():
    return render_template('load_json.html', titulo='Carregar Json')

@app.route('/check_schedules')
def check_schedules():
    shelve_file = shelve.open('rivvals', writeback=True)
    n_times = shelve_file['n_times']
    chosen = shelve_file['chosen']
    shelve_file.close()
    return render_template('check_schedules.html', n_times=n_times, jogadores=chosen, titulo='Checar Horarios')

@app.route('/show_results', methods=['GET', 'POST'])
def show_results():
    final_schedules = [{'SEG': 0, 'TER': 0, 'QUA': 0, 'QUI': 0, 'SEX': 0, 'SEGPLAYERS': '', 'TERPLAYERS': '', 'QUAPLAYERS': '', 'QUIPLAYERS':'', 'SEXPLAYERS':''},
                       {'SEG': 0, 'TER': 0, 'QUA': 0, 'QUI': 0, 'SEX': 0, 'SEGPLAYERS': '', 'TERPLAYERS': '', 'QUAPLAYERS': '', 'QUIPLAYERS':'', 'SEXPLAYERS':''},
                       {'SEG': 0, 'TER': 0, 'QUA': 0, 'QUI': 0, 'SEX': 0, 'SEGPLAYERS': '', 'TERPLAYERS': '', 'QUAPLAYERS': '', 'QUIPLAYERS':'', 'SEXPLAYERS':''},
                       {'SEG': 0, 'TER': 0, 'QUA': 0, 'QUI': 0, 'SEX': 0, 'SEGPLAYERS': '', 'TERPLAYERS': '', 'QUAPLAYERS': '', 'QUIPLAYERS':'', 'SEXPLAYERS':''}]
    filtered_schedules = []
    team = int(request.form['time'])
    team2 = int(request.form['time2'])
    shelve_file = shelve.open('rivvals', writeback=True)
    schedules = shelve_file['schedules']
    shelve_file.close()
    for schedule in schedules:
        if schedule['team'] == team or schedule['team'] == team2:
            filtered_schedules.append(schedule)
    for schedule in filtered_schedules:

        for day in schedule['schedule']:
            horario = day[-1]
            sigla = day[0:3]
            final_schedules[int(horario)-1][sigla] += 1
            final_schedules[int(horario) - 1][sigla+'PLAYERS'] = final_schedules[int(horario) - 1][sigla+'PLAYERS'] + ' ' + \
                                                           schedule['player']
    return render_template('show_results.html', schedules=final_schedules, titulo='Conflitos de Horário - Time '+str(team)+' e Time '+str(team2))
@app.route('/save_json', methods=['GET', 'POST'])
def save_json():
    shelve_file = shelve.open('rivvals', writeback=True)
    schedules = []
    last = 0
    chosen = shelve_file['chosen']
    for entrada in request.form:
        bits = entrada.split("_")
        if last == bits[1]:
            schedules[-1]["schedule"].append(bits[2])
            last = bits[1]
        else:
            schedules.append({"player": chosen[int(bits[1])-1]["nome"], "team": chosen[int(bits[1])-1]["team"], "schedule": [bits[2]]})
            last = bits[1]
    shelve_file["schedules"] = schedules
    shelve_file.close()
    flash('Json criado, pode checar os horarios!')
    return render_template('schedules_settings.html', titulo='Schedules Settings')

@app.route('/groups_settings')
def groups_settings():
    return render_template('groups_settings.html', titulo='Group Draw Settings')


@app.route('/process_groups_settings', methods=['GET', 'POST'])
def process_groups_settings():
    n_grupos = int(request.form['n_grupos'])
    n_times = int(request.form['n_times'])
    return render_template('groups_draw.html', titulo='Group Draw Settings', n_grupos=n_grupos, n_times=n_times)


@app.route('/draft_settings')
def draft_settings():
    return render_template('draft_settings.html', titulo='Draft Settings')


@app.route('/captains')
def captains():
    global rodada
    shelve_file = shelve.open('rivvals', writeback=True)
    times = shelve_file['n_times']
    for n in range(1, int(times) + 1):
        time = []
        jogadores[int(times)-n]["team"] = n
        time.append(jogadores.pop(int(times)-n))
        time[0]['nome'] = time[0]['nome'] + ' (c)'
        shelve_file[str(n)] = time
        shelve_file['power_'+str(n)] = time[0]['power']
    rodada = 1
    shelve_file.close()
    return redirect(url_for('draft'))


@app.route('/balance')
def balance():
    powers = []
    shelve_file = shelve.open('rivvals', writeback=True)
    n_times = shelve_file['n_times']
    for n in range(1, int(n_times) + 1):
        powers.append(shelve_file['power_' + str(n)])
    shelve_file.close()
    return render_template('balance.html', titulo='Força do Balanceamento', powers=powers)

@app.route('/process_form', methods=['GET', 'POST'])
def process_form():
    global jogadores, rodada
    shelve_file = shelve.open('rivvals', writeback=True)
    shelve_file['jogo'] = request.form['jogo']
    times = request.form['times']
    shelve_file['n_times'] = times
    p_times = request.form['p_times']
    shelve_file['p_times'] = p_times
    jogadores.sort(reverse=True, key=get_power)
    capitaes = jogadores[:int(times)]
    capitaes.sort(key=get_power)
    try:
        if request.form['cleverbox']:
            shelve_file.close()
            return render_template('captains.html', titulo='Capitães Rivvals', capitaes=capitaes)
    except:
        for n in range(1, int(times) + 1):
            shelve_file[str(n)] = []
            shelve_file['power_' + str(n)] = 0
            shelve_file.close()
        return redirect(url_for('draft'))


@app.route('/process_next', methods=['GET', 'POST'])
def process_next():
    global passo, rodada, jogadores
    sel = request.form['selected_name']
    if sel == '':
        flash('Selecione um player da lista de escolhas!', 'error')
        return redirect(url_for('draft'))
    shelve_file = shelve.open('rivvals', writeback=True)
    for index, jogador in enumerate(jogadores):
        if jogador['nome'] == sel:
            time = shelve_file[str(passo)]
            power = shelve_file['power_'+str(passo)]
            power = float(power) + float(jogador['power'])
            shelve_file['power_' + str(passo)] = power
            jogadores[index]["team"] = passo
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
        shelve_file.close()
    return redirect(url_for('draft'))


@app.route('/draft', methods=['GET', 'POST'])
def draft():
    global rodada, passo, jogadores
    shelve_file = shelve.open('rivvals', writeback=True)
    jogo = shelve_file['jogo']
    n_times = shelve_file['n_times']
    settings = {'jogo': jogo, 'times': n_times}
    time = shelve_file[str(passo)]
    shelve_file.close()
    pag_titulo = jogo + ' Rivvals Draft - ' + n_times + ' Equipes'
    jogadores_filtrados = filtrar_jogadores(time, jogadores)
    return render_template('lista.html', titulo=pag_titulo, jogadores=jogadores_filtrados[:10], settings=settings, time=time,
                           rodada=rodada, passo=passo)


@app.route('/final')
def final():
    times = []
    shelve_file = shelve.open('rivvals', writeback=True)
    for n in range(1, int(shelve_file['n_times']) + 1):
        times.append(shelve_file[str(n)])
    shelve_file["teams"] = times
    pag_titulo = "Relatório Final"
    shelve_file.close()
    return render_template('final.html', titulo=pag_titulo, times=times)

@app.route('/db_teams')
def check_db_teams():
    global shelve_file
    return shelve_file['teams']

@app.route('/db_schedules')
def check_db_schedules():
    global shelve_file
    return shelve_file['schedules']

@app.route('/db_dump')
def db_dump():
    shelve_file = shelve.open('rivvals', writeback=True)
    dump = list(shelve_file.items())
    shelve_file.close()
    return dump


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
    shelve_file = shelve.open('rivvals', writeback=True)
    power = shelve_file['power_' + str(passo)]
    # Se tiver batendo no poder máximo só pode escolher jogador de força 1 por rodada
    if max_power - float(power) <= 4:
        filtrados = [
            jogador for jogador in filtrados
            if jogador['power'] == 1
        ]
    shelve_file.close()
    if filtrados == []:
        return jogadores
    else:
        return filtrados


def get_power(jogador):
    return float(jogador['power'])


def alphabetical(jogador):
    return jogador['nome']


app.run(debug=True)
