function show(id,action){
    descricao = document.getElementById('descricao-'+id).innerText;
    document.getElementById('code').value = id;
    if(action=='edit'){
        $('#editor').summernote('reset');
        $('#editor').summernote('pasteHTML', descricao);
        document.getElementById('titulo').value =document.getElementById('titulo-'+id).innerText;
        document.getElementById('news-capa').src =document.getElementById('news-capa-'+id).src;
        //document.getElementById('form').method = 'PATCH';
    }
    else{
        document.getElementById('rem-titulo').value = document.getElementById('titulo-'+id).innerText;
        document.getElementById('rem-descricao').value = descricao;
        //document.getElementById('form').method = 'DELETE';
    }
}

function act(action){
    id = document.getElementById('code').value;
    document.getElementById('form').action = './'+id;
    if(action=='edit'){
        document.getElementById('code').value = 'u';
    }
    else{
        document.getElementById('code').value = 'e';
    }
    document.getElementById('form').submit();
}