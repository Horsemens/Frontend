console.log("added")
$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
})