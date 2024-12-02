from http.server import HTTPServer,  BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>properties</title>
    <style>
        *{
             background-color: rgb(113, 220, 242);
        }
        table {
            text-align: center;
            width: 60%;
            border-collapse: collapse;
            margin: 100px 0px;
           
        }
        th, td {
            border: 2px solid #1a1a17;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #c2e2c2;
        }
        .head{
            text-align: center;
            font-size: 80px;
            
        }

           
            
        
        
    </style>
</head> 
<body>
    <div class="head">
        <b>DEVICE PROPERTIES</b>
    </div>
<center>
    <table style="border: 10px;">
        <tr>
            <th>DEVICE NAME</th>
            <td>GOJO</td>
        </tr>
        <tr>
            <th>PROCESSOR</th>
            <td>13th Gen Intel(R) Core(TM) i7-1335U   1.30 GHz</td>
        </tr>
        <tr>
            <th>Installed RAM</th>
            <td>16.0 GB (15.7 GB usable)</td>
        </tr>
        <tr>
            <th>DEVICES ID</th>
            <td>15EEA3B2-7EF5-4DEC-903D-577382C3C005</td>
        </tr>
        <tr>
            <th>PRODUCT ID</th>
            <td>00342-42708-95366-AAOEM</td>
        </tr>
        <tr>
            <tr>
                <th>SYSTEM TYPE</th>
                <td>64-bit operating system, x64-based processor</td>
        </tr>
        <tr>
            <th>PEN AND TOUCH</th>
            <td>touch support with 3 touch points</td>
        </tr>                            
    </table>
    </center>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response (200)
        self.send_header('content-type','text-html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address =('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my server is running...")
httpd.serve_forever()        
        