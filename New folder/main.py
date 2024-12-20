from flask import Flask, render_template, request
import json 
import urllib.request

app=Flask(__name__)

@app.route('/', method=['POST','GET'])
def details():
    if request.method =='POST':
        location = request.form.get("location")
        api_key = 'AQwhmdsNoAXIAMKQY6lWSTNt_2Gg5rgc63hYO4_hBps'

        try:
             url= f'https://geocode.search.hereapi.com/v1/geocode?apikey={api_key}&q={location}'
             source = urllib.request.urlopen(url).read()

             print(f"API Response(raw):{source}")

             responseData = json.loads(source)

             if 'items' in responseData and len(responseData['item']) >0:
                 
                 data={
                     "latitude":str(responseData['item'][0]['position']['lat']),
                     "longitude":str(responseData['item'][0]['position']['lng']),
                 }
                 return render_template('index.html', data=data, apikey=api_key)
             else:
                 return render_template('index.html', data = data, apikey=api_key)
        except Exception as e:
            print(f"Error:{e}")
            return render_template('index.html',error="something went wrong. plz try again")

    return render_template('index.html')
if __name__=="__main__":
     app.run(host='0.0.0.0', port =8080)



             
        
             
                 
                

            

        

        



 