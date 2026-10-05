from flask import Flask, request, send_file
from flask_cors import CORS
from reportlab.pdfgen import canvas

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {
        "Mensagem": "Api python funcionando!"
    }

@app.route("/certificado", methods=["POST"])
def certificado():
    dados = request.get_json()

    nome = dados.get("nome", "")
    curso = dados.get("curso", "")
    carga = dados.get("cargaHoraria", "")

    arquivo = "certificado.pdf"

    pdf = canvas.Canvas(arquivo, pagesize=(595, 842))

    pdf.setFont("Helvetica-Bold", 26)
    pdf.drawCentredString(297, 700, "CERTIFICADO")

    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(297, 580, "Certificamos para os devidos fins que")
    
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(297, 530, nome)

    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(297, 480, f"concluiu com êxito o curso de {curso}")
    pdf.drawCentredString(297, 440, f"com a carga horária total de {carga}.")

    pdf.line(100, 220, 250, 220)
    pdf.setFont("Helvetica", 11)
    pdf.drawCentredString(175, 200, "Assinatura do Aluno")
    pdf.line(345, 220, 495, 220)
    pdf.drawCentredString(420, 200, "Coordenador do Curso")

    pdf.save()

    return send_file(
        arquivo,
        as_attachment=True,
        download_name="certificado.pdf"
    )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)  