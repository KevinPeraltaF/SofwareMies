var tblProducts;
var vents = {
    items :{
        fechaIngreso :'',
        responsable :'',
        ubicacion:'',
        categoria:'',
        descripcion:'',
        marca:'',
        modelo:'',
        condicion:'',
        serie:'',
        codigoMies:'',
        direccionIp:'',
        direccionMac:'',
        capacidadDisco:'',
        capacidadMemoria:'',
        capacidadProcesador:'',
        foto:'',
        detalle:[]
    },
    add: function (item) {
        if (item.cantidad <1) {
            alert("No hay stock")
        }else{
        this.items.detalle.push(item);
        this.list();
        }
    },
    list: function () {
        tblProducts = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            searching: false,
            ordering:  false,
            lengthChange: false,
            paging:false,
            data: this.items.detalle,
            columns: [
                {"data": "id"},
                {"data": "descripcion"},
                {"data": "cant"}
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat" style="color: white;"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
                {
                    targets: [2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cant" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.cant + '">';
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="cant"]').TouchSpin({
                    min: 1,
                    max: data.cantidad,
                    step: 1
                });

            },
            initComplete: function (settings, json) {

            }
        });}
};
  
$(function(){
    $('#tblProducts tbody')
    .on('click', 'a[rel="remove"]', function () {
        var tr = tblProducts.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Estas seguro de eliminar el producto de tu detalle?', function () {
            vents.items.detalle.splice(tr.row, 1);
            vents.list();
        });
    })
    .on('change', 'input[name="cant"]', function () {
        console.clear();
        var cant = parseInt($(this).val());
        var tr = tblProducts.cell($(this).closest('td, li')).index();
        vents.items.detalle[tr.row].cant = cant;
    });
    $('form').on('submit', function (e) {
        e.preventDefault();

        if (vents.items.detalle.length === 0) {
            message_error('Debe al menos tener un item en su detalle de venta');
            return false;
        }
        var parameters = new FormData($('#demo').get(0));
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('vents', JSON.stringify(vents.items));
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            location.href = '/Equipo';
        });
    });
    $('#id_periferico').select2({
        language:'es',
        allowClear:true,
        placeholder: 'Ingrese una descripción'
    }).on('select2:select', function(e){
        var data = e.params.data;
        data.descripcion = data.text;
        for (var i=0; i< vents.items.detalle.length; i++) {
            if (data.descripcion == vents.items.detalle[i].descripcion){
                $(this).val('').trigger('change.select2');
                alert('Ya existe');
                return false;
            }
        }
        data.cant = 1;
        vents.add(data);
        $(this).val('').trigger('change.select2');
    });
    vents.list();
});