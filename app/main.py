import enum
from flask import Flask,request, jsonify
from engine import pdf_to_image,process_audio,process_photo,process_text
app = Flask("MLE Challenge")


@app.route('/',methods=["GET"])
def hello_world():
    return 'This API is for Tawadros MLE Challenge'


@app.route('/audio', methods=['POST'])
def do_process_audio():
    try  :
        input_json = request.get_json(force=True)
        if input_json['outPath'][-1] !='/':
            outPath=input_json['outPath']+'/'
        else:
            outPath=input_json['outPath']
        ChunkPaths=process_audio(input_json['Path'],outPath)
        returns={"ChunkPaths":ChunkPaths,"numberOfChunks":len(ChunkPaths)}
        return jsonify(returns)
    except Exception as E:
        text_exp="There is a problem in the request or the JSON format and the exception caught is  "
        print(text_exp+str(E))
        dictToReturn_err_exp = {'Error':text_exp+str(E)}
        return jsonify(dictToReturn_err_exp)



@app.route('/photo', methods=['POST'])
def do_process_photo():
    try :
        input_json = request.get_json(force=True)
        all_faces=[]
        all_positions=[]
        all_paths=[]
        if input_json['outPath'][-1] !='/':
            outPath=input_json['outPath']+'/'
        else:
            outPath=input_json['outPath']
        if input_json['IsPDF']==True:
            
            paths=pdf_to_image(input_json['Path'],outPath)
            for ind,path in enumerate(paths):
                numFaces,positions,PicOutPath=process_photo(path,outPath+str(ind))
                all_faces.append(numFaces)
                all_positions.append(positions.tolist())
                all_paths.append(PicOutPath)
        else:
            numFaces,positions,PicOutPath=process_photo(input_json['Path'],outPath)
            all_faces.append(numFaces)
            all_positions.append(positions.tolist())
            all_paths.append(PicOutPath)
        print(type(all_positions))
        #
        returns={"Face":all_faces,"Path":all_paths,"Position":all_positions}
        return jsonify(returns)

    except Exception as E:
        text_exp="There is a problem in the request or the JSON format and the exception caught is  "
        print(text_exp+str(E))
        dictToReturn_err_exp = {'Error':text_exp+str(E)}
        return jsonify(dictToReturn_err_exp)







@app.route('/text', methods=['POST'])
def do_process_text():
    try :
        input_json = request.get_json(force=True)
        values=input_json['text'].encode('utf-8')
        text=values.decode('utf-8')

        if input_json['language'] in ['AR','EN']:
            predictions=process_text(text,input_json['language'])
            returns={"predictions":predictions,'wordsNumber':len(predictions)}
            return jsonify(returns)

        else:
            Choosetext = "Please Choose Between AR or EN"
            return jsonify({'WrongLang':Choosetext})
            
    except Exception as E:
        text_exp="There is a problem in the request or the JSON format and the exception caught is  "
        print(text_exp+str(E))
        dictToReturn_err_exp = {'Error':text_exp+str(E)}
        return jsonify(dictToReturn_err_exp)


# HTTP Errors handlers
@app.errorhandler(404)
def url_error(E):
    return """
    Wrong URL!
    <pre>{}</pre>""".format(E), 404


@app.errorhandler(500)
def server_error(E):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(E), 500



if __name__ == '__main__':
    app.run(debug=True, port=7000)
