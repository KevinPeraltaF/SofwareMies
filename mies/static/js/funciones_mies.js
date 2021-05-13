/** funcion para abrir el modal de editarr */

function abrirModalEditar(url){
            
    $('#editar').load(url,function(){
        $('#editar').modal('show');
    }
    )           
}

/** funcion para abrir el modal de eliminar */
function abrirModalEliminar(url){
            
    $('#eliminar').load(url,function(){
        $('#eliminar').modal('show');
    }
    )           
}


/** funcion para abrir el modal de eliminar */
function abrirModalDetalle(url){
            
    $('#detalle').load(url,function(){
        $('#detalle').modal('show');
    }
    )           
}



$(document).ready(function (){
    $('.solo-letra').bind('keypress', function(event) {
        var regex = new RegExp("^[a-zA-Z ]+$");
        var key = String.fromCharCode(!event.charCode ? event.which : event.charCode);
        if (!regex.test(key)) {
          event.preventDefault();
          return false;
        }
      }
    
    );
  });

  $(document).ready(function (){
    $('.solo-numero').bind('keypress', function(event) {
        var regex = new RegExp("^[0-9]");
        var key = String.fromCharCode(!event.charCode ? event.which : event.charCode);
        if (!regex.test(key)) {
          event.preventDefault();
          return false;
        }
      }
    
    );
  });
 