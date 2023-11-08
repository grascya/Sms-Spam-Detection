from flask import Flask, request, render_template
import pickle

with open('./model.bin','rb') as f_in:
    (vector,model) = pickle.load(f_in)

app = Flask(__name__,template_folder="template",static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    input = request.form.get('message')
    preprocessing = vector.transform([input])
    prediction = model.predict(preprocessing)

    label_info =''
    if(prediction[0]==0):
        label_info='Ham ✔'
    else:
        label_info = 'Spam 🚨'
    return render_template('index.html', prediction='This message is a: {}'.format(label_info))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)




