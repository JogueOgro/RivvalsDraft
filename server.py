from flask import Flask, render_template, request, redirect, url_for, flash
import shelve

app = Flask(__name__)
app.secret_key = 'rivvals'

jogadores = [
    {'nome': 'Joaozinho', 'nick': 'Capybara', 'power': 5, 'tags': ['dev', 'ambev'], 'wins': ['mj', 'mj']},
    {'nome': 'Israel', 'nick': 'Zanarkand', 'power': 5, 'tags': ['dev', 'ticket'], 'wins': ['mj2', 'med']},
    {'nome': 'Marcelo Tenório', 'nick': 'Valdoy', 'power': 4, 'tags': ['ppl', 'ambev'], 'wins': ['mj', 'med']},
    {'nome': 'Ana Marin', 'nick': 'Golpinho', 'power': 3, 'tags': ['dev', 'azul'], 'wins': []},
    {'nome': 'Pamela', 'nick': 'PAM', 'power': 3, 'tags': ['psi'], 'wins': []},
    {'nome': 'Jessé', 'nick': 'Rasta', 'power': 4, 'tags': ['ppl', 'rh'], 'wins': []},
    {'nome': 'Cadu', 'nick': 'CaduSSJ', 'power': 3, 'tags': ['rh', 'ambev'], 'wins': ['med']},
    {'nome': 'André Milanez', 'nick': 'Milanez', 'power': 4, 'tags': ['clvl'], 'wins': ['med']},
    {'nome': 'André Tirich', 'nick': 'Tiriri', 'power': 4, 'tags': ['fin'], 'wins': ['mj']},
    {'nome': 'Gustavo Barros', 'nick': 'Gu Barros', 'power': 4, 'tags': ['azul', 'ambev'], 'wins': ['mj2']},
    {'nome': 'Neto', 'nick': 'Fimose 5cm', 'power': 3, 'tags': ['dev', 'rh'], 'wins': []},
    {'nome': 'Rayane', 'nick': 'SenhoraTPM', 'power': 3, 'tags': ['cln'], 'wins': []},
    {'nome': 'Thales', 'nick': 'Thaleco', 'power': 4, 'tags': ['dev', 'azul'], 'wins': []},
]

rodada = 0
passo = 1

shelve_file = shelve.open('rivvals')
shelve_file['rodada'] = rodada
shelve_file['passo'] = passo


@app.route('/')
def index():
    return render_template('index.html', titulo='Draft Settings')


@app.route('/process_form', methods=['GET', 'POST'])
def process_form():
    global jogadores
    shelve_file['jogo'] = request.form['jogo']
    times = request.form['times']
    shelve_file['n_times'] = times
    jogadores.sort(reverse=True, key=get_power)

    for n in range(1, int(times) + 1):
        shelve_file[str(n)] = []
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
    return render_template('lista.html', titulo=pag_titulo, jogadores=jogadores_filtrados, settings=settings, time=time,
                           rodada=rodada, passo=passo)


@app.route('/final')
def final():
    times = []
    for n in range(1, int(shelve_file['n_times']) + 1):
        times.append(shelve_file[str(n)])
    pag_titulo = "Relatório Final"
    shelve_file.close()
    return render_template('final.html', titulo=pag_titulo, times=times)


def filtrar_jogadores(time, jogadores):
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

    if filtrados == []:
        return jogadores
    else:
        return filtrados


def get_power(jogador):
    return int(jogador['power'])


app.run(debug=True)
