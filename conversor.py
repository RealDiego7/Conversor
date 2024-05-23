from flask import Flask, request, send_file
import zebrafy

app = Flask(__name__)

# Rota para a página inicial
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Obtém o código ZPL do formulário
        zpl_code = request.form.get("zpl_code")

        # Converte ZPL para PDF
        pdf_bytes = zpl_code.encode("utf-8")  # Converta a string para bytes

        # Salve o PDF em um arquivo temporário
        with open("output.pdf", "wb") as pdf_file:
            pdf_file.write(pdf_bytes)

        return f"""
        <h1>PDF gerado com sucesso!</h1>
        <a href="/download_pdf"><button>Download PDF</button></a>
        """
    else:
        return """
        <form method="post">
            <textarea name="zpl_code" rows="10" cols="50" placeholder="Insira o código ZPL aqui"></textarea>
            <br>
            <input type="submit" value="Converter para PDF">
        </form>
        """

# Rota para baixar o PDF
@app.route("/download_pdf")
def download_pdf():
    return send_file("output.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
