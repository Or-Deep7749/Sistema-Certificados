from flask import Flask, request, send_file
from flask_cors import CORS

from reportlab.pdfgen import canvas

app = Flask(__name__)

CORS(app)

@app.route("/")
def home():
    return{
        "Mensagem":"Api python fucionando!"
    }

@app.route("/certificado", methods=["POST"])
def certificado():
    dados = request.get_json()

    nome = dados["nome"]
    curso = dados["curso"]
    carga = dados["cargaHoraria"]

    arquivo = "certificado.pdf"

    pdf = canvas.Canvas(arquivo)

    pdf.setFont(
        "Helveltica-Bold",
        22
    )

    pdf.drawCentredString(
        300,
        750,
        "CERTIFICADO"
    )

    pdf.setFont(
        "Helveltica",
        14
    )

    pdf.drawCentredString(
        300,
        600,
        f"Certificamos que {nome}"
    )

    pdf.drawCentredString(
            300,
            600,
            f"concluiu o curso {curso}"
        )

    pdf.drawCentredString(
            300,
            600,
            f"carga horária: {carga}"
    )

    pdf.save

    return send_file(
        arquivo,
        as_attachment=True,
        download_name="certificado.pdf"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)