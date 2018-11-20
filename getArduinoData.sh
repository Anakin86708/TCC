#!/bin/bash
#CONFIGURAÇÃO PÁGINA HTML
ip="localhost"
pagina="dados.html"

#Download da página
wget $ip/$pagina || 

#Caso falhe ao obter a página
echo "Falha ao obter a página $ip/$pagina" &&

#Script em Python para insert dos dados
python insertArduino.py || 

#Caso falhe no script Python
echo "Falha ao executar o scrip Python"

#Remove a página
rm -f $pagina


