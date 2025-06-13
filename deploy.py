# from flask import Flask, render_template, request
# import pickle



# app = Flask(__name__)
# #load the model
# model = pickle.load(open('savemodel.sav', 'rb'))

# @app.route('/')
# def home():
#     result = ''
#     return render_template('form.html', **locals())

# @app.route('/predict', methods=['POST'])
# def predict():

    # Bwd_Pkt_Len_Std = float(request.form['Bwd_Pkt_Len_Std'])
    # PSH_Flag_Cnt = float(request.form['PSH_Flag_Cnt'])
    # Fwd_Seg_Size_Min = float(request.form['Fwd_Seg_Size_Min'])
    # Bwd_Pkt_Len_Min = float(request.form['Bwd_Pkt_Len_Min'])
    # ACK_Flag_Cnt = float(request.form['ACK_Flag_Cnt'])
    # Fwd_IAT_Std = float(request.form['Fwd_IAT_Std'])
    # Init_Fwd_Win_Byts = float(request.form['Init_Fwd_Win_Byts'])
    # Flow_IAT_Max = float(request.form['Flow_IAT_Max'])
    # Bwd_Pkts = float(request.form['Bwd_Pkts/s'])
    # Bwd_IAT_Tot = float(request.form['Bwd_IAT_Tot'])
    # URG_Flag_Cnt = float(request.form['URG_Flag_Cnt'])
    # Pkt_Len_Min = float(request.form['Pkt_Len_Min'])
    # result = model.predict([[Bwd_Pkt_Len_Std, PSH_Flag_Cnt, Fwd_Seg_Size_Min, Bwd_Pkt_Len_Min, ACK_Flag_Cnt, Fwd_IAT_Std, Init_Fwd_Win_Byts, Flow_IAT_Max, Bwd_Pkts, Bwd_IAT_Tot, URG_Flag_Cnt, Pkt_Len_Min]])[0]
#     return render_template('form.html',**locals())

     






# if __name__== '__main__' :
#     app.run(debug=True)
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load your trained machine learning model
model = joblib.load('savemodel.sav')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        Bwd_Pkt_Len_Std = float(request.form['Bwd_Pkt_Len_Std'])
        PSH_Flag_Cnt = float(request.form['PSH_Flag_Cnt'])
        Fwd_Seg_Size_Min = float(request.form['Fwd_Seg_Size_Min'])
        Bwd_Pkt_Len_Min = float(request.form['Bwd_Pkt_Len_Min'])
        ACK_Flag_Cnt = float(request.form['ACK_Flag_Cnt'])
        Fwd_IAT_Std = float(request.form['Fwd_IAT_Std'])
        Init_Fwd_Win_Byts = float(request.form['Init_Fwd_Win_Byts'])
        Flow_IAT_Max = float(request.form['Flow_IAT_Max'])
        Bwd_Pkts = float(request.form['Bwd_Pkts/s'])
        Bwd_IAT_Tot = float(request.form['Bwd_IAT_Tot'])
        URG_Flag_Cnt = float(request.form['URG_Flag_Cnt'])
        Pkt_Len_Min = float(request.form['Pkt_Len_Min'])
        # Make prediction using your model
        result = model.predict([[Bwd_Pkt_Len_Std, PSH_Flag_Cnt, Fwd_Seg_Size_Min, Bwd_Pkt_Len_Min, ACK_Flag_Cnt, Fwd_IAT_Std, Init_Fwd_Win_Byts, Flow_IAT_Max, Bwd_Pkts, Bwd_IAT_Tot, URG_Flag_Cnt, Pkt_Len_Min]])
        prediction = "ANOMALY DETECTED!!!" if result[0] != 0 else "NO ANOMALY DETECTED!!!"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, render_template, request
# import joblib

# app = Flask(__name__)

# # Load your trained machine learning model
# model = joblib.load('savemodel.sav')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     prediction = None

#     if request.method == 'POST':
#         Dst_Port = float(request.form['Dst_Port'])
#         FlowDuration = float(request.form['FlowDuration'])
#         TotLen_Bwd_Pkts = float(request.form['TotLen_Bwd_Pkts'])
#         Bwd_Pkt_Len_Mean = float(request.form['Bwd_Pkt_Len_Mean'])
#         Flow_Pkts = float(request.form['Flow_Pkts/s'])
#         Flow_IAT_Mean = float(request.form['Flow_IAT_Mean'])
#         Flow_IAT_Max = float(request.form['Flow_IAT_Max'])
#         Fwd_Header_Len = float(request.form['Fwd_Header_Len'])
#         Fwd_Pkts = float(request.form['Fwd_Pkts/s'])
#         Pkt_Len_Max = float(request.form['Pkt_Len_Max'])
#         # URG_Flag_Cnt = float(request.form['URG_Flag_Cnt'])
#         # Pkt_Len_Min = float(request.form['Pkt_Len_Min'])
#         # Make prediction using your model
#         result = model.predict([[Dst_Port, FlowDuration, TotLen_Bwd_Pkts, Bwd_Pkt_Len_Mean, Flow_Pkts, Flow_IAT_Mean, Flow_IAT_Max, Fwd_Header_Len, Fwd_Pkts, Pkt_Len_Max]])
#         prediction = "ANOMALY DETECTED!!!" if result[0] != 0 else "NO ANOMALY DETECTED!!!"

#     return render_template('index.html', prediction=prediction)

# if __name__ == '__main__':
#     app.run(debug=True)
