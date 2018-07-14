<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Illness</title>
</head>

<body>
</body>
</html>


<?PHP
	
	
	$input = $_GET["illness"];
	echo exec("python parseIllness.py 2>&1 $input");

?>	