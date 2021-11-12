from flask import Flask
import flask
import random

def create_app():
    app = Flask(__name__)
    return app

copypasta_arr = [
    "Confesión #51601",
    "Cabros vengo a compartir mi SUPER MALA CUEA.",
    "Resulta que yo estoy en un movimiento scout, y hace unos meses había creado una cuenta de memes de la página que era de memes del movimiento. La cuenta la había creado solo para mis amigos en un inicio.",
    "El viernes se unió una nueva generación de scouts, entre los cuales se encontraba una mina que yo me quería jotear. Ayer toda esa nueva generación se unió al grupo de WhatsApp (el cual ahora tenía un total de 200 wnes)",
    "Hace un par de horas decidí hacer pública la página, para todos los miembros del movimiento. Por eso, mandé el link de la página por el grupo de todos los scouts diciendo que todos eran bienvenidos.",
    "Minutos después, la mina que me quiero jotear solicitó la página, y yo le tome ss a la solicitud pa mandarla por mi grupo de amigos. La cosa es que mande el ss y puse de caption 'Objetivo cumplido'.",
    "Sin embargo, 5 minutos después, me di cuenta que HABIA MANDADO ESE SS CON ESE CAPTION POR EL GRUPO GENERAL DE SCOUTS (EL CON LOS 200 WNES (Y CON LA MINA EN EL GRUPO)).",
    "Claramente para cuando me di cuenta y borré el mensaje, era muy tarde. Ya todo el grupo me estaba webeando con la wea.",
    "Después de 20 minutos de pensar que mierda hago y de hablarlo con mis amigos, decidí mandarle un audio a la mina por instagram (para que no pueda compartirlo sin darse la paja de grabar la pantalla) pidiéndole disculpas y chamullandole que sin querer había tocado su solicitud cuando quería tomarle ss a la página entera.",
    "Le mandé el audio y me respondió una wea como 'JAJAJA tranquiii'.",
    "En resumen señoras y señores, estoy pasando la vergüenza de me vida ctm y hasta ahora me siguen webeando por el grupo general.",
    "MORALEJA: NUNCA TOMEN SCREENSHOTS",
]


app = create_app()

@app.route('/', methods=['GET'])
def get_copypasta():
    file = random.choice(["main.html", "main_navon.html"])

    return flask.render_template(file), 200

@app.route('/docs', methods=['GET'])
def get_docs():
    return flask.render_template('docs.html'), 200

@app.route('/fragment', methods=['GET'])
def random_fragment():
    return random.choice(copypasta_arr)

@app.route('/daniel', methods=['GET'])
def get_daniel():
    return flask.render_template('daniel.html'), 200

@app.route('/navon', methods=['GET'])
def get_navon():
    return flask.render_template('navon.html'), 200


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return flask.render_template('404.html'), 404

@app.route('/herbert', methods=['GET'])
def get_image():
    index = random.randint(1,9)
    filename = f"./herbert/{index}.png"
    return flask.send_file(filename, mimetype='image/png')

@app.route('/jac', methods=['GET'])
def jac():
    filename = f"./herbert/jac.png"
    return flask.send_file(filename, mimetype='image/png')

@app.route('/whois', methods=['GET'])
def whois():
    user = flask.request.args.get('anon')
    print(user)
    return flask.render_template('danielanon.html', data={ "anon": user }), 200

if __name__ == '__main__':
    app.run(port = 9420)
