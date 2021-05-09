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
function agregar_inputs(){
    $('.select').select2("destroy");
    var total_forms = document.querySelectorAll('#jsTotalForms input[type=hidden]')[0];
    var value_last = parseInt(total_forms.value)-1;
    //nuevo label e input para periferico
    var nuevo_label_periferico = document.createElement('label');
    nuevo_label_periferico.innerHTML = 'Periferico'
    var nuevo_select_periferico = document.querySelector('#id_equipodetalle_set-'+value_last+'-periferico').cloneNode(true);
    nuevo_select_periferico.name = 'equipodetalle_set-'+total_forms.value+'-periferico';
    nuevo_select_periferico.id = 'id_equipodetalle_set-'+total_forms.value+'-periferico';
    nuevo_select_periferico.className = 'form-control select'
    //nuevo label e input para cantidad
    var nuevo_label_cantidad = document.createElement('label');
    nuevo_label_cantidad.innerHTML = 'Cantidad'
    var nuevo_select_cantidad = document.querySelector('#id_equipodetalle_set-'+value_last+'-cantidad').cloneNode(true);
    nuevo_select_cantidad.name = 'equipodetalle_set-'+total_forms.value+'-cantidad';
    nuevo_select_cantidad.id = 'id_equipodetalle_set-'+total_forms.value+'-cantidad';
    //nuevo label e input para eliminar
    var nuevo_label_eliminar = document.createElement('label');
    nuevo_label_eliminar.innerHTML = 'Eliminar'
    nuevo_label_eliminar.className = 'col-md-12'
    nuevo_label_eliminar.style.top = "40px"
    nuevo_label_eliminar.style.bottom = "40px"
    var nuevo_select_eliminar = document.querySelector('#id_equipodetalle_set-'+value_last+'-DELETE').cloneNode(true);
    nuevo_select_eliminar.name = 'equipodetalle_set-'+total_forms.value+'-DELETE';
    nuevo_select_eliminar.id = 'id_equipodetalle_set-'+total_forms.value+'-DELETE';
    nuevo_select_eliminar.className = ' col-md-12'
    nuevo_select_eliminar.style.top = "40px"
    nuevo_select_eliminar.style.bottom = "40px"

    var cantidadElemen = document.querySelectorAll("#js_periferico");
    var cantidadElemen_cantidad = document.querySelectorAll("#js_cantidad");
    var cantidadElemen_eliminar = document.querySelectorAll("#js_eliminar");
    for (let i=0; i< cantidadElemen.length; i++){
        if (i == cantidadElemen.length-1){
            cantidadElemen[i].appendChild(nuevo_label_periferico);
            cantidadElemen[i].appendChild(nuevo_select_periferico);
            cantidadElemen_cantidad[i].appendChild(nuevo_label_cantidad);
            cantidadElemen_cantidad[i].appendChild(nuevo_select_cantidad);
            cantidadElemen_eliminar[i].appendChild(nuevo_label_eliminar);
            cantidadElemen_eliminar[i].appendChild(nuevo_select_eliminar);
        }
    }
    total_forms.value = parseInt(total_forms.value)+1;

    $(function () {
        $('.select').select2(
            { theme: "bootstrap4", }
        );
    });
}



