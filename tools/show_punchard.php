<?php

require_once "punchcard.php";
echo "\n\n\n\n";
echo "Ignore above stuff from default punchcard.\n";
echo "\n\n\n\n";

$card = file_get_contents("punchcard.txt");
echo ibm029decode($card,true);
echo "\n";
?>
