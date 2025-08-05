<?php
// Definir dados de login pelo código enquanto não há banco de dados
$php_username = "Admin";
$php_password = "12345678";

// Dados do formulário
$form_username = $_POST['username'] ? $_POST['username'] : "";
$form_password = $_POST['password'] ? $_POST['password'] : "";

// Verifica se estão corretos 
if (!($form_password === $php_password) || !($form_username === $php_username)) {
    // Redireciona de volta com erro
    header("Location: login.html?error=1");
    exit;
}
// Redireciona para a home
header("Location: index.html");
exit;   