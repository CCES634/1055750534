from flask import Flask, request, jsonify
from random import randint
app= Flask (__name__)
@app.route("/raiz", methods=["GET"])
def raiz():
	numero=random.randint(1,10000)
	raiz=numero**(1/2)
	return jsonify({
		"numero": numero,
		"raiz": raiz
	}), 200

app.run(debug=True)
