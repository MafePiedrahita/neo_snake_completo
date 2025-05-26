## Descripción del Problema. 
Este proyecto tiene como objetivo rediseñar y mejorar el clásico juego Snake, incorporando una jugabilidad más dinámica, nuevas mecánicas, y un entorno visual más intuitivo. Se busca ofrecer una experiencia interactiva que combine desafío, adaptabilidad y control preciso por parte de los jugadores.
La lógica del juego se organiza a partir de clases que representan los elementos esenciales del mundo: la serpiente, sus movimientos, su crecimiento al alimentarse, la aparición de obstáculos, la gestión del tiempo y la puntuación en pantalla. El sistema debe permitir una interacción fluida y coherente entre estos elementos, garantizando una partida funcional y equilibrada.
Además, se incorporan diferentes niveles de dificultad que modifican la velocidad, los recursos disponibles y las condiciones del entorno, lo que amplía la rejugabilidad del juego. La interacción con los jugadores se refuerza mediante una interfaz que muestra el estado de la partida en tiempo real, incluyendo el puntaje, los power-ups activos y el tiempo restante cuando aplique.
En conjunto, Neo-Snake propone una versión enriquecida del clásico, manteniendo su esencia pero apostando por una estructura más sólida, modular y escalable que permita futuras expansiones.

## Modelo del mundo. 
### Identificación de entidades y características:
Con base en el enunciado se identifican las siguientes entidades (clases) y características (atributos):
#### Neo_Snake:
1. Dificultad
2. Jugador
3. Nivel
4. Puntaje
#### Serpiente
1. Cabeza
2. Cuerpo
3. Cola
#### Segmentos
1. Dirección
2. Velocidad
#### Alimento
1. Tipo
2. Posición
#### Obstáculos
1. Tipo
2. Posición
#### PowerUp
1. Tipo
2. Posición
3. Duración
#### Puntaje
1. Puntos
#### Jugador
1. Jugadores
#### Interfaz
1. Pantallas (menú, juego)
