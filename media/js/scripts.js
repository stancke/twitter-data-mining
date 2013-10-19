function random()
{
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    for( var i=0; i < 1; i++ )
        text += possible.charAt(Math.floor(Math.random() * possible.length));

    return text;
}


$('document').ready(function(){
	
	 $("#btnBusca").mouseover(function() {
		    $(this).removeClass('ui-state-default').addClass('ui-state-hover');
		  }).mouseout(function(){
		    $(this).removeClass('ui-state-hover').addClass('ui-state-default');
		  });
	 
	 $("#btnGerarXml").mouseover(function() {
		    $(this).removeClass('ui-state-default').addClass('ui-state-hover');
		  }).mouseout(function(){
		    $(this).removeClass('ui-state-hover').addClass('ui-state-default');
		  });
	
	$("#btnBusca").click(function(){
		buscaAjax();
	});
	
	
	
	function buscaAjax()
	{
		$.ajax({
			type: "POST",
			data: $("#frmBusca").serialize(),
			url: "busca/",
			beforeSend: function(){
				$("#resultado").html("<img style='margin-left: 650px; margin-top: 200px' src='media/images/loader.gif'/>");
			},
			success: function(data){
				$("#resultado").html(data);
			}
		});
	}
	
	$("#btnBuscaAleatoria").click(function(){ 
		
		$("#palavra_chave").val(random());
		
		if($("#intervalo").val() != "")
		{
			setInterval(function(){
				buscaAjax();
				$("#palavra_chave").val(random());
			},$("#intervalo").val() * 1000);
		}else{
			buscaAjax();
		}
	});
	
	$("#btnGerarXml").click(function(){
		window.location = 'xml/';
	});

});