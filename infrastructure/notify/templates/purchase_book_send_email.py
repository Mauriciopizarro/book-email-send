

def get_body_book_purchase():
    body = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Confirmación Compra de Libro</title>
        <style>
            body {
                font-family: 'Georgia', serif;
                background-color: #f7f4f1;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 600px;
                margin: 20px auto;
                background-color: #ffffff;
                padding: 20px;
                border: 1px solid #e0d7d3;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                position: relative;
            }
            h1 {
                color: #7b4b35;
                text-align: center;
                font-family: 'Georgia', serif;
            }
            p {
                font-size: 16px;
                color: #5e4a3d;
                line-height: 1.6;
            }
            .book-details {
                text-align: center;
                margin: 20px 0;
            }
            .book-details img {
                max-width: 200px;
                border-radius: 10px;
            }
            .book-details h2 {
                font-size: 24px;
                color: #7b4b35;
            }
            .book-details p {
                font-size: 18px;
                color: #5e4a3d;
            }
            .instructions {
                text-align: center;
                margin: 30px 0;
            }
            .instructions p {
                font-size: 18px;
                color: #7b4b35;
                font-weight: bold;
            }
            .button {
                display: inline-block;
                padding: 12px 25px;
                background-color: #f7b79a;
                color: #ffffff;
                text-decoration: none;
                border-radius: 5px;
                margin-top: 20px;
                font-size: 18px;
                font-family: 'Georgia', serif;
            }
            .floral {
                position: absolute;
                top: -20px;
                left: -20px;
                width: 120px;
            }
            .floral-right {
                position: absolute;
                top: -20px;
                right: -20px;
                width: 120px;
                transform: scaleX(-1);
            }
            .footer {
                text-align: center;
                font-size: 14px;
                color: #a89d94;
                margin-top: 30px;
            }
        </style>    
    </head>
        <body>
            <div class="container">
                <img src="https://i.ibb.co/SNz4kpb/pngwing-com-1.png" alt="Flores" class="floral">
                <img src="https://i.ibb.co/SNz4kpb/pngwing-com-1.png" alt="Flores" class="floral-right">
                <h1>¡Gracias por tu compra!</h1>
                <p>Hemos recibido tu pedido para el siguiente libro:</p>
                <div class="book-details">
                    <img src="https://i.ibb.co/gMjmGKy/Whats-App-Image-2024-09-10-at-10-11-45-PM.jpg" alt="4000 dias para transformarte">
                    <h2>4000 dias para transformarte</h2>
                    <p>Julia Alexandra Garcia</p>
                </div>
                <div class="instructions">
                    <p>Por favor, responde a este correo con la dirección donde deseas recibir el libro.</p>
                    <a href="mailto:tu-email@tudominio.com" class="button">Responder con mi Dirección</a>
                </div>
        
                <p>Si tienes alguna pregunta o necesitas más información, no dudes en contactarnos.</p>
                <p class="footer">Saludos cordiales,<br>Equipo de Ventas</p>
            </div>
        </body>
    </html>
    """

    return body