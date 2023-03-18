
class Server:
    def template(title):
        html_template = """
<!DOCTYPE html>
<html>
    <head>
        <title>"""+title+"""</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body{color: white;background-color: black;display: flex;justify-content: center;flex-direction: column;align-items: center;}
            div{margin: 1em 0;}
            label{font-weight: bold;margin-right: 0.5em;text-transform: capitalize;}
            label:after{content: ":";}
            span.class-temp:after{content: " C";}
            span.class-hum:after{content: "%%";}
        </style>
    </head>
    <body>
        <h1>"""+title+"""</h1>
        %s
    </body>
</html>
                """
        return html_template
