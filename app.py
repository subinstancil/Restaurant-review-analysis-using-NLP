from flask import *
import NLPrun
import scrapReview
import re





def mainfunction(url):
    scrapReview.scrap(url,10000)
    string_url = str(10000)+".txt"
    rating, count, pstve = NLPrun.rate(string_url)
    return rating, count, pstve; 





app = Flask(__name__)  


@app.route('/')  
def upload():  
	return render_template("predict.html")  

@app.route('/scrap', methods = ['POST'])  
def succesaass():
    if request.method == 'POST':
        text = request.form['urls']
        rating, count, pstve = mainfunction(text)
        if rating == "exit":	
            rating, count, pstve = mainfunction(text)
        else:
            neg = int(count)-int(pstve)
            return render_template("htl_rating.html", **locals())
    return render_template("htl_rating.html", **locals())    
	# if request.method == 'POST':  
	# 	return render_template("1.html", name = "asd") 
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        comment = request.form['comment']
        my_prediction = NLPrun.pred(comment)
        return render_template('result.html', prediction=my_prediction)
    return render_template('predict.html')


@app.route('/rte',methods=['GET','POST'])
def rting():
    if request.method == 'POST':
        return render_template('rating.html')
    return render_template('rating.html')




@app.route('/ratelist',methods=['GET','POST'])
def ratelist():
    listOfUrls = []
    with open('listfile.txt', 'r') as filehandle:
        for line in filehandle:
            urls = line[:-1]
            listOfUrls.append(urls)
    if request.method == 'POST':
        text = request.form['url']
        cont=1       
        for i in listOfUrls:
            print("xx")
            if i == text:
                string_url = str(cont)+".txt"
                print(string_url)
                rating, count, pstve = NLPrun.rate(string_url)
                print(rating, count, pstve)
            cont +=1
        neg = int(count)-int(pstve)
        return render_template("htl_rating.html", **locals())
    return render_template('ratelist.html', len = len(listOfUrls), ListOfUrls = listOfUrls)


if __name__ == '__main__':  
	app.run(threaded=True)  
	app.debug = True


