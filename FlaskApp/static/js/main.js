function start(){
	console.log("Hello World!");
}

$(start);
   $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });