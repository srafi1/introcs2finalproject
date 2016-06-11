var x = 11;
var y = 6;
var enc = '';

function start() {
	x = parseInt(document.getElementById('xcoord').innerHTML);
	y = parseInt(document.getElementById('ycoord').innerHTML);
	enc = document.getElementById('encounters').innerHTML;
	window.scrollTo(0, 170);
	draw();
}

function draw() {
	var c = document.getElementById('rpg');
	var ctx = c.getContext('2d');
	var rpg = document.getElementById('map');
	var sprite = document.getElementById('sprite');
	var watersprite = document.getElementById('watersprite');
	ctx.drawImage(rpg, 0, 0, 840, 490);
	if (x < 10 && y > 7) ctx.drawImage(watersprite, x*35, y*35 - 15, 35, 45);
	else ctx.drawImage(sprite, x*35, y*35 - 15, 35, 45);
}

function encounter() {
	var chance = 6*Math.random();
	if (chance < 1) {
		var area = '';
		if (x < 10) {
			if (y < 6) area = 'grass';
			else area = 'water';
		} else {
			if (y < 6) area = 'desert';
			else area = 'random';
		}
	 window.location = 'encounter.py?area=' + area + '&x=' + x + '&y=' + y + '&encounters=' + enc;
	}
}

window.onkeydown = function(e) {
	e.preventDefault();
	//movement
	var key = e.keyCode;
	if (key == 80 || key == 79) return;
	if (key == 37) x--;
	if (key == 38) y--;
	if (key == 39) x++;
	if (key == 40) y++;
	//correction for out of screen
	if (x < 0 || x > 23 || y < 0 || y > 13) {
		if (x < 0) x++;
		if (x > 23) x--;
		if (y < 0) y++;
		if (y > 13) y--;
		return;
	}
	if ((x == 15 && y == 2) || (x == 22 && y == 5) || (x == 17 && y == 3) || (x == 17 && y == 4) || (x == 18 && y == 3) || (x == 18 && y == 4)) {
		var go = 2;
		if ((x == 15 && y == 2) || (x == 22 && y == 5)) go = 1;
		for (var i = 0; i < go; i++) {
			if (key == 37) x--;
			if (key == 38) y--;
			if (key == 39) x++;
			if (key == 40) y++;
		}
	}
	if ((x < 10 && (y < 6 || y > 7)) || (x > 13 && (y < 6 || y > 7))) encounter();
	draw();
};
