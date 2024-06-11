import flask

server = flask.Flask(__name__)

@server.route("/get_anime", methods=["GET"])
def function1():
    anime_dict = {
        "Name" : "Naruto",
        "Year" : "1999",
        "Heroes" : ["Naruto", "Saske", "Sakura"]
    }
    return anime_dict

@server.route("/get_film", methods=["GET"])
def function2():
    film_dict = {
        "first" : {
            "Name" : "Friend Robot",
            "Year" : "1999",
        },
        "second" : {
            "Name" : "Oleg",
            "Year" : "2000",
        },
        "third" : {
            "Name" : "Titanic",
            "Year" : "1997"
        }
    }
    return film_dict

@server.route("/chat_Oleg", methods=["POST"])
def function3():
    print(flask.request.json["Text"])
    answer_to_Yarik = input()
    return {"success": answer_to_Yarik}

server.run(host="0.0.0.0")
