Juego de la Pirámide de Palitos

Descripción

El Juego de la Pirámide de Palitos es un juego de estrategia en el que los jugadores deben retirar palitos de una pirámide. El objetivo es evitar retirar el último palito para no perder la partida. Algunos palitos son especiales y pueden desencadenar eventos aleatorios que afectan el desarrollo del juego.

Reglas del Juego

Objetivo:

Retira entre 1 y 3 palitos por turno.

El jugador que retire el último palito pierde.

Palitos Rojos:

Al retirar un palito rojo, se activa un evento aleatorio.

Si se retiran varios palitos rojos en un turno, solo se ejecuta un evento.

Eventos Aleatorios:

Evento 1: El jugador pierde su próximo turno.

Evento 2: Se agregan entre 1 y M palitos a la pirámide.

Evento 3: El 20% de los palitos se congelan por 3 turnos y no pueden ser retirados.

Evento 4: ¡Bomba! El jugador debe retirar una fila completa.

Evento 5: Se reinicia la pirámide con todos los palitos, manteniendo los palitos rojos.

Instrucciones de Uso

Ejecutar el juego:

python nombre_del_script.py

Opciones del Menú Principal:

Comenzar el juego: Inicia una nueva partida.

Reglas: Muestra las reglas del juego.

Salir: Cierra la aplicación.

Estructura del Código

Funciones Principales:

evento_4(piramide): Permite al jugador retirar una fila completa.

evento_4_ia(piramide): La IA retira una fila aleatoria.

evento_5(piramide, filas_piramide): Reinicia la pirámide.

recuento_de_palitos(jugador_actual, palitos_sacados): Lleva el conteo de palitos retirados por cada jugador.

comparar_ganador_palitos(palitos_sacados_ia, palitos_sacados_usuario): Compara los palitos retirados y determina al ganador.

main(): Función principal que gestiona el flujo del juego.

Dependencias

Python 3.x

Colorama: Para el manejo de colores en la consola.

pip install colorama

Créditos

Desarrollado por [Tu Nombre].

¡Diviértete jugando al Juego de la Pirámide de Palitos! 🎉

