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

    // $('.alert').delay(1000).hide('slow');
});
