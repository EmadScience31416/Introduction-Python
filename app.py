from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal (/) que se ejecutará cuando se visite la URL raíz
@app.route("/")
def index():
    """
    Lee el valor actual del contador desde count.txt,
    lo incrementa en uno, actualiza el archivo y envía
    el valor a la plantilla index.html para mostrarlo.
    """
    # Abrir el archivo count.txt en modo lectura y obtener el número
    with open("count.txt", "r") as f:
        count = int(f.read().strip() or 0)

    # Incrementar el contador en uno
    count += 1

    # Guardar el nuevo valor en count.txt
    with open("count.txt", "w") as f:
        f.write(str(count))

    # Renderizar la plantilla y pasar la variable count
    # 🔹 "Renderizar" significa *procesar una plantilla HTML (index.html)*
    # y devolverla como una página completa al navegador.
    # Flask usa `render_template()` para combinar el HTML con variables de Python.
    # Por ejemplo:
    # - En tu plantilla index.html puedes tener algo como:
    #       <h1>Contador: {{ count }}</h1>
    #   Flask reemplaza {{ count }} por el valor que le pases desde Python.
    # 🔹 Ejemplo rápido:
    # Si en tu código haces: render_template("saludo.html", nombre="Emanuel")
    # y en tu HTML tienes:  <p>Hola {{ nombre }}</p>
    # → el navegador mostrará: "Hola Emanuel"
    return render_template("index.html", count2=count)




#Es una condición especial que se usa para saber si el archivo se está ejecutando directamente
#  o si se está importando como módulo desde otro script.

# Básicamente le estás diciendo a Python:

# “Oye, si este archivo se está ejecutando directamente (no importado), haz esto.”


if __name__ == "__main__":


    # Ejecutar la aplicación Flask en modo debug para recargar automáticamente.
    # 🔹 `debug=True` hace dos cosas:
    #   1. Activa el "modo depuración": si ocurre un error, Flask muestra un mensaje detallado
    #      en el navegador para ayudarte a encontrar la causa.
    #   2. Recarga automática: cada vez que editas tu código, el servidor se reinicia solo.
    #
    # 🔸 Si NO pones `debug=True`:
    #   - Tendrás que reiniciar manualmente el servidor cada vez que cambies el código.
    #   - Y si hay un error, Flask solo mostrará una página genérica de error sin detalles técnicos.
    app.run(debug=True)



# Flask usa el mismo comportamiento con los archivos estáticos.
# Por defecto busca una carpeta llamada static (para CSS, imágenes, JS, etc.),
# a menos que tú cambies el nombre y lo indiques así:

# app = Flask(__name__, static_folder="archivos_estaticos")


# En Flask (que usa el motor de plantillas Jinja2), las llaves {{ variable }}
#  sirven para insertar valores de Python dentro del HTML.

# 🧠 ¿Qué es Jinja2?

# Jinja2 es el motor de plantillas (template engine) que usa Flask para generar páginas HTML dinámicas.

# En cristiano: te permite combinar código HTML con variables y lógica de Python — sin tener que escribir todo el HTML a mano cada vez que cambia algo.

# 🧩 ¿Qué hace exactamente?

# Cuando usas esto en tu código Flask:

# return render_template("index.html", nombre="Emanuel", edad=28)


# Flask manda esas variables (nombre y edad) a Jinja2,
# y este reemplaza los valores dentro de tu plantilla HTML, por ejemplo:

# <p>Hola {{ nombre }}, tienes {{ edad }} años.</p>


# 🡒 Al procesarse, Jinja2 genera el HTML final así:

# <p>Hola Emanuel, tienes 28 años.</p>


# Y eso es lo que ve el navegador.

# 🧠 Jinja2 es una librería de Python

# Literalmente, Jinja2 es un módulo (paquete) escrito en Python que sirve para generar archivos de texto dinámicos,
# especialmente HTML.

# Es decir, no es parte del lenguaje Python por defecto: viene como una dependencia 
# instalada junto con Flask (cuando haces pip install flask, ya se instala Jinja2 también).