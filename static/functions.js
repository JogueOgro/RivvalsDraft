// Contador
var segundos = 60;

// Update a cada 1s
var x = setInterval(function() {

  segundos = segundos - 1;

  // Display no elemnto timer
  document.getElementById('timer').innerHTML = segundos + 's ';

  // Quando acaba escreve que acabou
  if (segundos < 0) {
    clearInterval(x);
    document.getElementById('timer').innerHTML = 'TEMPO ACABADO';
  }
}, 1000);

var current_team = 1
var current_group = 1
var setup = true;
var listaTimes = [];

function setUp (totalTimes) {
    for (var i = 1; i <= totalTimes; i++) {
        // console.log(i);
        listaTimes.push(i);
    }
}

function updateLista (time, totalTimes) {
    var novaLista = [];
    for (var i = 1; i <= totalTimes; i++) {
        if (i !== time) {
            novaLista.push(i);
        }
    }
    listaTimes = novaLista;
}



$(document).ready(function() {

    $('tbody#tb_escolhas tr').click(function () {
        var tr = $(this).closest('tr').hide().clone();
        tr.attr('id', 'chosen');
        tr.show()
        $('#time tbody').append(tr);
        $('#selected_name').attr('value', tr.find('td.nome').text())
    });

    $('a#undo').click(function () {
        var tr = $('tr#chosen').remove();
        $('tbody#tb_escolhas tr').show()
        $('#selected_name').attr('value', '')
    });

    $('a#draw').click(function () {
        var n_times = $('meta#my_data').data('n_times');
        var n_grupos = $('meta#my_data').data('n_grupos');
        var totalTimes = n_grupos*n_times;

        if (setup == true) {
            // alert(setup);
            setUp(totalTimes);
            setup = false;
        }
        // alert(setup);

        sorteado = Math.floor(Math.random() * totalTimes) + 1;
        console.log(sorteado);
        updateLista(sorteado, totalTimes);
        console.log(listaTimes);
        alert('td#coords_'+current_group+current_team);
        $('td#coords_'+current_group+current_team).html("Time "+sorteado);

        current_group++;
        if (current_group > n_grupos) {
            current_group = 1;
            current_team++;
        }
    });

});
