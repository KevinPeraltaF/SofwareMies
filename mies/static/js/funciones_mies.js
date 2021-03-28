/** funcion para abrir el modal de editar */
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
