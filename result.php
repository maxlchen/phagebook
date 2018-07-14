<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Illness Search</title>
</head>

<body>
</body>
</html>

<?PHP
	
	
	$input = $_GET["illness"];
	echo shell_exec("python parseIllness.py 2>&1 $input");

?>